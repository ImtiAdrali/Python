import os
import requests
from datetime import datetime

APPICATION_ID = "APPICATION_ID"
API_KEY = "API_KEY"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APPICATION_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}


user_input = input("Tell me which exercise you did: ")
exercise_paramester = {
    "query": user_input,
    "gender": "male",
    "age": 25
}


response = requests.post(url=exercise_endpoint, json=exercise_paramester, headers=headers)

response.raise_for_status
data = response.json()
print(data)
for exercise in data["exercises"]:
    add = {
        "workout" : {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url="https://api.sheety.co/0eaf3971e85ff2a0c43ec46ca984a225/workoutTracking/workouts", json=add)


