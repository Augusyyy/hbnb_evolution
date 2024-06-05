import datetime
import json
from enum import Enum

from model.amenity import Amenity
from model.city import City
from data.IPersistenceManager import IPersistenceManager
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


    def update(self, entity):
        pass

    def get(self, entity_id, entity_type):
        pass

    def save(self, entity):
        pass

    def __init__(self, json_file):
        self.json_file = json_file
        self.memory_data = self._load_from_file()


