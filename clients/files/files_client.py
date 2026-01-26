from httpx import Response

from clients.api_client import APIClient

from typing import TypedDict

from clients.private_http_builder import AuthenticationUserDict, get_private_http_client


class UploadFileDict(TypedDict):
    """
    Описание структуры запроса на создание файла.
    """
    filename:str
    directory:str
    upload_file: str

class File(TypedDict):
    id: str
    filename: str
    directory: str
    url: str

class UploadFileResponseDict(TypedDict):
    file: File


class FilesClient(APIClient):
    """
    Клиент для работы с /api/v1/files
    """
    def get_file_api(self,file_id:str) -> Response:
        """
        Метод получения файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def delete_file_api(self,file_id:str) -> Response:
        """
        Метод удаления файла.

        :param file_id: Идентификатор файла.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/files/{file_id}")

    def upload_file_api(self, request:UploadFileDict ) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/files",data=request,files={"upload_file": open(request['upload_file'], "rb")})

    def upload_file(self, request: UploadFileDict ) -> UploadFileResponseDict:
        return self.upload_file_api(request= request).json()

def get_files_client(user:AuthenticationUserDict) -> FilesClient:
    return FilesClient(get_private_http_client(user=user))