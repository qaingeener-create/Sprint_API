from allure import step
from data.urls import url
import random
import string
import requests

@step('Generate new courier data')
def generate_new_data_courier():
    letters = string.ascii_lowercase
    login_new = ''.join(random.choice(letters) for i in range(10))
    password_new = ''.join(random.choice(letters) for i in range(10))
    first_name_new = ''.join(random.choice(letters) for i in range(10))

    return {
        "login": login_new,
        "password": password_new,
        "firstName": first_name_new
    }

@step('Register new courier and return login password')
def register_new_courier_and_return_login_password():
    data = generate_new_data_courier()
    payload = {
        "login": data["login"],
        "password": data["password"],
        "firstName": data["firstName"]
    }

    response = requests.post(f"{url}/api/v1/courier", json=payload)

    if response.status_code == 201:
        return [data["login"], data["password"], data["firstName"]]

@step('Create courier')
def create_courier(payload):
    response = requests.post(f"{url}/api/v1/courier", json=payload)
    return response

@step('Login courier')
def login_courier(login_payload):
    response = requests.post(f"{url}/api/v1/courier/login", json=login_payload)
    return response

@step('Delete courier')
def delete_courier(courier_id):
    response = requests.delete(f"{url}/api/v1/courier/{courier_id}")
    return response
