from hashlib import new
from operator import eq
from flask import request,send_file
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
from sqlalchemy import desc,asc
from werkzeug.utils import secure_filename
import os,shutil
from pathlib import Path
from tareas import convertir_archivos, convertir_archivos_test

from modelos import db,Usuario, UsuarioSchema,Tarea,TareaSchema
from google.cloud import storage
from google.cloud import pubsub_v1

usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()
formats = ['mp3','acc','ogg','wav','wma']

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path('conversor-audio', 'new_task_pubsub')

storage_client = storage.Client()
BUCKET_NAME = "audio-conversor-files"
bucket = storage_client.bucket(BUCKET_NAME)

def upload_to_gcs(local_route, gcs_route):
  blob = bucket.blob(gcs_route)
  blob.upload_from_filename(local_route)

def download_from_gcs(gcs_route, local_route):
  blob = bucket.blob(gcs_route)
  blob.download_to_filename(local_route)

class VistaSignIn(Resource):

    def post(self):
        usuario = Usuario.query.filter(Usuario.username == request.json["username"]).first()
        correo = Usuario.query.filter(Usuario.email == request.json["email"]).first()
        if usuario is not None:
            return {"error": "El usuario ingresado ya esta en uso"}
        elif correo is not None:
            return {"error": "El correo ingresado ya esta en uso"}
        elif request.json["password1"]  != request.json["password2"] :
            return {"error": "Las contraseñas no coinciden"}
        else:
            nuevo_usuario = Usuario(username=request.json["username"], password=request.json["password1"],  email=request.json["email"])
            db.session.add(nuevo_usuario)

            db.session.commit()
            return {"mensaje": "usuario creado exitosamente", "id": nuevo_usuario.id}


class VistaLogIn(Resource):

    def post(self):
        if request.json == None or not "username" in request.json or not "password" in request.json:
          return {'error': 'Ingrese usuario y contraseña'}

        
        usuario = Usuario.query.filter(Usuario.username == request.json["username"],
                                       Usuario.password == request.json["password"]).first()
        db.session.commit()
        if usuario is None:
            return "Usuario o Contraseña no validos", 404
        else:
            token_de_acceso = create_access_token(identity=usuario.id)
            return {"mensaje": "Inicio de sesión exitoso", "token": token_de_acceso}



class VistaTarea(Resource):            
    @jwt_required()
    def get(self, id):
        uid = get_jwt_identity()
        return [tarea_schema.dump(ca) for ca in Tarea.query.filter(Tarea.id_user==uid , Tarea.id==id).all()]

    @jwt_required()
    def put(self, id):
        uid = get_jwt_identity()
        if request.json == None or not "newFormat" in request.json:
            return {'error': 'Debe ingresar un formato destino'}
        elif request.json["newFormat"].lower()  not in formats:
            return {'error': 'El formato a convetir ingresado no es sorportado'}

        tarea = Tarea.query.get_or_404(id)
        tarea.newFormat = request.json.get("newFormat", tarea.newFormat)
        tarea.status = 'uploaded'
        db.session.commit()

        #convertir_archivos.apply_async(kwargs={'id':tarea.id}, countdown=60)
        data = {"tareaId":tarea.id}
        publisher.publish(topic_path, str(data).encode("utf-8"), taskid=str(tarea.id))
        return tarea_schema.dump(tarea)

    def delete(self, id):
        tarea = Tarea.query.get_or_404(id)
        db.session.delete(tarea)
        db.session.commit()
        return {'mensaje': 'Tarea Eliminada Correctamente'}

class VistaTareas(Resource):
    @jwt_required()
    def get(self):
        uid = get_jwt_identity()
        args = request.args
        registros = args.get("max", default=1000, type=int)
        orden = args.get("order", default=0, type=int)

        if registros <1:
            registros = 1000
        if orden == 1:
            return [tarea_schema.dump(ca) for ca in Tarea.query.filter(Tarea.id_user==uid).order_by(desc(Tarea.id)).limit(registros).all()]
        else:
            return [tarea_schema.dump(ca) for ca in Tarea.query.filter(Tarea.id_user==uid).order_by(asc(Tarea.id)).limit(registros).all()]

    @jwt_required()
    def post(self):
        
        uid = get_jwt_identity()
        
        if 'fileName' not in request.files:
            return {'error': 'Se debe cargar un archivo'}

        file = request.files['fileName']
        if file.filename == '':
            return {'error': 'no se detecto archivo'}
        fileName = file.filename 
        
        if request.form == None or not "newFormat" in request.form:
            return {'error': 'Debe ingresar un formato destino'}
        elif request.form["newFormat"].lower()  not in formats:
            return {'error': 'El formato a convetir ingresado no es sorportado'}
        newFormat = request.form['newFormat']

        if '.' in fileName and fileName.rsplit('.', 1)[1].lower() in formats:
            filename = secure_filename(file.filename)
            nuevo_tarea = Tarea(id_user=uid,fileName=filename,newFormat = newFormat,status = 'uploaded')
            db.session.add(nuevo_tarea)
            db.session.commit()
            dir = "./uploads/"+str(nuevo_tarea.id)+"/old/"
            path = Path(dir)
            path.mkdir(parents=True)
            file.save(os.path.join(dir, filename))
            upload_to_gcs(f"./uploads/{nuevo_tarea.id}/old/{filename}",f"uploads/{nuevo_tarea.id}/old/{filename}")
            #convertir_archivos.apply_async(kwargs={'id':nuevo_tarea.id}, countdown=60)
            data = {"tareaId":nuevo_tarea.id}
            publisher.publish(topic_path, str(data).encode("utf-8"), taskid=str(nuevo_tarea.id))
            #publisher.publish(topic_path, nuevo_tarea.id)
            return {"mensaje": "Tarea creada exitosamente", "id": nuevo_tarea.id}
        else:
            return {'error': 'El formato del archivo ingresado no es valido'}
        
        
class VistaArchivos(Resource):
    @jwt_required()
    def get(self,id,estado):
        uid = get_jwt_identity()
        tarea = Tarea.query.get_or_404(id)
        if estado == "convertido":
            file_name, file_extension = os.path.splitext(tarea.fileName)
            file_extension = file_extension.replace(".","")
            tarea.fileName = tarea.fileName.replace(file_extension,tarea.newFormat)
            gcs_dir = "uploads/"+str(id)+"/new/"+tarea.fileName
        else:
            gcs_dir = "uploads/"+str(id)+"/old/"+tarea.fileName
        print(gcs_dir)
        print(tarea.newFormat)
        local_file_name = f"./downloads/{tarea.fileName}"
        download_from_gcs(gcs_dir, local_file_name)
        if os.path.isfile(local_file_name):
            return send_file(local_file_name)
        else:
            return {"error": "Archivo No disponible"}
        
        
class VistaTest(Resource):

    @jwt_required()
    def post(self):
        
        uid = get_jwt_identity()
        
        if 'fileName' not in request.files:
            return {'error': 'Se debe cargar un archivo'}

        file = request.files['fileName']
        if file.filename == '':
            return {'error': 'no se detecto archivo'}
        fileName = file.filename 
        
        if request.form == None or not "newFormat" in request.form:
            return {'error': 'Debe ingresar un formato destino'}
        elif request.form["newFormat"].lower()  not in formats:
            return {'error': 'El formato a convetir ingresado no es sorportado'}
        newFormat = request.form['newFormat']

        cantidad = request.form['cantidad']

        if '.' in fileName and fileName.rsplit('.', 1)[1].lower() in formats:
            for i in range(int(cantidad)):
              filename = secure_filename(file.filename)
              nuevo_tarea = Tarea(id_user=uid,fileName=filename,newFormat = newFormat,status = 'uploaded')
              db.session.add(nuevo_tarea)
              db.session.commit()
              dir = "uploads/"+str(nuevo_tarea.id)+"/old/"
              path = Path(dir)
              path.mkdir(parents=True)

              file.save(os.path.join(dir, filename))
              #convertir_archivos_test.apply_async(kwargs={'id':nuevo_tarea.id},countdown=1)
              data = {"tareaId":nuevo_tarea.id}
              publisher.publish(topic_path, str(data).encode("utf-8"), taskid=str(nuevo_tarea.id), target="test")
              #publisher.publish(topic_path, nuevo_tarea.id)
            
            return {"mensaje": "Tarea creada exitosamente", "id": nuevo_tarea.id}
        else:
            return {'error': 'El formato del archivo ingresado no es valido'}
