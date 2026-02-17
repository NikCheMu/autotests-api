from http import HTTPStatus

import pytest

from clients.courses.courses_client import CoursesClient
from clients.courses.courses_schema import UpdateCourseRequestSchema, UpdateCourseResponseSchema, \
    GetCoursesQuerySchema, GetCoursesResponseSchema
from fixtures.course import CourseFixture
from fixtures.users import UserFixture
from tools.assertions.base import assert_status_code
from tools.assertions.courses import assert_update_course_response, assert_get_courses_response
from tools.assertions.schema import validate_json_schema


@pytest.mark.courses
@pytest.mark.regression
class TestCourses:
    def test_update_course(self, courses_client: CoursesClient , function_course: CourseFixture):
        request = UpdateCourseRequestSchema()
        response = courses_client.update_course_api(function_course.response.course.id, request=request)
        response_data = UpdateCourseResponseSchema.model_validate_json(response.text)

        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_update_course_response(request=request, response=response_data)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    def test_get_courses(self, courses_client: CoursesClient , function_course: CourseFixture, function_user: UserFixture):
        query = GetCoursesQuerySchema(user_id=function_user.response.user.id)
        response = courses_client.get_courses_api(query=query)
        response_data = GetCoursesResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_courses_response(response_data,[function_course.response])
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

