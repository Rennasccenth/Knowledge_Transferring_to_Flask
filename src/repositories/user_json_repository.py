import os
from abc import ABC, abstractmethod
from json import load
from typing import List

from src.models.user import User
from src.repositories.abstractions.user_repository import UserRepository

base_path = os.environ.get("DATABASE_PATH")
file_name = os.environ.get("DATABASE_FILENAME")


class UserJsonRepository(UserRepository):
    def __init__(self):
        # self.database_path = base_path + file_name
        # TODO: Tem que mudar esse banco de lugar, vai dar cagada ele ficar ali dentro desse
        #  aninhamento de diretórios... recomendo colocar no mesmo nível de src e test
        self.database_path = "./src/app/database/database.json"

    def get_by_id(self, identifier: int) -> User:
        with open(self.database_path, "r") as json_file:
            database: dict = load(json_file)

            for register in database["data"]:
                if register["id"] == id:
                    user = self._build_user(register)
                    return user

    def get_all(self) -> List[User]:
        with open(self.database_path, "r") as json_file:
            database: dict = load(json_file)
            users = list()
            for register in database["data"]:
                users.append(self._build_user(register))
            return users

    def store(self, user: User) -> bool:
        pass

    def update(self, user: User) -> bool:
        pass

    def remove(self, identifier: int) -> User:
        pass

    def _build_user(self, register: dict) -> User:
        """Private func to help while creating User objects from dict"""
        user = User(
            name=register["name"],
            email=register["email"]
        )
        user.id = register["id"]
        return user
