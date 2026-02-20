from httpx import Client
from pydantic import BaseModel
from functools import lru_cache

from clients.authentication.authentication_client import get_authentication_client, LoginRequestSchema
from clients.event_hooks import curl_event_hook


class AuthenticationUserSchema(BaseModel, frozen = True):
    email: str
    password: str

@lru_cache()
def get_private_http_client(user:AuthenticationUserSchema) ->Client:
    """
    Функция создаёт экземпляр httpx.Client с авторизацией с базовыми настройками.

    :return: Готовый к использованию объект httpx.Client.
    """
    authentication_client = get_authentication_client()
    login_request = LoginRequestSchema(email=user.email,password=user.password)
    login_response = authentication_client.login(login_request)
    return Client(
        timeout=100,
        base_url="http://127.0.0.1:8000",
        headers={"Authorization": f"Bearer {login_response.token.access_token}"},
        event_hooks={"request": [curl_event_hook]}
    )