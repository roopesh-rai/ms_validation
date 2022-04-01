import requests
# URL = "http://127.0.0.1:8000/stuinfo/"

# r = requests.get(url= URL)
r = requests.get(url="http://127.0.0.1:8000/stuinfo/2")
data = r.json()
print(data)