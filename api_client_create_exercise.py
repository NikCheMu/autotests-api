from clients.courses.courses_client import get_courses_client
from clients.courses.courses_schema import CreateCourseRequestSchema
from clients.exercises.exercises_client import get_exercises_client
from clients.exercises.exercises_schema import CreateExerciseRequestSchema
from clients.files.files_client import get_files_client
from clients.files.files_schema import UploadFileRequestSchema
from clients.private_http_builder import AuthenticationUserSchema
from clients.users.public_users_client import get_public_users_client
from clients.users.users_schema import CreateUserRequestSchema
from tools.fakers import fake

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestSchema(
    email = fake.email(),
    password = "123qwe",
    last_name="Mu",
    first_name="Nik",
    middle_name="Che"
)

create_user_response = public_users_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserSchema(
    email=create_user_request.email,
    password=create_user_request.password
)

files_client = get_files_client(authentication_user)

course_client = get_courses_client(authentication_user)

create_file_request = UploadFileRequestSchema(
    filename='picture',
    directory= 'courses',
    upload_file='./test_data/files/image.jpeg'
)

create_file_response = files_client.upload_file(create_file_request)
print("Create file data: ", create_file_response)

create_course_request = CreateCourseRequestSchema(
    title="Python",
    max_score=100,
    min_score=10,
    description="Python API course",
    estimated_time="2 weeks",
    preview_file_id=create_file_response.file.id,
    created_by_user_id=create_user_response.user.id
)

create_course_response = course_client.create_course(create_course_request)
print("Create course data: ", create_course_response)

exercises_client = get_exercises_client(authentication_user)

create_exercise_request = CreateExerciseRequestSchema(
    title =  'Python exercise',
    course_id = create_course_response.course.id,
    max_score = 100,
    min_score = 60,
    order_index =  1,
    description = 'Exercise 1',
    estimated_time = '5 minutes',
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)
print("Create exercise data: ", create_exercise_response)