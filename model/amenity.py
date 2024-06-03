import uuid
from datetime import datetime


class Amenity:
    def __init__(self, name):
        self._id = str(uuid.uuid4())
        self._name = name
        self._created_at = datetime.now().timestamp()
        self._updated_at = self._created_at

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self._updated_at = datetime.now().timestamp()

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at
