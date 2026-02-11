from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema
from tools.assertions.base import assert_equal


def assert_create_user_response(actual: CreateUserResponseSchema, expected: CreateUserRequestSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param expected: Исходный запрос на создание пользователя.
    :param actual: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.user.email, expected.email, "email")
    assert_equal(actual.user.first_name, expected.first_name, "first_name")
    assert_equal(actual.user.last_name, expected.last_name, "last_name")
    assert_equal(actual.user.middle_name, expected.middle_name, "middle_name")