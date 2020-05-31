import json
import boto3
ec2client = boto3.client('ec2')
def main(event, context):
    response = ec2client.describe_instances()
    for i in response['Reservations']:
        for e in i['Instances']:
            print (e['InstanceId'])
            id = e['InstanceId']
            try:
                nametag = e['Tags']
                print ('Tag found')
                key = e['Tags']
                for i in key:
                    if 'Name' in i:
                        print (i)
                    else:
                        print('no name key')
                        stopec2 = ec2client.stop_instances(InstanceIds=[id])
                        
                        print (stopec2)
                        print ('Stopping instance' + id)
                   
                    
                print (e['Tags'])
            except:
                print ('some error')
                

    return {
       'body': 'Trying to stop untagged instances'
        
    }