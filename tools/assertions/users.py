import allure

from clients.users.users_schema import CreateUserResponseSchema, CreateUserRequestSchema, UserSchema, \
    GetUserResponseSchema
from tools.assertions.base import assert_equal

@allure.step("Check create user response")
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

@allure.step("Check user")
def assert_user(actual: UserSchema, expected: UserSchema):
    assert_equal(actual.email, expected.email, "email")
    assert_equal(actual.first_name, expected.first_name, "first_name")
    assert_equal(actual.last_name, expected.last_name, "last_name")
    assert_equal(actual.middle_name, expected.middle_name, "middle_name")
    assert_equal(actual.id, expected.id, "id")

@allure.step("Check get user response")
def assert_get_user_response(actual: GetUserResponseSchema, expected: CreateUserResponseSchema):
    assert_user(actual=actual.user, expected=expected.user)