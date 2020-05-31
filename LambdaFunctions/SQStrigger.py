import json

def lambda_handler(event, context):
    # TODO implement
    
    print (event['Records'][0]['body'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
