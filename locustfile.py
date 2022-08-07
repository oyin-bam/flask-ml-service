import time
from locust import HttpUser, TaskSet, task, between

class APIUser(HttpUser):
    
    min_wait = 5000
    max_wait = 9000
    host = "https://bam-flask-app.azurewebsites.net:443"

    @task
    def index(self):
        self.client.get("/")
        
    @task
    def get_prediction(self):
        self.client.post("/predictions", json={
    "CHAS": {
        "0": 0
    },
    "RM": {
        "0": 6.575
    },
    "TAX": {
        "0": 296.0
    },
    "PTRATIO": {
        "0": 15.3
    },
    "B": {
        "0": 396.9
    },
    "LSTAT": {
        "0": 4.98
    }
})  