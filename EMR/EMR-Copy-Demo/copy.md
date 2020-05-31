<!-- Step Type -->
Custome Jar

<!-- Name -->
CopyCommand

<!-- #Jar Location -->
command-runner.jar

<!-- Arguments -->
s3-dist-cp --s3Endpoint=s3.amazonaws.com --src=s3://rkamle-emr/emr-copy-demo/ --dest=hdfs:///output

<!-- Login to EC2 instance and run below command to check the file -->
hadoop fs -ls hdfs:///output

