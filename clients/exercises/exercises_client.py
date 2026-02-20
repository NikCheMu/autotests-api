import allure
from httpx import Response

from clients.api_client import APIClient
from clients.exercises.exercises_schema import GetExercisesQueryParamsSchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema, \
    GetExerciseResponseSchema
from clients.private_http_builder import AuthenticationUserSchema, get_private_http_client


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get all exercises")
    def get_exercises_api(self,query:GetExercisesQueryParamsSchema) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises",params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by Id {exercise_id}")
    def get_exercise_api(self,exercise_id:str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    @allure.step("Create exercise")
    def create_exercise_api(self,request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания упражнения.

        :param request: модель CreateExerciseRequestSchema
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json= request.model_dump(by_alias=True))

    @allure.step("Update exercise with Id {exercise_id}")
    def update_exercise_api(self,exercise_id:str, request:UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: модель UpdateExerciseRequestSchema
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json= request.model_dump(by_alias=True))

    @allure.step("Delete exercise with Id {exercise_id}")
    def delete_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор упражнения.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

    def get_exercises(self,query:GetExercisesQueryParamsSchema) -> GetExercisesResponseSchema:
        """
        Метод получения списка упражнений для курса
        :param query: Идентификатор курса courseId.
        :return: список упражнений GetExercisesResponseSchema
        """
        response = self.get_exercises_api(query=query)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def get_exercise(self, exercise_id: str) -> GetExerciseResponseSchema:
        """
        Метод получения упражнения по id курса
        :param exercise_id: идентификатор упражнения
        :return: упражнение GetExerciseResponseSchema
        """
        response = self.get_exercise_api(exercise_id=exercise_id)
        return GetExerciseResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        """
        Метод создания упражнения
        :param request: CreateExerciseRequestSchema
        :return: созданное упражнение CreateExerciseResponseSchema
        """
        response = self.create_exercise_api(request=request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self,exercise_id:str, request:UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        """
        Метод (частичного) обновления упражнения по id
        :param exercise_id: идентификатор упражнение
        :param request: UpdateExerciseRequestSchema
        :return: UpdateExerciseResponseSchema
        """
        response = self.update_exercise_api(exercise_id=exercise_id, request= request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


def get_exercises_client(user:AuthenticationUserSchema) -> ExercisesClient:
    """
    Билдер для ExercisesClient
    :param user: Объект с логином и паролем пользователя
    :return: Экземпляр ExercisesClient
    """
    return ExercisesClient(get_private_http_client(user=user))

