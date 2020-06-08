import boto3
import json
from datetime import datetime
import calendar
import random
import time
from botocore.exceptions import ClientError
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('devicedata')

def lambda_handler(event, context):
    # TODO implement
    id = event['id']
   
    try:
        response = table.query(
        KeyConditionExpression=Key('id').eq(id)
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        # return response['Item']

        return {
            'statusCode': 200,
            'body': response['Items']
        }

