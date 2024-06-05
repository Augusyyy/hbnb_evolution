import datetime
import json
from enum import Enum

from model.amenity import Amenity
from model.city import City
from data.IPersistenceManager import IPersistenceManager
from model.country import Country
from model.place import Place
from model.review import Review
from model.user import User
from datetime import datetime


class EntityType(Enum):
    COUNTRY = "country"
    PLACE = "place"
    REVIEW = "review"
    USER = "user"
    AMENITY = "amenity"
    CITY = "city"


class DataManager(IPersistenceManager):

    def __init__(self):
        """init attribute in memory
        attribute is private"""
        self.__user = {}
        self.__countries = {}
        self.__cities = {}
        self.__places = {}
        self.__amenity = {}
        self.__review = {}

        """from json file load data 
                save in attribute"""
        filename = 'data/' + EntityType.USER.value + '.json'
        with open(filename, "r") as f:
            self.__user = json.loads(f.read())

        filename = 'data/' + EntityType.COUNTRY.value + '.json'
        with open(filename, "r") as f:
            self.__countries = json.loads(f.read())

        filename = 'data/' + EntityType.CITY.value + '.json'
        with open(filename, "r") as f:
            self.__cities = json.loads(f.read())

        filename = 'data/' + EntityType.PLACE.value + '.json'
        with open(filename, "r") as f:
            self.__places = json.loads(f.read())

        filename = 'data/' + EntityType.AMENITY.value + '.json'
        with open(filename, "r") as f:
            self.__amenity = json.loads(f.read())

        filename = 'data/' + EntityType.REVIEW.value + '.json'
        with open(filename, "r") as f:
            self.__review = json.loads(f.read())

    def delete(self, entity_id, entity_type):
        filename = 'data/' + entity_type.value + '.json'
        try:
            with open(filename, "r") as f:
                if entity_type == EntityType.USER:
                    self.__user = json.loads(f.read())
        except FileNotFoundError:
            if entity_type == EntityType.USER:
                self.__user = {}

    def save(self, entity):
        if isinstance(entity, User):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'first_name': entity.first_name,
                'last_name': entity.last_name,
                'email': entity.email,
                'password': entity.password
            }
            # add data to memory
            self.__user['User'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.USER.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__user, indent=4))

        elif isinstance(entity, Review):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'commentor_user_id': entity.commentor_user_id,
                'place_id': entity.place_id,
                'feedback': entity.feedback,
                'rating': entity.rating
            }
            # add data to memory
            self.__review['Review'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.REVIEW.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__review, indent=4))   #4个缩进

        elif isinstance(entity, Place):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'name': entity.name,
                'description': entity.description,
                'address': entity.address,
                'latitude': entity.latitude,
                'longitude': entity.longitude,
                'number_of_rooms': entity.number_of_rooms,
                'bathrooms': entity.bathrooms,
                'price_per_night': entity.price_per_night,
                'max_guests': entity.max_guests
            }
            # add data to memory
            self.__places['Place'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.PLACE.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__places, indent=4))

        elif isinstance(entity, Amenity):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'name': entity.name
            }
            # add data to memory
            self.__amenity['Amenity'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.AMENITY.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__amenity, indent=4))

        elif isinstance(entity, Country):
            pass

        elif isinstance(entity, City):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'country_id': entity.country_id,
                'name': entity.name
            }
            # add data to memory
            self.__cities['Cities'].append(new_entity)
            # flush json file
            filename = 'data/' + EntityType.CITY.value + '.json'
            with open(filename, "w") as f:
                f.write(json.dumps(self.__cities, indent=4))

        else:
            raise TypeError("Unsupported entity type")
        
    def update(self, entity):
        pass

    def get(self, entity_id, entity_type):
        pass




