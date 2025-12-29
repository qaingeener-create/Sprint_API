
from methods.create_courier import CourierMethods
import data




class TestCreateCourier:
    
    #@allure.title('Создание курьера')
    def test_create_courier_success(self):
        response = CourierMethods.create_courier(body = data.DataForCourier.Creat_Courier_Body)
        assert response.status_code == 200
        assert response.json() == {"ok": True}, "Неверное содержимое ответа."
       
       
       
       
       
       
       
       # data = generation_new_data_courier()
        #payload = data
        #l#ogging.info(f"Data for courier creation: {data}")
#
 #       response = create_courier(payload)  # Используем ранее созданный шаг
  #      assert response.status_code == 201
   #     assert response.json() == {"ok": True}, "Неверное содержимое ответа."

        

    #@allure.title('Проверка невозможности создать курьера с уже существующими учётными данными')
    #@allure.description('Проверка, что нельзя создать курьера с уже существующеми кредами (код - 409 и текст - "message": "Этот логин уже используется. Попробуйте другой.")')
 #   def test_create_courier_duplicate_login(self):
  #      data = generation_new_data_courier()
   #     payload = data
    #    response = create_courier(payload)  # Используем ранее созданный шаг
#
 #       assert response.status_code == 409
  #      assert response.json() == {"code": 409, "message": "Этот логин уже используется. Попробуйте другой."}, "Неверное содержимое ответа."

   # @allure.title('Проверка невозможности создать курьера без всех обязательных полей')
   # @allure.description(
    #    'Проверка заполнения не всех обязательных полей. Курьер не создан (код - 400 и текст - "message": "Недостаточно данных для создания учетной записи"')
    #def test_create_courier_without_password(self):
     #   data = generation_new_data_courier()
      #  payload = {
       #     "login": data["login"],
        #    "firstName": data["firstName"]
        #}
        #response = create_courier(payload)  # Используем ранее созданный шаг

        #assert response.status_code == 400
        #assert response.json() == {"code": 400,
         #                          "message": "Недостаточно данных для создания учетной записи"}, "Неверное содержимое ответа."