import uuid
from datetime import datetime


class User:
    def __init__(self, email, password, first_name, last_name):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        self.__first_name = first_name
        self.__last_name = last_name
        self.__email = email
        self.__password = password

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value
        self.updated_at = datetime.now()

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value
        self.updated_at = datetime.now()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
        self.updated_at = datetime.now()

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
        self.updated_at = datetime.now()

