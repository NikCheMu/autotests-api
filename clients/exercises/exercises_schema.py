from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class GetExercisesQueryParamsSchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    course_id:str = Field(alias="courseId")

class CreateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание упражнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class UpdateExerciseRequestSchema(BaseModel):
    """
    Описание структуры запроса на обновление упражнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    title: Optional[str] = None
    maxScore: Optional[int] = Field(alias="maxScore", default=None)
    minScore: Optional[int] = Field(alias="minScore", default=None)
    orderIndex: Optional[str] = Field(alias="orderIndex", default=None)
    description: Optional[str] = None
    estimatedTime: Optional[str] = Field(alias="estimatedTime",default=None)

class ExerciseSchema(BaseModel):
    """
    Описание структуры упражнения.
    """
    model_config = ConfigDict(validate_by_name=True, validate_by_alias=True)

    id: str
    title: str
    course_id: str = Field(alias="courseId")
    max_score: int = Field(alias="maxScore")
    min_score: int = Field(alias="minScore")
    order_index: int = Field(alias="orderIndex")
    description: str
    estimated_time: str = Field(alias="estimatedTime")

class GetExercisesResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение списка упражнений.
    """
    exercises: list[ExerciseSchema]

class GetExerciseResponseSchema(BaseModel):
    """
    Описание структуры запроса на получение упражнения.
    """
    exercise: ExerciseSchema


class CreateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос создания упражнения.
    """
    exercise: ExerciseSchema


class UpdateExerciseResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос обновления упражнения.
    """
    exercise: ExerciseSchema