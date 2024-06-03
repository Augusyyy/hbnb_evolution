import uuid
from datetime import datetime


class Review:
    def __init__(self, commentor_user_id, place_id, feedback, rating):
        self._id = str(uuid.uuid4())
        self._commentor_user_id = commentor_user_id
        self._place_id = place_id
        self._feedback = feedback
        self._rating = rating
        self._created_at = datetime.now().timestamp()
        self._updated_at = self._created_at

    @property
    def id(self):
        return self._id

    @property
    def commentor_user_id(self):
        return self._commentor_user_id

    @commentor_user_id.setter
    def commentor_user_id(self, value):
        self._commentor_user_id = value
        self._updated_at = datetime.now().timestamp()

    @property
    def place_id(self):
        return self._place_id

    @place_id.setter
    def place_id(self, value):
        self._place_id = value
        self._updated_at = datetime.now().timestamp()

    @property
    def feedback(self):
        return self._feedback

    @feedback.setter
    def feedback(self, value):
        self._feedback = value
        self._updated_at = datetime.now().timestamp()

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, value):
        self._rating = value
        self._updated_at = datetime.now().timestamp()

    @property
    def created_at(self):
        return self._created_at

    @property
    def updated_at(self):
        return self._updated_at