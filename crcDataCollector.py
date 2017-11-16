import datetime
import requests
import json
import os

API_TOKEN = os.environ["API_TOKEN"]

url = 'https://gatech.weatherstem.com/api'
indata = {'api_key':API_TOKEN,'stations':['crc']}
headers = {'Accept': 'application/json'}
response = requests.get(url, headers=headers, params=indata)



filename = str(datetime.datetime.today().strftime('%b-%d-%Y:%H')) + '.json'

with open('collectedFile.txt', 'a') as dataList:
    dataList.write(filename)
    dataList.write('\n')

print response.content

with open(filename, 'w') as outf:
    outf.write(response.content)
