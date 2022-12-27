import requests
from datetime import datetime

NUTRITION_ID = "752834f7"
NUTRITION_API_KEY = "5457d94706be1e91a24acc88df3e45aa"
NUTRITION_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

SHEETY_URL = "https://api.sheety.co/19fa8afaa5c3704a3de3037c5f81ce14/workout/workouts"

headers = {
    "x-app-id": NUTRITION_ID,
    "x-app-key": NUTRITION_API_KEY,
    "x-remote-user-id": "0"
}

parameters = {
    "gender": "male",
    "weight_kg": 105,
    "height_cm": 180,
    "age": 24
}

query = input("Tell me which exercises you did: ")
parameters["query"] = query
sheety_params = {
    "workout": {
        "date": "astazi",
        "time": "maine",
        "exercise": "running hot",
        "duration": "1000sec",
        "calories": "32"
    }
}

with requests.post(url=SHEETY_URL, json=sheety_params) as post:
    print(post.text)

with requests.get(url=SHEETY_URL) as data:
    pass

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")


with requests.post(url=NUTRITION_URL, data=parameters, headers=headers) as response:
    exercise_data = response.json()

for exercise in exercise_data["exercises"]:
    sheety_params = {
        "workout": {
            "date": today_date
        }
    }