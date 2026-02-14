import pytest

from clients.private_http_builder import AuthenticationUserSchema
from clients.users.private_users_client import get_private_users_client, PrivateUsersClient
from clients.users.public_users_client import PublicUsersClient, get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema

from pydantic import BaseModel, EmailStr


class UserFixture(BaseModel):
    """
    Модель объекта, возвращаемого из фикстуры для создания пользователя
    """
    request: CreateUserRequestSchema
    response: CreateUserResponseSchema

    @property
    def email(self) -> EmailStr:
        return self.request.email

    @property
    def password(self) -> str:
        return self.request.password

    @property
    def authentication_user(self):
        return AuthenticationUserSchema(
            email=self.email,
            password=self.password
        )

@pytest.fixture
def public_users_client() -> PublicUsersClient:
    """
    Фикстура, возвращающая PublicUsersClient
    :return: PublicUsersClient
    """
    return get_public_users_client()

@pytest.fixture
def function_user(public_users_client: PublicUsersClient) -> UserFixture:
    """
    Фикстура для создания тестового пользователя
    :param public_users_client: Фикстура, возвращающая PublicUsersClient
    :return: Объект UserFixture
    """
    request = CreateUserRequestSchema()
    response = public_users_client.create_user(request)
    return UserFixture(request=request,response=response)

@pytest.fixture
def private_users_client(function_user) -> PrivateUsersClient:
    """
    Фикстура, возвращающая PrivateUsersClient
    :return: PrivateUsersClient
    """
    return get_private_users_client(function_user.authentication_user)