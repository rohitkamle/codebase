import json

def lambda_handler(event, context):
    # TODO implement
    
    print (event['Records'][0]['s3']['object']['key'])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }