import pytest

from clients.authentication.authentication_client import get_authentication_client, AuthenticationClient


@pytest.fixture
def authentication_client() -> AuthenticationClient:
    """
    Фикстура, возвращающая AuthenticationClient
    :return: AuthenticationClient
    """
    return get_authentication_client()

