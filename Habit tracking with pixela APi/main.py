import requests
from datetime import datetime

USERNAME = "USERNAME"
TOKEN = "TOKEN"
ID = "ID"
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
};


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
grap_params = {
    "id": ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN 
}

# response = requests.post(url=grap_endpoint, json=grap_params, headers=headers)
# print(response.text)
today = datetime(year=2022, month=6, day=19)
# post_pixel_endpoint = f"{grap_endpoint}/{ID}"


pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "8",
}

update_pixel_params = {
    "quantity": "18",

}
year = pixel_params["date"]
grap_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{year}"
response = requests.delete(url=grap_endpoint, headers=headers)
print(response.text)