from hashlib import new
from operator import eq
from flask import request,send_file
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from flask_restful import Resource
from sqlalchemy import desc,asc
from werkzeug.utils import secure_filename
import os,shutil
from pathlib import Path
from tareas import convertir_archivos

from modelos import db,Usuario, UsuarioSchema,Tarea,TareaSchema

usuario_schema = UsuarioSchema()
tarea_schema = TareaSchema()
formats = ['mp3','acc','ogg','wav','wma']

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
    @jwt_required
    def get(self, id):
        uid = get_jwt_identity()
        return [tarea_schema.dump(ca) for ca in Tarea.query.filter(Tarea.id_user==uid , Tarea.id==id).all()]

    @jwt_required
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

        dir = "uploads/"+str(tarea.id)+"/new/"
        if os.path.isdir(dir):
            shutil.rmtree(dir)
        convertir_archivos.apply_async(kwargs={'id':tarea.id}, countdown=60)
        return tarea_schema.dump(tarea)

    def delete(self, id):
        tarea = Tarea.query.get_or_404(id)
        db.session.delete(tarea)
        db.session.commit()
        return {'mensaje': 'Tarea Eliminada Correctamente'}

class VistaTareas(Resource):
    @jwt_required
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

    @jwt_required
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
            dir = "uploads/"+str(nuevo_tarea.id)+"/old/"
            path = Path(dir)
            path.mkdir(parents=True)
            file.save(os.path.join(dir, filename))
            convertir_archivos.apply_async(kwargs={'id':nuevo_tarea.id}, countdown=60)
            
            return {"mensaje": "Tarea creada exitosamente", "id": nuevo_tarea.id}
        else:
            return {'error': 'El formato del archivo ingresado no es valido'}
        
        
class VistaArchivos(Resource):
    @jwt_required
    def get(self,id,estado):
        uid = get_jwt_identity()
        tarea = Tarea.query.get_or_404(id)
        if estado == "convertido":
            file_name, file_extension = os.path.splitext(tarea.fileName)
            file_extension = file_extension.replace(".","")
            fileName = tarea.fileName.replace(file_extension,tarea.newFormat)
            dir = "uploads/"+str(id)+"/new/"+fileName
        else:
            dir = "uploads/"+str(id)+"/old/"+tarea.fileName
        
        if os.path.isfile(dir):
            return send_file(dir)
        else:
            return {"error": "Archivo No disponible"}
        
        
