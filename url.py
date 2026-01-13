class Url:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    create_courier_endpoint = '/api/v1/courier'
    login_courier_endpoint = '/api/v1/courier/login'
    orders_list_endpoint = '/api/v1/orders'

# Конкатенируем URL с конечными точками
    create_courier_url = BASE_URL + create_courier_endpoint
    login_courier_url = BASE_URL + login_courier_endpoint
    orders_list_url = BASE_URL + orders_list_endpoint

#print(create_courier_url)  # https://qa-scooter.praktikum-services.ru/api/v1/courier
#print(login_courier_url)   # https://qa-scooter.praktikum-services.ru/api/v1/courier/login
#print(orders_list_url)     # https://qa-scooter.praktikum-services.ru/api/v1/orders
