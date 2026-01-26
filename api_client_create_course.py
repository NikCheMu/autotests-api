from clients.courses.courses_client import get_courses_client, CreateCourseDict
from clients.files.files_client import get_files_client, UploadFileDict
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict
from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(email = get_random_email(), password = "123qwe", lastName="Mu", firstName="Nik", middleName="Che")

create_user_response = public_users_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserDict(email=create_user_request["email"], password=create_user_request["password"])

files_client = get_files_client(authentication_user)

course_client = get_courses_client(authentication_user)

create_file_request = UploadFileDict(filename='picture', directory= 'courses' ,upload_file='./test_data/files/image.jpeg')

create_file_response = files_client.upload_file(create_file_request)

print(create_file_response)

create_course_request = CreateCourseDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = course_client.create_course(create_course_request)
print(create_course_response)