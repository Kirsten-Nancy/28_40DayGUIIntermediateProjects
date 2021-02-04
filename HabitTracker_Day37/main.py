import requests
import config

USERNAME = config.username
TOKEN = config.token

pixela_endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": config.token,
    "username": config.username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_parameters)
# print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

headers = {
    "X-USER-TOKEN": config.token
}

graph_config = {
    "id": "graph01",
    "name": "Flutter Graph",
    "unit": "hours",
    "type": "int",
    "color": "momiji",
    "timezone": "Asia/Shanghai"
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph01"
pixel_config = {
    "date": "20210204",
    "quantity": "6"
}
response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)