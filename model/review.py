import uuid
from datetime import datetime


class Review:
    def __init__(self, user_id, place_id, comment, rating):
        self.id = str(uuid.uuid4())
        self.__user_id = user_id
        self.__place_id = place_id
        self.__comment = comment
        self.__rating = rating
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value
        self.updated_at = datetime.now().timestamp()

    @property
    def place_id(self):
        return self.__place_id

    @place_id.setter
    def place_id(self, value):
        self.__place_id = value
        self.updated_at = datetime.now().timestamp()

    @property
    def comment(self):
        return self.__comment

    @comment.setter
    def comment(self, value):
        self.__comment = value
        self.updated_at = datetime.now().timestamp()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value
        self.updated_at = datetime.now().timestamp()