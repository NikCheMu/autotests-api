from http import HTTPStatus

import allure
import pytest

from clients.authentication.authentication_client import AuthenticationClient
from clients.authentication.authentication_schema import LoginRequestSchema, LoginResponseSchema
from fixtures.users import UserFixture
from tools.allure.epic import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.severity import Severity
from tools.allure.stories import AllureStory
from tools.allure.tags import AllureTag
from tools.assertions.authentication import assert_login_response
from tools.assertions.base import assert_status_code
from tools.assertions.schema import validate_json_schema

@pytest.mark.authentication
@pytest.mark.regression
@allure.tag(AllureTag.AUTHENTICATION,AllureTag.REGRESSION)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.AUTHENTICATION)
class TestAuthentication:
    @allure.story(AllureStory.LOGIN)
    @allure.title("Login with correct credentials")
    @allure.severity(Severity.BLOCKER)
    def test_login(self,authentication_client: AuthenticationClient, function_user: UserFixture):
        request = LoginRequestSchema(email=function_user.email, password=function_user.password)
        response = authentication_client.login_api(request)
        assert_status_code(response.status_code, HTTPStatus.OK)
        assert_login_response(LoginResponseSchema.model_validate_json(response.text))
        validate_json_schema(response.json(), LoginResponseSchema.model_json_schema())
