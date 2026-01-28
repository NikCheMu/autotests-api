from clients.courses.courses_client import get_courses_client, CreateCourseDict
from clients.files.files_client import get_files_client
from clients.files.files_schema import UploadFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(email = get_random_email(), password = "123qwe", last_name="Mu", first_name="Nik", middle_name="Che")

create_user_response = public_users_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserSchema(email=create_user_request.email, password=create_user_request.password)

files_client = get_files_client(authentication_user)

course_client = get_courses_client(authentication_user)

create_file_request = UploadFileRequestSchema(filename='picture', directory= 'courses' ,upload_file='./test_data/files/image.jpeg')

create_file_response = files_client.upload_file(create_file_request)

print(create_file_response)

create_course_request = CreateCourseDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response.file.id,
    createdByUserId=create_user_response.user.id
)

create_course_response = course_client.create_course(create_course_request)
print(create_course_response)