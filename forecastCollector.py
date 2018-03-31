import datetime
import requests
import json
import os

API_TOKEN = os.environ["API_TOKEN"]

url = 'http://api.wunderground.com/api/'+ API_TOKEN + '/hourly/q/GA/Atlanta.json'
headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers)


filename = str(datetime.datetime.today().strftime('%b-%d-%Y:%H:%M')) + '.json'

with open('/home/wwhitlow/CynicalMeteorologist/collectedFile.txt', 'a') as dataList:
    dataList.write(filename)
    dataList.write('\n')

with open('/home/wwhitlow/CynicalMeteorologist/collectedData/'+filename, 'w') as outf:
    outf.write(response.content)

