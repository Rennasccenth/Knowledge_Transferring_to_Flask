from unittest.mock import patch

from src.models.user import User
from src.services.user_service_impl import UserService, UserServiceImpl


# Nome do que eu vou testar _ Contexto em que eu vou estar _ Resultado esperado
def test_get_user_by_id_when_user_exists_should_return_the_user():
    # Arrange and act
    id_needed = 10
    user_mock = User(
        name="Victor Nunes",
        email="VictorNunes@gmail.com"
    )
    user_mock.id = id_needed
    user_service = UserServiceImpl()

    # Mocking UserRepository.get_by_id response
    with patch('src.repositories.user_json_repository.UserJsonRepository',
               return_value=user_mock):
        user_found = user_service.get_by_id(id=id_needed)

    # Assert
    assert user_found.id == id_needed
    assert isinstance(user_found, User)


def test_get_user_by_id_when_user_doesnt_exists_should_return_none():
    # Arrange
    id_needed = -1
    user_service = UserService()

    # Act
    user_found = user_service.get_by_id(id=id_needed)

    # Assert
    assert user_found is None
