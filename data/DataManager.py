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


def save_data(filename, data):
    with open(filename, "w") as f:
        f.write(json.dumps(data, indent=4))


class DataManager(IPersistenceManager):

    def __init__(self):
        """init attribute in memory
        attribute is private"""
        self.__countries = {}
        self.__cities = {}
        self.__places = {}
        self.__amenity = {}
        self.__review = {}
        self.__user = {}

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
        delete_data = None
        if entity_type == EntityType.USER:
            for i in range(len(self.__user['User'])):
                if self.__user['User'][i]['id'] == entity_id:
                    delete_data = self.__user['User'][i]
                    self.__user['User'].pop(i)
                    break
            if delete_data is not None:
                save_data('data/user.json', self.__user)
                return delete_data
            else:
                return None

        elif entity_type == EntityType.CITY:
            for i in range(len(self.__cities['City'])):
                if self.__cities['City'][i]['id'] == entity_id:
                    delete_data = self.__cities['City'][i]
                    self.__cities['City'].pop(i)
                    break
            if delete_data is not None:
                save_data('data/city.json', self.__cities)
                return delete_data
            else:
                return None

        elif entity_type == EntityType.PLACE:
            for i in range(len(self.__places['Place'])):
                if self.__places['Place'][i]['id'] == entity_id:
                    delete_data = self.__places['Place'][i]
                    self.__places['Place'].pop(i)
                    break
            if delete_data is not None:
                save_data('data/place.json', self.__places)
                return delete_data
            else:
                return None

        elif entity_type == EntityType.REVIEW:
            for i in range(len(self.__review['Review'])):
                if self.__review['Review'][i]['id'] == entity_id:
                    delete_data = self.__review['Review'][i]
                    self.__review['Review'].pop(i)
                    break
            if delete_data is not None:
                save_data('data/review.json', self.__review)
                return delete_data
            else:
                return None

        elif entity_type == EntityType.AMENITY:
            for i in range(len(self.__amenity['Amenity'])):
                if self.__amenity['Amenity'][i]['id'] == entity_id:
                    delete_data = self.__amenity['Amenity'][i]
                    self.__amenity['Amenity'].pop(i)
                    break
            if delete_data is not None:
                save_data('data/amenity.json', self.__amenity)
                return delete_data
            else:
                return None
        elif entity_type == EntityType.CITY:
            for i in range(len(self.__cities['City'])):
                if self.__cities['City'][i]['id'] == entity_id:
                    delete_data = self.__cities['City'][i]
                    self.__cities['City'].pop(i)
                    break
            if delete_data is not None:
                save_data('data/city.json', self.__cities)
                return delete_data
            else:
                return None

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
            save_data('data/user.json', self.__user)
            return new_entity

        elif isinstance(entity, Review):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'user_id': entity.user_id,
                'place_id': entity.place_id,
                'comment': entity.comment,
                'rating': entity.rating
            }
            # add data to memory
            self.__review['Review'].append(new_entity)
            save_data('data/review.json', self.__review)
            return new_entity

        elif isinstance(entity, Place):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'host_user_id': entity.host_user_id,
                'name': entity.name,
                'description': entity.description,
                'address': entity.address,
                'latitude': entity.latitude,
                'longitude': entity.longitude,
                'number_of_rooms': entity.number_of_rooms,
                'bathrooms': entity.bathrooms,
                'price_per_night': entity.price_per_night,
                'max_guests': entity.max_guests,
                'amenity_ids': entity.amenity_ids,
                'city_id': entity.city_id
            }
            # add data to memory
            self.__places['Place'].append(new_entity)
            save_data('data/place.json', self.__places)
            return new_entity

        elif isinstance(entity, Amenity):
            new_entity = {
                'id': entity.id,
                'created_at': entity.created_at,
                'updated_at': entity.updated_at,
                'name': entity.name
            }
            # add data to memory
            self.__amenity['Amenity'].append(new_entity)
            save_data('data/amenity.json', self.__amenity)
            return new_entity

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
            self.__cities['City'].append(new_entity)
            save_data('data/city.json', self.__cities)
            return new_entity

        else:
            raise TypeError("Unsupported entity type")

    def update(self, entity):
        if isinstance(entity, User):
            for idx, user in enumerate(self.__user['User']):
                if user['id'] == entity.id:
                    updated_user = {
                        'id': entity.id,
                        'created_at': user['created_at'],
                        'updated_at': entity.updated_at,
                        'first_name': entity.first_name,
                        'last_name': entity.last_name,
                        'email': entity.email,
                        'password': entity.password
                    }
                    self.__user['User'][idx] = updated_user
                    save_data('data/user.json', self.__user)
                    return updated_user
            return None

        elif isinstance(entity, Review):
            for idx, review in enumerate(self.__review['Review']):
                if review['id'] == entity.id:
                    updated_review = {
                        'id': entity.id,
                        'created_at': review['created_at'],
                        'updated_at': entity.updated_at,
                        'user_id': entity.user_id,
                        'place_id': entity.place_id,
                        'comment': entity.comment,
                        'rating': entity.rating
                    }
                    self.__review['Review'][idx] = updated_review
                    save_data('data/review.json', self.__review)
                    return updated_review
            return None

        elif isinstance(entity, Place):
            for idx, place in enumerate(self.__places['Place']):
                if place['id'] == entity.id:
                    updated_place = {
                        'id': entity.id,
                        'created_at': place['created_at'],
                        'updated_at': entity.updated_at,
                        'host_user_id': entity.host_user_id,  # 补充字段
                        'name': entity.name,
                        'description': entity.description,
                        'address': entity.address,
                        'latitude': entity.latitude,
                        'longitude': entity.longitude,
                        'number_of_rooms': entity.number_of_rooms,
                        'bathrooms': entity.bathrooms,
                        'price_per_night': entity.price_per_night,
                        'max_guests': entity.max_guests,
                        'amenity_ids': entity.amenity_ids,
                        'city_id': entity.city_id
                    }
                    self.__places['Place'][idx] = updated_place
                    save_data('data/place.json', self.__places)
                    return updated_place
            return None

        elif isinstance(entity, Amenity):
            for idx, amenity in enumerate(self.__amenity['Amenity']):
                if amenity['id'] == entity.id:
                    updated_amenity = {
                        'id': entity.id,
                        'created_at': amenity['created_at'],
                        'updated_at': entity.updated_at,
                        'name': entity.name
                    }
                    self.__amenity['Amenity'][idx] = updated_amenity
                    save_data('data/amenity.json', self.__amenity)
                    return updated_amenity
            return None

        elif isinstance(entity, Country):
            for idx, country in enumerate(self.__countries['Country']):
                if country['id'] == entity.id:
                    updated_country = {
                        'id': entity.id,
                        'created_at': country['created_at'],
                        'updated_at': entity.updated_at,
                        'name': entity.name,
                        'code': entity.code
                    }
                    self.__countries['Country'][idx] = updated_country
                    save_data('data/country.json', self.__countries)
                    return updated_country
            return None

        elif isinstance(entity, City):
            for idx, city in enumerate(self.__cities['City']):
                if city['id'] == entity.id:
                    updated_city = {
                        'id': entity.id,
                        'created_at': city['created_at'],
                        'updated_at': entity.updated_at,
                        'country_id': entity.country_id,
                        'name': entity.name
                    }
                    self.__cities['City'][idx] = updated_city
                    save_data('data/city.json', self.__cities)
                    return updated_city
            return None

        else:
            raise TypeError("Unsupported entity type")

    def get(self, entity_id, entity_type):
        if entity_type == EntityType.USER:
            for user in self.__user['User']:
                if user['id'] == entity_id:
                    return user
            return None
        elif entity_type == EntityType.REVIEW:
            for review in self.__review['Review']:
                if review['id'] == entity_id:
                    return review
            return None
        elif entity_type == EntityType.PLACE:
            for place in self.__places['Place']:
                if place['id'] == entity_id:
                    return place
            return None
        elif entity_type == EntityType.AMENITY:
            for amenity in self.__amenity['Amenity']:
                if amenity['id'] == entity_id:
                    return amenity
            return None
        elif entity_type == EntityType.COUNTRY:
            for country in self.__countries['Country']:
                if country['id'] == entity_id:
                    return country
            return None
        elif entity_type == EntityType.CITY:
            for city in self.__cities['City']:
                if city['id'] == entity_id:
                    return city
            return None
        else:
            raise TypeError("Unsupported entity type")

    def get_list(self, entity_type):
        if entity_type == EntityType.COUNTRY:
            return self.__countries['Country']
        elif entity_type == EntityType.PLACE:
            return self.__places['Place']
        elif entity_type == EntityType.REVIEW:
            return self.__review['Review']
        elif entity_type == EntityType.USER:
            return self.__user['User']
        elif entity_type == EntityType.AMENITY:
            return self.__amenity['Amenity']
        elif entity_type == EntityType.CITY:
            return self.__cities['City']
        else:
            raise TypeError("Unsupported entity type")




