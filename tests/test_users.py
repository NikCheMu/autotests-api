from http import HTTPStatus

import pytest

from clients.users.private_users_client import PrivateUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response


@pytest.mark.users
@pytest.mark.regression
def test_create_user(public_users_client):
    request = CreateUserRequestSchema()
    response = public_users_client.create_user_api(request)
    response_data = CreateUserResponseSchema.model_validate_json(response.text)

    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_create_user_response(actual=response_data,expected=request)
    validate_json_schema(response.json(), CreateUserResponseSchema.model_json_schema())

@pytest.mark.users
@pytest.mark.regression
def test_get_user_me(function_user,private_users_client):
    response = private_users_client.get_user_me_api()
    response_data = GetUserResponseSchema.model_validate_json(response.text)
    assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
    assert_get_user_response(actual = response_data,expected=function_user.response)
    validate_json_schema(response.json(), GetUserResponseSchema.model_json_schema())