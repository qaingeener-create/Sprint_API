import requests
from url import Url 

class CourierMethods :

    @staticmethod
    def create_courier(body):
        return requests.post (
            url=Url.create_courier_url,
            json=body
        )