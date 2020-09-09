"""
Requirements:

locust==1.2.3

Run:
locust --host=http://localhost:8000/api/v2
locust --host=http://localhost:8000/api/v2 --no-web -c 100 -r 10
"""
import os 
from locust import HttpUser, task, between

MIN_WAIT = int(os.getenv("MIN_WAIT", 1))
MAX_WAIT = int(os.getenv("MAX_WAIT", 3))

class DemoUser(HttpUser):
    wait_time = between(MIN_WAIT, MAX_WAIT)

    @task(1)
    def index(self):
        self.client.get(os.getenv("INDEX", "/"))
