from abc import ABC, abstractmethod
from typing import List

from src.models.user import User


# TODO: Isso aqui funciona como uma interface, no caso eu tô definindo um contrato de modo que
#  qualquer implementação de UserRepository irá ter que implementar esses métodos... Isso é usado
#  pra Dependency INVERSION [A letra D do SOLID] e posteriormente se usa pra Dependency INJECTION...
class UserRepository(ABC):
    @abstractmethod
    def get_by_id(self, identifier: int) -> User:
        """Get user by his identifier"""

    @abstractmethod
    def get_all(self) -> List[User]:
        """Get all users stored"""

    @abstractmethod
    def store(self, user: User) -> bool:
        """Store user on repository"""

    @abstractmethod
    def update(self, user: User) -> bool:
        """Updates the user on repository"""

    @abstractmethod
    def remove(self, identifier: int) -> User:
        """Remove the user stored on repository"""
