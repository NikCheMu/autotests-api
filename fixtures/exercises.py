import pytest
from pydantic import BaseModel

from clients.exercises.exercises_client import get_exercises_client, ExercisesClient
from clients.exercises.exercises_schema import CreateExerciseRequestSchema, CreateExerciseResponseSchema
from fixtures.course import CourseFixture
from fixtures.users import UserFixture

class ExerciseFixture(BaseModel):
    """
    Модель объекта, возвращаемого из фикстуры для создания упражнения
    """
    request: CreateExerciseRequestSchema
    response: CreateExerciseResponseSchema


@pytest.fixture
def exercises_client(function_user: UserFixture) -> ExercisesClient:
    """
    Фикстура, возвращающая экземпляр ExercisesClient
    :param function_user:
    :return: ExercisesClient
    """
    return get_exercises_client(function_user.authentication_user)

@pytest.fixture
def function_exercise(function_course: CourseFixture, exercises_client: ExercisesClient) -> ExerciseFixture:
    """
    Фикстура для создания упражнения
    :param function_course: Результат работы фикстуры для создания курса
    :param exercises_client: экземпляр ExercisesClient
    :return: экземпляр ExerciseFixture
    """
    request = CreateExerciseRequestSchema(course_id= function_course.response.course.id)
    response = exercises_client.create_exercise(request)
    return ExerciseFixture(request=request, response=response)
