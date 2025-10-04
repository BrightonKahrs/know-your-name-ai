from locust import HttpUser, task, between
import json


class NameAnalysisUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        """Called when a user starts"""
        self.client.headers.update({"Content-Type": "application/json"})

    @task(3)
    def analyze_name(self):
        """Test the name analysis endpoint"""
        names = ["John", "Mary", "David", "Sarah", "Michael", "Emma", "James", "Olivia"]

        for name in names:
            payload = {"name": name}
            with self.client.post(
                "/api/nameanalysis/analyze", json=payload, catch_response=True
            ) as response:
                if response.status_code == 200:
                    response.success()
                else:
                    response.failure(f"Failed with status code: {response.status_code}")

    @task(1)
    def health_check(self):
        """Test the health check endpoint"""
        with self.client.get(
            "/api/nameanalysis/health", catch_response=True
        ) as response:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Health check failed: {response.status_code}")


class WebUser(HttpUser):
    wait_time = between(2, 5)

    @task
    def load_homepage(self):
        """Test loading the homepage"""
        self.client.get("/")
