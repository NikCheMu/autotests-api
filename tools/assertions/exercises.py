from clients.exercises.exercises_schema import CreateExerciseResponseSchema, CreateExerciseRequestSchema
from tools.assertions.base import assert_equal


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
