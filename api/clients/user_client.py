import requests
import os
from dotenv import load_dotenv
from utils.logger import get_logger
load_dotenv()
logger=get_logger()



class UserClient:

    BASE_URL = "https://reqres.in/api"
    HEADERS = {
        "x-api-key": os.getenv("REQRES_API_KEY")
    }

    def get_user(self, user_id: int):
        endpoint = f"{self.BASE_URL}/users/{user_id}"
        logger.info(f"Sending GET request to {endpoint}")
        response = requests.get(
            endpoint,
            headers=self.HEADERS
        )
        logger.info(f"Received response with status code {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response

    def create_user(self, name: str, job: str):
        endpoint = f"{self.BASE_URL}/users"
        payload = {
                "name": name,
                "job": job
            }
        logger.info(f"Sending POST request to {endpoint}")
        logger.info(f"Request payload: {payload}")
        response = requests.post(
            endpoint,
            json=payload,
            headers=self.HEADERS
        )
        logger.info(f"Received response with status code {response.status_code}")
        logger.info(f"Response body: {response.json()}")
        return response