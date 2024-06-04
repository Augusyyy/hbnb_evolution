from flask import Flask
from flask_restx import Api

app = Flask(__name__)

api = Api(app, version='1.0', title='hbnb_evolution API', description='A hbnb_evolution project API')
user_api = api.namespace("Users", description='User operation')

from api.user_api import *

country_api = api.namespace('Countries', description='Country operations')

from api.country_api import *

cities_api = api.namespace('Cities', description='cities operations')

from api.cities_api import *

amenities_api = api.namespace('Amenity', description='inform about amenities')

from api.amenities_api import *

places_api = api.namespace('Places', description='inform about places')

from api.places_api import *

reviews_api = api.namespace('Reviews', description='the reviews operations')

from api.reviews_api import *