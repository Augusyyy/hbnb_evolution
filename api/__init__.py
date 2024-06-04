from flask import Flask
from flask_restx import Api

app = Flask(__name__)

api = Api(app, version='1.0', title='hbnb_evolution API', description='A hbnb_evolution project API')
user_api = api.namespace("users", description='User operation')

from api.user_api import *
