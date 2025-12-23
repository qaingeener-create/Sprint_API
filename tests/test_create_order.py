import requests
import allure
import pytest
from data.urls import url
from test_data import test_data  # Импортируем тестовые данные

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

        r = requests.post(f"{url}/orders_list_endpoint", json=payload)
        assert r.status_code == 201
        assert 'track' in r.json()
