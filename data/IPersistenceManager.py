from abc import ABC, abstractmethod


class IPersistenceManager(ABC):

    @abstractmethod
    def save(self, entity):
        """add entity to persistence data,
            update memory data and update json file"""
        pass


    @abstractmethod
    def get(self, entity_id, entity_type):
        """get a entity from memory data"""
        pass


    @abstractmethod
    def update(self, entity):
        """update a entity
            update the memory data and update json file"""
        pass

    """"""
    @abstractmethod
    def delete(self, entity_id, entity_type):
        """delete entity from memory and delete from json file"""
        pass