import json

def lambda_handler(event, context):
    # TODO 
    
    fileName = event['Records'][0]['s3']['object']['key']
    print ('file uploaded to S3', fileName)
    return {
        'statusCode': 200,
        'body': {'file uploaded to S3' : fileName}
    }
