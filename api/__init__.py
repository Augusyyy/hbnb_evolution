from flask import Flask
from flask_restx import Api

from data.DataManager import DataManager

app = Flask(__name__)

data_manager = DataManager()

api = Api(app, version='1.0', title='hbnb_evolution API', description='A hbnb_evolution project API')
user_api = api.namespace("users", description='User operation')

from api.user_api import *

country_api = api.namespace('countries', description='Country operations')

from api.country_api import *

cities_api = api.namespace('cities', description='cities operations')

from .cities_api import *

amenities_api = api.namespace('amenity', description='inform about amenities')

from api.amenities_api import *

places_api = api.namespace('places', description='inform about places')

from api.places_api import *

reviews_api = api.namespace('reviews', description='the reviews operations')

from api.reviews_api import *