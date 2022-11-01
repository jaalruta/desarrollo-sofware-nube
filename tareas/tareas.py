from celery import Celery
import sqlalchemy as db
import os
from pydub import AudioSegment
from pathlib import Path
import smtplib, ssl
import certifi

celery_app =Celery(__name__,broker='redis://localhost:6379/0')
celery_app.conf.enable_utc = False

@celery_app.task()
def convertir_archivos (id):
    engine = db.create_engine('postgresql://postgres:postgres@35.232.161.92:5432/conversor')
    fileNameOrig =""
    newFormat = ""
    email = ""
    with engine.connect() as connection:

        metadata = db.MetaData()
        tarea = db.Table('tarea', metadata, autoload=True, autoload_with=engine)
        stmt = tarea.select().where(tarea.c.id==id)
        datos_tarea = connection.execute(stmt)
        row = datos_tarea.fetchone()
        fileNameOrig = row._mapping["fileName"]
        newFormat = row._mapping["newFormat"]
        id_user = row._mapping["id_user"]
         
        usuario = db.Table('usuario', metadata, autoload=True, autoload_with=engine)
        stmt = usuario.select().where(usuario.c.id==id_user)
        datos_usuario = connection.execute(stmt)
        row_usua = datos_usuario.fetchone()
        email = row_usua._mapping["email"]

        file_name, file_extension = os.path.splitext(fileNameOrig)
        file_extension = file_extension.replace(".","")
        old_dir = "/nfs/uploads/"+str(id)+"/old/"   
        new_dir = "/nfs/uploads/"+str(id)+"/new/" 
        new_file = new_dir+file_name+"."+newFormat
        path = Path(new_dir)
        path.mkdir(parents=True)
        file = old_dir+fileNameOrig  
        if os.path.isfile(file):   

            original = AudioSegment.from_file(file, format="mp3")
            original.export(new_file, format=newFormat)
        
        stmt = tarea.update().values(status = 'processed').where(tarea.c.id==id)
        connection.execute(stmt)

        context = ssl.create_default_context(cafile=certifi.where())
        port = 465
        sender_email = "conversormiso26@gmail.com"
        receiver_email = email
        message = 'Subject: {}\n\n{}'.format("Notificacion de conversion finalizada", "Buen dia , se ha finalizado la conversion del archivo "+file_name+" con identificador "+str(id)+".")

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("conversormiso26@gmail.com", "yjqeitpyneftgkpa")
            server.sendmail(sender_email, receiver_email, message)
            server.quit()
