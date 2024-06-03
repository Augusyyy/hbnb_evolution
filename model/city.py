import uuid
from datetime import datetime


class City:
    def __init__(self,__name,__country_id):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().timestamp()
        self.updated_at = datetime.now().timestamp()
        self.__name = __name
        self.__country_id = __country_id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property
    def country_id(self):
        return self.__country_id

    @country_id.setter
    def country_id(self,country_id):
        self.__country_id = country_id


