import requests
import os
from dotenv import load_dotenv
load_dotenv()



class UserClient:

    BASE_URL = "https://reqres.in/api"
    HEADERS = {
        "x-api-key": os.getenv("REQRES_API_KEY")
    }

    def get_user(self, user_id: int):
        response = requests.get(
            f"{self.BASE_URL}/users/{user_id}",
            headers=self.HEADERS
        )
        return response

    def create_user(self, name: str, job: str):
        response = requests.post(
            f"{self.BASE_URL}/users",
            json={
                "name": name,
                "job": job
            },
            headers=self.HEADERS
        )
        return response