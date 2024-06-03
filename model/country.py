import uuid
from datetime import datetime


class Country:
    def __init__(self, name, code):
        self.id = str(uuid.uuid4())
        self.__name = name
        self.__code = code
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.updated_at = datetime.now()

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        self.__code = value
        self.updated_at = datetime.now()