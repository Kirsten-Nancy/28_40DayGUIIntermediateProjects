import requests
import datetime
import config

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = config.SHEET_ENDPOINT

headers = {
    "x-app-id": config.APP_ID,
    "x-app-key": config.API_KEY
}
nutritionix_data = {
    "query": input("Enter exercise undertaken: "),
    "gender": "female",
    "weight_kg": 53,
    "height_cm": 157,
    "age": 23
}
nutritionix_response = requests.post(url=nutritionix_endpoint, json=nutritionix_data, headers=headers)
exercise_data = nutritionix_response.json()['exercises']
print(exercise_data)

headers = {
    "headers": config.AUTH_HEADER
}

for i in range(len(exercise_data)):
    exercise_name = exercise_data[i]['name'].title()
    exercise_duration = exercise_data[i]['duration_min']
    calories_burnt = exercise_data[i]['nf_calories']

    today = datetime.datetime.now()


    sheety_data = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": exercise_name,
            "duration": exercise_duration,
            "calories": calories_burnt
        }
    }

    sheety_post_response = requests.post(url=sheety_endpoint, json=sheety_data, headers=headers,
                                         auth=(config.username, config.SHEET_PASS))
    print(sheety_post_response.text)

    # sheety_delete_response = requests.delete(url=f"{sheety_endpoint}/2")
    # print(sheety_delete_response.text)
