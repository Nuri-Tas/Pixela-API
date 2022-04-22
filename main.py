import requests
from datetime import datetime

token = "fasdkvxesdcedfc"
user_parameters = {
    "token": token,
    "username": "cantas",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}


#user_response = requests.post(url="https://pixe.la/v1/users", json=user_parameters)
#print(user_response.text)

headers = {
    "X-USER-TOKEN": token
}

graph_params = {
    "id":"graph1",
    "name":"graph-name",
    "unit":"hour",
    "type":"float",
    "color":"shibafu"
}

graph_response = requests.post(url="https://pixe.la/v1/users/cantas/graphs",headers=headers, json=graph_params)
#print(graph_response.text)

update_params= {
    "name":"daily python",
    "unit":"hour",
    "color":"momiji"
}


udpate_response = requests.put(url="https://pixe.la/v1/users/cantas/graphs/graph1",headers=headers,json=update_params)


now = datetime.now()

# datetime.strftime converts different time formats to another
value_format = now.strftime("%Y%m%d")
print("value format: ", value_format)

today = str(now.today()).split(" ")[0]

dates = today.split("-")

value_date = ""
for date in dates:
    value_date += date
print(value_date)

value_params = {
    "date":value_format,
    "quantity":"4"
}


value_response = requests.post(url="https://pixe.la/v1/users/cantas/graphs/graph1", headers=headers, json=value_params)
print(value_response.text)

yesterday = datetime(year=2022, month=4, day=5)
yesterday_format = yesterday.strftime("%Y%m%d")
value_yesterday = {
    "date": yesterday_format,
    "quantity": "0.2"
}

yesterday_response = requests.post(url="https://pixe.la/v1/users/cantas/graphs/graph1", headers=headers, json=value_yesterday)
print(yesterday_response.text)

value_update = {
    "date":value_format,
    "quantity":"5"
}

value_update2 = requests.put(url=f"https://pixe.la/v1/users/cantas/graphs/graph1/{value_format}", headers=headers, json=value_update)
print(value_update2.text)