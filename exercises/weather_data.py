import urllib.request
import requests
import json


api_id = "84600bca7507293656495e8972aec659"
city_id = "Southampton"

mode = "json"
unit = "metric"

api = 'http://api.openweathermap.org/data/2.5/weather?q='

full_api_url = api + str(city_id) + '&mode=' + mode + '&units=' + unit + '&APPID=' + api_id
print(full_api_url)
request_data = requests.get(full_api_url)

print("Status:", format(request_data))

data = json.loads(request_data.text)

print(data['main']['temp'])
print(data['weather'][0]['description'])


#with urllib.request.urlopen(full_api_url) as url:
#	return json.loads(url.read().decode('utf-8'))