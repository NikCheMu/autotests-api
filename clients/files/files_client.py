from httpx import Response

from clients.api_client import APIClient
from clients.files.files_schema import UploadFileRequestSchema, UploadFileResponseSchema

from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema



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

    def upload_file_api(self, request:UploadFileRequestSchema) -> Response:
        """
        Метод создания файла.

        :param request: Словарь с filename, directory, upload_file.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.post("/api/v1/files",data=request.model_dump(by_alias=True,exclude={'upload_file'}),files={"upload_file": open(request.upload_file, "rb")})

    def upload_file(self, request: UploadFileRequestSchema) -> UploadFileResponseSchema:
        response = self.upload_file_api(request= request)
        return UploadFileResponseSchema.model_validate_json(response.text)

def get_files_client(user:AuthenticationUserSchema) -> FilesClient:
    return FilesClient(get_private_http_client(user=user))