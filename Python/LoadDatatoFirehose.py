import boto3
import json
from datetime import datetime
import calendar
import random
import time

streamname = 'simplejson'

fhclient = boto3.client('firehose', region_name='us-east-1')

def put_to_stream(property_value, property_timestamp):
    message = random.choice(('Healthy', 'Error'))
    timestamp = calendar.timegm(datetime.utcnow().timetuple())
    Id = random.choice(('Device1', 'Device2', 'Device3'))
    
    
    post_body = {
          "message": message ,
          "timestamp": timestamp ,
          "Id": Id
        }
        

    addedline = str(post_body) + '\n'
    print (addedline)
    response = fhclient.put_record(
           DeliveryStreamName = streamname,
           Record={
                'Data': addedline
            }
        )
    print(response)

while True:
    property_value = random.randint(40, 120)
    property_timestamp = calendar.timegm(datetime.utcnow().timetuple())
    thing_id = 'aa-bb'

    put_to_stream(property_value, property_timestamp)

    # wait for 5 second
    time.sleep(1)