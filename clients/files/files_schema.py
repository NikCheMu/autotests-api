from pydantic import BaseModel, HttpUrl, Field

from tools.fakers import fake


class UploadFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename:str = Field(default_factory= lambda: f"{fake.uuid4()}.png")
    directory:str = Field(default="tests")
    upload_file: str

class FileSchema(BaseModel):
    """
    Описание структуры файла.
    """
    id: str
    filename: str
    directory: str
    url: HttpUrl

class UploadFileResponseSchema(BaseModel):
    """
    Описание структуры ответа на запрос на создание файла.
    """
    file: FileSchema

class GetFileResponseSchema(BaseModel):
    """
    Описание структуры запроса получения файла.
    """
    file: FileSchema