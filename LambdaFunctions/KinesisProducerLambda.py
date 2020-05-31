import boto3
import json
from datetime import datetime
import calendar
import random
import time
my_stream_name = 'news3stream'
kinesis_client = boto3.client('kinesis', region_name='ap-south-1')
def lambda_handler(event, context):
    # TODO implement
    message = event['message']
    timestamp = event['timestamp']
    Id = event['Id']
    data = {
                'message': message,
                'timestamp': timestamp,
                'Id': Id
              }
    put_response = kinesis_client.put_record(
                        StreamName=my_stream_name,
                        Data=json.dumps(data),
                        PartitionKey=Id)    
    return {
        'statusCode': 200,
        'body': json.dumps(data)
    }
