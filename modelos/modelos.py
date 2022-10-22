from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.sql import func

db = SQLAlchemy()

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    email  = db.Column(db.String(50))
    password  = db.Column(db.String(50))

class Tarea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_user = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    fileName = db.Column(db.String(200))
    newFormat = db.Column(db.String(200))
    status = db.Column(db.String(50))
    timeStamp = db.Column(db.DateTime,default=func.now())



class UsuarioSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Usuario
        include_relationships = True
        load_instance = True

class TareaSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Tarea
        include_relationships = True
        load_instance = True


