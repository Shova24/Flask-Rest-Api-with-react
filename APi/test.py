import requests
BASE = 'http://127.0.0.1:5000/'

data = [
    {"name": "Rest Api with Flask","likes": 10, "views": 1000},
    {"name": "Flask","likes": 10, "views": 1000},
    {"name": " Api with Flask","likes": 10, "views": 1000}
]


# creating data 
# for i in range(len(data)):
#     url = '/videos/' + str(i)
#     response = requests.put(BASE + url, data[i])
#     print(response.json())

input()
#geting data 
response = requests.get(BASE + "videos/1")
print(response.json())

input()
#deleting data
response = requests.delete(BASE + "videos/1")
print(response)

input()
#geting data after delete
response = requests.get(BASE + "videos/1")
print(response.json())


# response = requests.get(BASE + 'helloworld/shova')
# print(response.json())
# response = requests.put(BASE + '/videos/1', {"name": "Rest Api with Flask","likes": 10, "views": 1000})
# print(response.json())

# input()
# response = requests.get(BASE + '/videos/19')
# print(response.json())
