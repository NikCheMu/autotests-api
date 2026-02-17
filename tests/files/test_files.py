from http import HTTPStatus

import pytest

from clients.errors_schema import ValidationErrorResponseSchema, InternalErrorResponseSchema
from clients.files.files_client import FilesClient
from clients.files.files_schema import UploadFileRequestSchema, UploadFileResponseSchema, GetFileResponseSchema
from fixtures.files import FileFixture
from tools.assertions.base import assert_status_code
from tools.assertions.files import assert_create_file_response, assert_get_file_response, \
    assert_create_file_with_empty_filename_response, assert_create_file_with_empty_directory_response, \
    assert_file_not_found_response
from tools.assertions.schema import validate_json_schema



@pytest.mark.file
@pytest.mark.regression
class TestFiles:
    def test_create_file(self,files_client: FilesClient):
        request = UploadFileRequestSchema(upload_file="test_data/files/image.jpeg")
        response = files_client.upload_file_api(request=request)
        response_data = UploadFileResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_create_file_response(request=request, response=response_data)

        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())


    def test_get_file(self,files_client: FilesClient, function_file: FileFixture):
        response = files_client.get_file_api(function_file.response.file.id)
        response_data = GetFileResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.OK)
        assert_get_file_response(response_data, function_file.response)
        validate_json_schema(instance=response.json(), schema=response_data.model_json_schema())

    @pytest.mark.negative
    def test_create_file_with_empty_filename(self,files_client: FilesClient):
        request = UploadFileRequestSchema(upload_file="test_data/files/image.jpeg",filename="")
        response = files_client.upload_file_api(request=request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_filename_response(actual=response_data)

    @pytest.mark.negative
    def test_create_file_with_empty_directory(self,files_client: FilesClient):
        request = UploadFileRequestSchema(upload_file="test_data/files/image.jpeg", directory="")
        response = files_client.upload_file_api(request=request)
        response_data = ValidationErrorResponseSchema.model_validate_json(response.text)
        assert_status_code(actual=response.status_code, expected=HTTPStatus.UNPROCESSABLE_ENTITY)
        assert_create_file_with_empty_directory_response(actual=response_data)

    @pytest.mark.negative
    def test_delete_file(self,files_client: FilesClient, function_file: FileFixture):
        delete_response = files_client.delete_file_api(function_file.response.file.id)
        assert_status_code(actual=delete_response.status_code, expected=HTTPStatus.OK)

        get_response = files_client.get_file_api(function_file.response.file.id)
        get_response_data = InternalErrorResponseSchema.model_validate_json(get_response.text)
        assert_status_code(actual=get_response.status_code, expected=HTTPStatus.NOT_FOUND)
        assert_file_not_found_response(get_response_data)
        validate_json_schema(instance=get_response.json(), schema=get_response_data.model_json_schema())



