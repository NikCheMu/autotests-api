import allure

from clients.errors_schema import InternalErrorResponseSchema
from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema, \
    ExerciseSchema, GetExerciseResponseSchema, UpdateExerciseResponseSchema, UpdateExerciseRequestSchema, \
    GetExercisesResponseSchema
from tools.assertions.base import assert_equal, assert_length
from tools.assertions.errors import assert_internal_error_response

@allure.step("Check create exercise response")
def assert_create_exercise_response(actual: CreateExerciseResponseSchema, expected: CreateExerciseRequestSchema):
    """
     Проверяет, что фактические данные ответа на создание упражнения соответствуют ожидаемым.

     :param actual: Фактические данные упражнения.
     :param expected: Ожидаемые данные упражнения.
     :raises AssertionError: Если хотя бы одно поле не совпадает.
     """
    assert_equal(actual.exercise.title,expected.title, name="title")
    assert_equal(actual.exercise.max_score, expected.max_score, name="max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, name="min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, name="order_index")
    assert_equal(actual.exercise.description, expected.description, name="title")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, name="estimated_time")

@allure.step("Check exercise")
def assert_exercise(actual: ExerciseSchema, expected: ExerciseSchema):
    """
     Проверяет, что фактические данные упражнения соответствуют ожидаемым.

     :param actual: Фактические данные упражнения.
     :param expected: Ожидаемые данные упражнения.
     :raises AssertionError: Если хотя бы одно поле не совпадает.
     """
    assert_equal(actual.id, expected.id, name="id")
    assert_equal(actual.title, expected.title, name="title")
    assert_equal(actual.course_id, expected.course_id, name="course_id")
    assert_equal(actual.max_score, expected.max_score, name="max_score")
    assert_equal(actual.min_score, expected.min_score, name="min_score")
    assert_equal(actual.order_index, expected.order_index, name="order_index")
    assert_equal(actual.description, expected.description, name="description")
    assert_equal(actual.estimated_time, expected.estimated_time, name="estimated_time")

@allure.step("Check get exercise response")
def assert_get_exercise_response(actual: GetExerciseResponseSchema, expected: CreateExerciseResponseSchema):
    """
     Проверяет, что фактические данные ответа на получение упражнения соответствуют ожидаемым.

     :param actual: Фактические данные упражнения.
     :param expected: Ожидаемые данные упражнения.
     :raises AssertionError: Если хотя бы одно поле не совпадает.
     """
    assert_exercise(actual=actual.exercise, expected=expected.exercise)

@allure.step("Check update exercise response")
def assert_update_exercise_response(actual: UpdateExerciseResponseSchema, expected: UpdateExerciseRequestSchema):
    """
    Проверяет, что ответ на обновление задания соответствует данным из запроса.

    :param expected: Исходный запрос на обновление задания.
    :param actual: Ответ API с обновленными данными задания.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(actual.exercise.title, expected.title, name="title")
    assert_equal(actual.exercise.max_score, expected.max_score, name="max_score")
    assert_equal(actual.exercise.min_score, expected.min_score, name="min_score")
    assert_equal(actual.exercise.order_index, expected.order_index, name="order_index")
    assert_equal(actual.exercise.description, expected.description, name="description")
    assert_equal(actual.exercise.estimated_time, expected.estimated_time, name="estimated_time")

@allure.step("Check exercise not found response")
def assert_exercise_not_found_response(actual:InternalErrorResponseSchema):
    """
    Функция для проверки ошибки, если задание не найдено на сервере.

    :param actual: Фактический ответ.
    :raises AssertionError: Если фактический ответ не соответствует ошибке "Exercise not found"
    """
    expected = InternalErrorResponseSchema(details="Exercise not found")
    assert_internal_error_response(actual=actual, expected=expected)

@allure.step("Check get exercises response")
def assert_get_exercises_response(
        get_exercises_response: GetExercisesResponseSchema,
        create_exercises_response: list[CreateExerciseResponseSchema]):
    """
    Проверяет, что ответ на получение списка заданий соответствует ответам на их создание.

    :param get_exercises_response: Ответ API при запросе списка заданий.
    :param create_exercises_response: Список API ответов при создании заданий.
    :raises AssertionError: Если данные заданий не совпадают.
    """
    assert_length(get_exercises_response.exercises, create_exercises_response, name="exercises")

    for index, create_exercises_response in enumerate(create_exercises_response):
        assert_exercise(get_exercises_response.exercises[index], create_exercises_response.exercise)
