import pytest
from data.courier_data import register_new_courier_and_return_login_password
import logging

@pytest.fixture
def registered_courier_data():
    login_pass = register_new_courier_and_return_login_password()
    return {
        "login": login_pass[0],
        "password": login_pass[1],
        "firstName": login_pass[2]
    }