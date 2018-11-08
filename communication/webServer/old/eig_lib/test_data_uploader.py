import requests
import uuid
import json

# add inspection example
testinsection = 'test_inspection.json'

with open(testinsection) as data_file:    
    inspectiondata = json.load(data_file)

inspectiondata['inspection_id'] = str(uuid.uuid1())

url = 'http://localhost:3000/addInspection'
headers = {'Content-type': 'application/json'}

# print json.dumps(inspectiondata)
myResponse = requests.post(url, data=json.dumps(inspectiondata), headers=headers)
print myResponse.text

# add sensor example
testsensor = 'test_sensor.json'

with open(testsensor) as data_file:    
    sensorinfo = json.load(data_file)

url = 'http://localhost:3000/addSensor'
headers = {'Content-type': 'application/json'}

# print json.dumps(inspectiondata)
myResponse = requests.post(url, data=json.dumps(sensorinfo), headers=headers)
print myResponse.text




