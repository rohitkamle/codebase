import csv
import boto3

fhclient = boto3.client('firehose')
streamname = 'CSVToS3'
filename = "CovidCases.csv"

with open(filename, 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
        data = row
        data_string = str(data)[1:-1] 
        data_binary_string = str.encode(data_string)
        print (data_binary_string)
        response = fhclient.put_record(
        DeliveryStreamName = streamname,
        Record={'Data': data_string }
        )
        # print(response)
  
