import uuid
from datetime import datetime


class Amenity:
    def __init__(self, name):
        self.id = str(uuid.uuid4())
        self.__name = name
        self.created_at = datetime.now()
        self.updated_at = self.created_at


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.updated_at = datetime.now()