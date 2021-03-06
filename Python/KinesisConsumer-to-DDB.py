import boto3
import json
from datetime import datetime
import time
my_stream_name = 'stream-1'
kinesis_client = boto3.client('kinesis', region_name='ap-south-1')
response = kinesis_client.describe_stream(StreamName=my_stream_name)
my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='LATEST')

my_shard_iterator = shard_iterator['ShardIterator']
record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=2)

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1')
table = dynamodb.Table('kinesisdata')


while 'NextShardIterator' in record_response:
    record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=2)

    # print (record_response['Records'])
    for data in record_response['Records']:
        print (data['Data'])
        
        d = json.loads(data['Data'])
        prop = d['prop']
        timestamp = d['timestamp']
        thing_id = d['timestamp']

        dbresponse = table.put_item(
           Item={
        'prop': prop,
        'timestamp': timestamp,
        'thing_id': thing_id
               }
        )
        print (dbresponse)



    # wait for 5 seconds
    time.sleep(1)