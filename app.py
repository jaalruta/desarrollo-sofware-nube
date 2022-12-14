from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from modelos import db
from vistas import VistaSignIn, VistaLogIn, VistaTareas, VistaTarea, VistaArchivos, VistaTest

UPLOAD_FOLDER = '/uploads'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/conversor'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'frase-secreta'
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

cors = CORS(app)

api = Api(app)
api.add_resource(VistaSignIn, '/signup')
api.add_resource(VistaLogIn, '/login')
api.add_resource(VistaTareas, '/tasks')
api.add_resource(VistaTarea, '/tasks/<int:id>')
api.add_resource(VistaArchivos, '/files/<int:id>/<string:estado>')
api.add_resource(VistaTest, '/test')

jwt = JWTManager(app)

        



