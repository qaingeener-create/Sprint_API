import requests
import allure
import pytest
from data.urls import url
from test_data import test_data  # Импортируем тестовые данные

def create_order(payload):
    response = requests.post(f"orders_list_url", json=payload)
    return response

class TestCreateOrder:
    @pytest.mark.parametrize('color', [
        ['BLACK'],
        ['GREY'],
        ['BLACK', 'GREY'],
        []
    ])
    @allure.title('Создание заказа')
    @allure.description('Проверка создания заказа (код - 201 и track в ответе)')
    def test_create_order(self, color):
        payload = {
            **test_data["order"],  # Распаковываем общие данные заказа
            "color": color
        }

        response = create_order(payload)  # Используем ранее созданный шаг
        assert response.status_code == 201
        assert 'track' in response.json()

