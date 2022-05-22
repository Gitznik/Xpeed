from pymongo import MongoClient
from abc import ABC, abstractmethod
from typing import Dict


class DbInterface(ABC):
    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def get_user_data(self, user_ref):
        pass


class MongoInterface(DbInterface):
    def __init__(self, password: str):
        self.db = self._connect(password=password)

    def _connect(self, password: str):
        server_url = f"mongodb+srv://Rob:{password}@xpeedprod.2tlk5.mongodb.net/?retryWrites=true&w=majority"
        client = MongoClient(server_url)
        return client.Xpeed

    def get_user_data(self, user_ref: str) -> Dict:
        collection = self.db['Runs']
        return collection.find({"user_data": {"user_ref": user_ref}})


if __name__ == "__main__":
    # Example Usage
    interface = MongoInterface(password="FakePassword")
    user_data = interface.get_user_data(user_ref = "test_user")
    for run in user_data:
        print(run)
