import os
import requests
from datetime import datetime

API_ID = os.environ['NT_APP_ID']
API_KEY = os.environ['NT_API_KEY']
Authorization = os.environ['Authorization']


END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
Sheety_Endpoint = "https://api.sheety.co/39c61fdf9b97ac405ce00ee02671cfb0/workouts/sheet1"

Parameters = {
    "query": input("Tell me which exercises you did: "),
    "gender": "male",
    "weight_kg": 59,
    "age": 20,
}

header = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

access_header = {
    "Authorization": Authorization,
}

response = requests.post(url=END_POINT, json=Parameters, headers=header)
data = response.json()["exercises"]
# print(len(data))

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")

for i in range(0, len(data)):
    exercise = data[i]["name"].title()
    duration = data[i]["duration_min"]
    calories = data[i]["nf_calories"]
    user_data = {
        "sheet1": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration": duration,
            "calories": calories,
        }
    }
    response = requests.post(url=Sheety_Endpoint, json=user_data, headers=access_header)
    print(response.text)
