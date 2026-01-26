from httpx import Response

from clients.api_client import APIClient

from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class GetExercisesQueryParamsDict(TypedDict):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    courseId:str

class CreateExerciseDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения.
    """
    title: str
    courseId: str
    maxScore: int
    minScore: int
    orderIndex: str
    description: str
    estimatedTime: str

class UpdateExerciseDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: str | None
    description: str | None
    estimatedTime: str | None

class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self,query:GetExercisesQueryParamsDict) -> Response:
        """
        Метод получения списка упражнений.

        :param query: Словарь с userId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises",params=query)

    def get_exercise_api(self,exercise_id:str) -> Response:
        """
        Метод получения упражнения.

        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self,request: CreateExerciseDict) -> Response:
        """
        Метод создания упражнения.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/exercises", json= request)

    def update_exercise_api(self,exercise_id:str, request:UpdateExerciseDict) -> Response:
        """
        Метод обновления упражнения.
        :param exercise_id: Идентификатор упражнения.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json= request)

    def delete_exercise_api(self, exercise_id:str) -> Response:
        """
        Метод удаления упражнения.

        :param exercise_id: Идентификатор курса.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

def get_exercises_client(user:AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(get_private_http_client(user=user))

