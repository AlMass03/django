from locust import HttpUser, task, between

class UserBehavior(HttpUser):
    wait_time = between(1, 3)  # Интервал времени между запросами
    
    @task
    def login(self):
        self.client.post("/login/", json={"username": "test_user", "password": "test_password"})

    @task
    def index_page(self):
        self.client.get("/")