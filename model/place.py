import uuid
from datetime import datetime


class Place:
    def __init__(self, host_user_id, city_id, name, description, address, latitude, longitude, number_of_rooms,
                 bathrooms, price_per_night, max_guests):
        self._id = str(uuid.uuid4())
        self._host_user_id = host_user_id
        self._city_id = city_id
        self._name = name
        self._description = description
        self._address = address
        self._latitude = latitude
        self._longitude = longitude
        self._number_of_rooms = number_of_rooms
        self._bathrooms = bathrooms
        self._price_per_night = price_per_night
        self._max_guests = max_guests
        self._created_at = datetime.now().timestamp()
        self._updated_at = self._created_at

    @property
    def id(self):
        return self._id

    @property
    def host_user_id(self):
        return self._host_user_id

    @host_user_id.setter
    def host_user_id(self, value):
        self._host_user_id = value
        self._updated_at = datetime.now().timestamp()

    @property
    def city_id(self):
        return self._city_id

    @city_id.setter
    def city_id(self, value):
        self._city_id = value
        self._updated_at = datetime.now().timestamp()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._updated_at = datetime.now().timestamp()

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value
        self._updated_at = datetime.now().timestamp()

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value
        self._updated_at = datetime.now().timestamp()

    @property
    def latitude(self):
        return self._latitude

    @latitude.setter
    def latitude(self, value):
        self._latitude = value
        self._updated_at = datetime.now().timestamp()

    @property
    def longitude(self):
        return self._longitude

    @longitude.setter
    def longitude(self, value):
        self._longitude = value
        self._updated_at = datetime.now().timestamp()

    @property
    def number_of_rooms(self):
        return self._number_of_rooms

    @number_of_rooms.setter
    def number_of_rooms(self, value):
        self._number_of_rooms = value
        self._updated_at = datetime.now().timestamp()

    @property
    def bathrooms(self):
        return self._bathrooms

    @bathrooms.setter
    def bathrooms(self, value):
        self._bathrooms = value
        self._updated_at = datetime.now().timestamp()

    @property
    def price_per_night(self):
        return self._price_per_night

    @price_per_night.setter
    def price_per_night(self, value):
        self._price_per_night = value
        self._updated_at = datetime.now().timestamp()

    @property
    def max_guests(self):
        return self._max_guests

    @max_guests.setter
    def max_guests(self, value):
        self._max_guests = value
        self._updated_at = datetime.now().timestamp()

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
