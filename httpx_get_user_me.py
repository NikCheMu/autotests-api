import httpx

BASE_URL = "http://127.0.0.1:8000"

LOGIN_ENDPOINT = "/api/v1/authentication/login"

GET_ME_ENDPOINT = "/api/v1/users/me"

login_payload = {
  "email": "shchebakov@mail.ru",
  "password": "123QWE"
}

login_response = httpx.post(BASE_URL+LOGIN_ENDPOINT, json=login_payload)
login_response_json = login_response.json()

print(login_response.status_code)
print(login_response_json)

bearer_header = {
    "Authorization": "Bearer "+login_response_json["token"]["accessToken"]
}

get_me_response = httpx.get(BASE_URL+GET_ME_ENDPOINT, headers=bearer_header)
get_me_response_json = get_me_response.json()

print(get_me_response.status_code)
print(get_me_response_json)

