from pydantic import BaseModel, HttpUrl


class UploadFileRequestSchema(BaseModel):
    """
    Описание структуры запроса на создание файла.
    """
    filename:str
    directory:str
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