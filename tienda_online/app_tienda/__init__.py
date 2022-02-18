from flask import  Flask
from app_tienda import config
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

#todo creando la aplicacion
app=Flask(__name__)
cors=CORS(app)
app.secret_key = os.urandom(24)
app.config['CORS_HEADERS']='Content-Type'

#todo Conexion con la BD

app.config.from_object(config.Config)
db=SQLAlchemy(app)

from app_tienda import routers,models