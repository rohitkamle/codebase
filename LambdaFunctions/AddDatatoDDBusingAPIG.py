import boto3
import json
from datetime import datetime
import calendar
import random
import time
import uuid
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('devicedata')

def lambda_handler(event, context):
    # TODO implement
    device = event['id']
    timestamp = event['timestamp']
    message = event['message']
    print (id)
    uid = str(id)
    
    data = {
            'id': device,
            'timestamp': timestamp,
            'message': message,
    }   
    print (data)
    dbresponse = table.put_item(
           Item=data
        )
    print (dbresponse)

    return {
        'statusCode': 200,
        'body': json.dumps(dbresponse)
    }

