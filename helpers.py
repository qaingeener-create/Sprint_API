import random
import string

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
