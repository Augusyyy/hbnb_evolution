import uuid
from datetime import datetime


class Review:
    def __init__(self, commentor_user_id, place_id, feedback, rating):
        self.id = str(uuid.uuid4())
        self.__commentor_user_id = commentor_user_id
        self.__place_id = place_id
        self.__feedback = feedback
        self.__rating = rating
        self.created_at = datetime.now().timestamp()
        self.updated_at = self.created_at

    @property
    def commentor_user_id(self):
        return self.__commentor_user_id

    @commentor_user_id.setter
    def commentor_user_id(self, value):
        self.__commentor_user_id = value
        self.updated_at = datetime.now().timestamp()

    @property
    def place_id(self):
        return self.__place_id

    @place_id.setter
    def place_id(self, value):
        self.__place_id = value
        self.updated_at = datetime.now().timestamp()

    @property
    def feedback(self):
        return self.__feedback

    @feedback.setter
    def feedback(self, value):
        self.__feedback = value
        self.updated_at = datetime.now().timestamp()

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        self.__rating = value
        self.updated_at = datetime.now().timestamp()