from clients.private_http_builder import AuthenticationUserDict
from clients.users.private_users_client import get_private_users_client
from clients.users.public_users_client import get_public_users_client, CreateUserRequestDict

from tools.fakers import get_random_email

public_users_client = get_public_users_client()

create_user_request = CreateUserRequestDict(email = get_random_email(), password = "123qwe", lastName="Mu", firstName="Nik", middleName="Che")

create_user_response = public_users_client.create_user(request=create_user_request)

authentication_user = AuthenticationUserDict(email=create_user_request["email"], password=create_user_request["password"])

private_users_client = get_private_users_client(authentication_user)

user_response = private_users_client.get_user(create_user_response["user"]["id"])

print(create_user_response)

print(user_response)
