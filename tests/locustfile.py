import json
import requests
s = requests.Session()


# http://localhost:8089
# https://pypi.org/project/locust/
# https://www.youtube.com/watch?v=_Z62E46bDmY
from locust import HttpUser, SequentialTaskSet, task, between, constant, user


class User(HttpUser):
    @task (user)
    class SequenceOfTasks(SequentialTaskSet):
        # wait_time = between(1, 5)
        wait_time = constant(1)

        @task(user)
        def mainPage(self):
            self.client.get("/")
            # with   self.client.get("http://jsonplaceholder.typicode.com/todos"catch_response=True) as response:
            #     assert response == json, 'not answer to todos'

        @task(user)
        def login(self):
            print('ttests')
            # self.client.options("https://api.demoblaze.com/login")
            # self.client.post("https://api.demoblaze.com/login", json={"username": "aaaa", "password": "YWFhYQ=="})
            # self.client.options("https://api.demoblaze.com/check")
            # self.client.get("http://jsonplaceholder.typicode.com/todos/1") as request:
            # self.client.post("https://petstore.swagger.io/v2/swagger.json", json={"token": "YWFhYTE2MzA5NDU="})
            # assert request == json, 'not answer to todos/1'
        @task(user)
        def clickProduct(self):
            self.client.get("http://jsonplaceholder.typicode.com/todos/1")
            # self.client.options("https://api.demoblaze.com/check")
            # self.client.options("https://api.demoblaze.com/view")
            # self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
            # self.client.post("https://api.demoblaze.com/view", json={"id": "1"})

        @task
        def addToCart(self):
          self.client.options("http://jsonplaceholder.typicode.com/todos/2")
        # self.client.post("https://api.demoblaze.com/addtocart",
        #                  json={"id": "fb3d5d23-f88c-80d9-a8de-32f1b6034bfd", "cookie": "YWFhYTE2MzA5NDU=",
        #                        "prod_id": 1, "flag": 'true'})

        @task
        def viewCart(self):
            self.client.get("http://jsonplaceholder.typicode.com/todos/3")
        # self.client.options("https://api.demoblaze.com/check")
        # self.client.options("https://api.demoblaze.com/viewcart")
        # self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
        # self.client.post("https://api.demoblaze.com/viewcart", json={"cookie": "YWFhYTE2MzA5NDU=", "flag": 'true'})
        # self.client.options("https://api.demoblaze.com/view")
        # self.client.post("https://api.demoblaze.com/check", json={"token": "YWFhYTE2MzA5NDU="})
        # self.client.post("https://api.demoblaze.com/view", json={"id": "1"})

        @task
        def viewCart(self):
            self.client.get("http://jsonplaceholder.typicode.com/todos/5")


