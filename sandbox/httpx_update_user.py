import httpx

from tools.fakers import fake

BASE_URL = "http://127.0.0.1:8000"

USERS_ENDPOINT = "/api/v1/users"

LOGIN_ENDPOINT = "/api/v1/authentication/login"

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post(BASE_URL+USERS_ENDPOINT, json=create_user_payload)
create_user_response_json = create_user_response.json()

print('CREATE_USER PERFORMED')
print(create_user_response.status_code)
print(create_user_response_json)

login_payload = {
  "email": create_user_payload["email"],
  "password": create_user_payload["password"]
}

user_id = create_user_response_json["user"]["id"]

login_response = httpx.post(BASE_URL+LOGIN_ENDPOINT, json=login_payload)
login_response_json = login_response.json()

print('LOGIN PERFORMED')
print(login_response.status_code)
print(login_response_json)

bearer_header = {
    "Authorization": "Bearer "+login_response_json["token"]["accessToken"]
}

update_user_payload = {
  "email": fake.email(),
  "lastName": "string1",
  "firstName": "string1",
  "middleName": "string1"
}

update_user_response = httpx.patch(BASE_URL+USERS_ENDPOINT+f'/{user_id}', json=update_user_payload, headers=bearer_header)
update_user_response_json = update_user_response.json()

print('UPDATE_USER PERFORMED')
print(update_user_response.status_code)
print(update_user_response_json)