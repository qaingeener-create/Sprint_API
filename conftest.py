import pytest
from data.courier_data import register_new_courier_and_return_login_password
import logging
import requests
from data.urls import url


@pytest.fixture
def registered_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    courier_data = {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }
    yield courier_data

    # Удаление курьера после теста
    response = requests.post(f"{url}/login_courier_endpoint", json={"login": courier_data["login"], "password": courier_data["password"]})
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f"{url}/create_courier_endpoint/{courier_id}")


@pytest.fixture
def delete_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    yield {
        "login": login_pass[0],
        "password": login_pass[1]
    }
    response = requests.post(f"{url}/login_courier_endpoint", json=login_pass)
    if response.status_code == 200:
        courier_id = response.json().get("id")
        if courier_id:
            requests.delete(f"{url}/create_courier_endpoint/{courier_id}")