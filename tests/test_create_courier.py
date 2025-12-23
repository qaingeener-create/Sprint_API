import requests
import allure
from data.urls import url
from data.courier_data import generation_new_data_courier
import logging

# Вынесем шаги в отдельный модуль
def create_courier(payload):
    response = requests.post(f"{url}/api/v1/courier", json=payload)
    return response

def login_courier(login_payload):
    response = requests.post(f"{url}/api/v1/courier/login", json=login_payload)
    return response

def delete_courier(courier_id):
    response = requests.delete(f"{url}/api/v1/courier/{courier_id}")
    return response

class TestCreateCourier:
    @allure.title('Создание курьера')
    def test_create_courier(self):
        data = generation_new_data_courier()
        payload = data
        logging.info(f"Data for courier creation: {data}")

        response = create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}, "Неверное содержимое ответа."

        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        login_response = login_courier(login_payload)
        assert login_response.status_code == 200, "Login failed."

        courier_id = login_response.json().get("id")
        assert courier_id is not None, "Courier ID not found in login response."

        # Delete the created courier
        delete_response = delete_courier(courier_id)
        assert delete_response.status_code == 200, "Failed to delete courier."

    @allure.title('Проверка невозможности создать курьера с уже существующими учётными данными')
    @allure.description('Проверка, что нельзя создать курьера с уже существующеми кредами (код - 409 и текст - "message": "Этот логин уже используется. Попробуйте другой.")')
    def test_create_courier_duplicate_login(self):
        data = generation_new_data_courier()
        payload = data
        response = create_courier(payload)

        assert response.status_code == 409
        assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}, "Неверное содержимое ответа."

    @allure.title('Проверка невозможности создать курьера без всех обязательных полей')
    @allure.description(
        'Проверка заполнения не всех обязательных полей. Курьер не создан (код - 400 и текст - "message": "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_password(self):
        data = generation_new_data_courier()
        payload = {
            "login": data["login"],
            "firstName": data["firstName"]
        }
        response = requests.post(f"{url}/api/v1/courier", json=payload)

        assert response.status_code == 400
        assert response.json() == {"code": 400,
                                   "message": "Недостаточно данных для создания учетной записи"}, "Неверное содержимое ответа."