import json
import boto3
ec2client = boto3.client('ec2')
def main(event, context):
    response = ec2client.describe_instances(Filters=[{'Name': 'tag:Environment', 'Values': ['Dev']}])
    for i in response['Reservations']:
        for e in i['Instances']:
            print (e['InstanceId'])
            id = e['InstanceId']
            stopec2 = ec2client.stop_instances(InstanceIds=[id])
            print (stopec2)
    return {
       'body': 'Stop Development Instance'
        
    }