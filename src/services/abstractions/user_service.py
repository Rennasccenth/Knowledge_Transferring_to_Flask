from abc import ABC, abstractmethod
from typing import List

from src.models.user import User


# TODO: Mesma coisa que eu escrevi no UserRepository, isso é um contrato, só que no caso vamo usar
#  ele pra service e não pro repository
class UserService(ABC):

    @abstractmethod
    def get_by_id(self, id: int) -> User:
        """Get user by his identifier"""

    @abstractmethod
    def get_all(self) -> List[User]:
        """Get all users"""

    @abstractmethod
    def store(self, user: User) -> bool:
        """Store user"""

    @abstractmethod
    def update(self, user: User) -> bool:
        """Updates the user"""

    @abstractmethod
    def remove(self, identifier: int) -> User:
        """Remove the user"""
