import uuid
from datetime import datetime


class Place:
    def __init__(self, host_user_id, city_id, name, description, address, latitude, longitude, number_of_rooms,
                 bathrooms, price_per_night, max_guests, amenity_ids):
        self.id = str(uuid.uuid4())
        self.__host_user_id = host_user_id
        self.__city_id = city_id
        self.__name = name
        self.__description = description
        self.__address = address
        self.__latitude = latitude
        self.__longitude = longitude
        self.__number_of_rooms = number_of_rooms
        self.__bathrooms = bathrooms
        self.__price_per_night = price_per_night
        self.__max_guests = max_guests
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at
        self.__amenity_ids = amenity_ids


    @property
    def host_user_id(self):
        return self.__host_user_id

    @host_user_id.setter
    def host_user_id(self, value):
        self.__host_user_id = value
        self.updated_at = datetime.now().timestamp()

    @property
    def city_id(self):
        return self.__city_id

    @city_id.setter
    def city_id(self, value):
        self.__city_id = value
        self.updated_at = datetime.now().timestamp()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.updated_at = datetime.now().timestamp()

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
        self.updated_at = datetime.now().timestamp()

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value
        self.updated_at = datetime.now().timestamp()

    @property
    def latitude(self):
        return self.__latitude

    @latitude.setter
    def latitude(self, value):
        self.__latitude = value
        self.updated_at = datetime.now().timestamp()

    @property
    def longitude(self):
        return self.__longitude

    @longitude.setter
    def longitude(self, value):
        self.__longitude = value
        self.updated_at = datetime.now().timestamp()

    @property
    def number_of_rooms(self):
        return self.__number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        self.__number_of_rooms = value
        self.updated_at = datetime.now().timestamp()

    @property
    def bathrooms(self):
        return self.__bathrooms

    @bathrooms.setter
    def bathrooms(self, value):
        self.__bathrooms = value
        self.updated_at = datetime.now().timestamp()

    @property
    def price_per_night(self):
        return self.__price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        self.__price_per_night = value
        self.updated_at = datetime.now().timestamp()

    @property
    def max_guests(self):
        return self.__max_guests

    @max_guests.setter
    def max_guests(self, value):
        self.__max_guests = value
        self.updated_at = datetime.now().timestamp()

    @property
    def amenity_ids(self):
        return self.__amenity_ids

    @max_guests.setter
    def amenity_ids(self, value):
        self.__amenity_ids = value
        self.updated_at = datetime.now().timestamp()
