from http import HTTPStatus

import allure
import pytest

from clients.users.public_users_client import PublicUsersClient
from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, GetUserResponseSchema
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.severity import Severity
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema
from tools.assertions.users import assert_create_user_response, assert_get_user_response
from tools.fakers import fake



@pytest.mark.users
@pytest.mark.regression
@allure.tag(AllureTag.USERS, AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.USERS)
class TestUsers:
    @pytest.mark.parametrize("domain", ["mail.ru", "gmail.com", "example.com"])
    @allure.tag(AllureTag.CREATE_ENTITY)
    @allure.story(AllureStory.CREATE_ENTITY)
    @allure.title("Create user")
    @allure.severity(Severity.BLOCKER)
    def test_create_user(self,public_users_client: PublicUsersClient, domain: str):
        request = CreateUserRequestSchema(email=fake.email(domain=domain))
        response = public_users_client.create_user_api(request)
        response_data = CreateUserResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_user_response(actual=response_data, expected=request)
        validate_json_schema(response.json(), CreateUserResponseSchema.model_json_schema())

    @allure.tag(AllureTag.GET_ENTITY)
    @allure.story(AllureStory.GET_ENTITY)
    @allure.title("Get user me")
    @allure.severity(Severity.CRITICAL)
    def test_get_user_me(self,function_user, private_users_client):
        response = private_users_client.get_user_me_api()
        response_data = GetUserResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_user_response(actual=response_data, expected=function_user.response)
        validate_json_schema(response.json(), GetUserResponseSchema.model_json_schema())