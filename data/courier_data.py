from helpers import generate_new_data_courier
from data.URL import url
import requests

def register_new_courier_and_return_login_password():
    data = generate_new_data_courier()
    payload = {
        "login": data["login"],
        "password": data["password"],
        "firstName": data["firstName"]
    }

    response = requests.post(f"{url}/api/v1/courier", data=payload)

    if response.status_code == 201:
        return [data["login"], data["password"], data["firstName"]]

