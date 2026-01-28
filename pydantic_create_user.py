from pydantic import BaseModel, ConfigDict
from pydantic.alias_generators import to_camel

class BaseSchema(BaseModel):
    """
    Базовая модель с настройками для работы с camelCase
    """
    model_config = ConfigDict(alias_generator=to_camel, validate_by_name=True, validate_by_alias=True)
    def to_json(self) -> str:
        """
        Метод для создания json строки только с обязательными полями
        :return: json строку только с обязательными полями
        """
        return self.model_dump_json(by_alias= True,exclude_none=True)

class UserSchema(BaseSchema):
    """
    Обобщенная модель User
    """
    id: str | None = None
    email: str
    last_name: str
    first_name: str
    middle_name: str

class CreateUserRequestSchema(UserSchema):
    """
    Модель запроса на создание пользователя
    """
    password: str


class CreateUserResponseSchema(BaseSchema):
    """
    Модель ответа на запрос создания пользователя
    """
    user: UserSchema


request_payload = CreateUserRequestSchema(
    email="user@example",
    last_name="Mu",
    first_name="Nik",
    middle_name="Che",
    password= "123QWE"
)

response_payload = CreateUserResponseSchema(
    user= UserSchema(
        id = "userId1",
        email = "user@example",
        last_name="Mu",
        first_name="Nik",
        middle_name="Che",
    )
)
print("Request: ", request_payload.to_json())
print("Response: ", response_payload.to_json())


