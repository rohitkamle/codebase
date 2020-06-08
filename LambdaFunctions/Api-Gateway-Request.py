import http.client
import json
from datetime import datetime
import calendar
import random
import time


def post_to_apigateway(id, timestamp, message):
    
    conn = http.client.HTTPSConnection('632xtsewze.execute-api.ap-south-1.amazonaws.com')
    headers = {'Content-type': 'application/json'}
    
    post_body = {
          "id": id,
          "timestamp": timestamp,
          "message": message
        }
        
    json_data = json.dumps(post_body)
    print (json_data)
    conn.request('POST', '/prod/adddata', json_data, headers)
    response = conn.getresponse()
    print (json.dumps(response.status), json.dumps(response.reason))

while True:
    id = random.choice(('Device5', 'Device6', 'Device7'))
    timestamp = calendar.timegm(datetime.utcnow().timetuple())
    message = random.choice(('Healthy', 'Error'))
    
    post_to_apigateway(id, timestamp, message)

    # wait for 5 second
    time.sleep(1)