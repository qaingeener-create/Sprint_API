import requests
import allure
from data.URL import url
from data.courier_data import generation_new_data_courier
import logging





class TestCreateCourier:

    @allure.step('Создание курьера')
    def create_courier(payload):
            response = requests.post(f"{url}/api/v1/courier", data=payload)
            return response

    def test_create_courier(self, registered_courier_data):
        data = generation_new_data_courier()
        data.pop("firstName")
        payload = data
        logging.info(f"Data for courier creation: {data}")
        

        response = requests.post(f"{url}/api/v1/courier", data=payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}, "Неверное содержимое ответа."

        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        login_response = requests.post(f"{url}/api/v1/courier/login", data=login_payload)
        assert login_response.status_code == 200, "Login failed."

        courier_id = login_response.json().get("id")
        assert courier_id is not None, "Courier ID not found in login response."

        # Delete the created courier
        delete_response = requests.delete(f"{url}/api/v1/courier/{courier_id}")
        assert delete_response.status_code == 200, "Failed to delete courier."

    @allure.step('Проверка создания курьера с уже существующими учётными данными')
    def create_courier_with_duplicate_credentials(payload):
        response = requests.post(f"{url}/api/v1/courier", data=payload)
        return response
    @allure.title('Проверка невозможности создать курьера. дублирующие креды')
    @allure.description('Проверка, что нельзя создать курьера с уже существующеми кредами (код - 409 и текст - "message": "Этот логин уже используетсяПопробуйте другой."')
    def test_create_courier_duplicate_login(self, registered_courier_data):
        payload = registered_courier_data
        response = requests.post(f"{url}/api/v1/courier", data=payload)

        assert response.status_code == 409
        assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}, "Неверное содержимое ответа."

    @allure.step('Проверка создания курьера без всех обязательных полей')
    def create_courier_without_required_fields(payload):
        response = requests.post(f"{url}/api/v1/courier", data=payload)
        return response
    @allure.title('Проверка невозможности создать курьера. Не все обязательные поля')
    @allure.description(
        'Проверка заполнения не всех обязательных полей. Курьер не создан (код - 400 и текст - "message": "Недостаточно данных для создания учетной записи"')
    def test_create_courier_without_password(self):
        data = generation_new_data_courier()
        payload = {
            "login": data["login"],
            "firstName": data["firstName"]
        }
        response = requests.post(f"{url}/api/v1/courier", data=payload)

        assert response.status_code == 400
        assert response.json() == {"code": 400,
                                   "message": "Недостаточно данных для создания учетной записи"}, "Неверное содержимое ответа."