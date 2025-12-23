import requests
import allure
from data.urls import url
from test_data import test_data  # Импортируем тестовые данные

class TestGetListOfOrders:
    @allure.title('Получение списка заказов')
    @allure.description('Получение списка заказов (код - 200 и "orders" в ответе)')
    def test_get_list_of_orders(self):
        payload = test_data["order"]  # Используем общие данные заказа

        requests.post(f"{url}/api/v1/orders", json=payload)
        r = requests.get(f"{url}/api/v1/orders")
        assert r.status_code == 200
        assert 'orders' in r.json()
