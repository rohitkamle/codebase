import json
import boto3
from boto3.dynamodb.conditions import Key, Attr
def main(event, context):

    action = event['Action']
    if action == 'query':
        return get_item(event, context)
    if action == 'putdata':
        return put_item(event, context)
def get_item(event, context):

    key = event['key']
    value = event['value']
    dynamodb_client = boto3.resource('dynamodb', region_name="ap-south-1")
    table = dynamodb_client.Table('demo1')
    response = table.query(
    KeyConditionExpression=Key(key).eq(value)
    )
    
    print(response['Items'])
    return {
        'statusCode': 200,
        'body': json.dumps(response['Items'])
    }

def put_item(event, context):

    dynamodb_client = boto3.resource('dynamodb', region_name="ap-south-1")
    table = dynamodb_client.Table('demo1')
    userid = event['data']
    
    score = event['data']
    
    response = table.put_item(TableName='demo1', Item={'score': '200', 'result': 'lose', 'user_id': 'user1', 'game_id': 'game5'})

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
    # {'score': '200', 'result': 'lose', 'user_id': 'user1', 'game_id': 'game5'}