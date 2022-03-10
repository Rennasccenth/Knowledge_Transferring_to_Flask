from typing import List

from src.models.user import User
from src.repositories.user_json_repository import UserRepository, UserJsonRepository
from src.services.abstractions.user_service import UserService


class UserServiceImpl(UserService):
    # TODO: Procurar sobre Dependency injection no python pra desacoplar isso. A idéia é nunca usar
    #  a implementação em si [UserJsonRepository] como nesse caso e sim usarmos a abstração disso,
    #  no caso a classe [UserRepository]. Como por exemplo:
    #  _user_repository = UserRepository()
    _user_repository = UserJsonRepository()

    def get_by_id(self, id: int) -> User:
        return self._user_repository.get_by_id(id)

    def get_all(self) -> List[User]:
        return self._user_repository.get_all()

    def store(self, user: User) -> bool:
        pass

    def update(self, user: User) -> bool:
        pass

    def remove(self, identifier: int) -> User:
        pass
