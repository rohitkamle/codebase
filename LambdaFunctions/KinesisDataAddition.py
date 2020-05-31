import boto3
import json
from datetime import datetime
import calendar
import random
import time
my_stream_name = 'news3stream'
kin_client = boto3.client('kinesis', region_name='ap-south-1')
def lambda_handler(event, context):
    # TODO implement
    message = random.choice(('Healthy', 'Error'))
    timestamp = calendar.timegm(datetime.utcnow().timetuple())
    Id = random.choice(('Device1', 'Device2', 'Device3'))
    

    data = {
                'message': message,
                'timestamp': timestamp,
                'Id': Id
              }
    put_response = kin_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(data),
                        PartitionKey=Id)      
    print (put_response)
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
