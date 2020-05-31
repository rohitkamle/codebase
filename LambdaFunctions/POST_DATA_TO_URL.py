import http.client
import json
from datetime import datetime
import calendar
import random
import time

def lambda_handler(event, context):
    
    conn = http.client.HTTPSConnection('ouwdcvsgu7.execute-api.ap-south-1.amazonaws.com')
    headers = {'Content-type': 'application/json'}
    
    message = random.choice(('Healthy', 'Error'))
    timestamp = calendar.timegm(datetime.utcnow().timetuple())
    Id = random.choice(('Device1', 'Device2', 'Device3'))
    
    
    post_body = {
          "message": message ,
          "timestamp": timestamp ,
          "Id": Id
        }
        
    json_data = json.dumps(post_body)
    conn.request('POST', '/Prod', json_data, headers)
    response = conn.getresponse()

    # TODO implement
    return {
        'statusCode': response.status,
        'data': post_body,
        'response': json.dumps( response.reason)
    }
