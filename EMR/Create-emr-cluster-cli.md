# Run below command to create cluster with Hive Step
aws emr create-cluster --name "HIVE cluster" --release-label emr-5.30.0 --applications Name=Hive --use-default-roles --ec2-attributes KeyName=rkamle2021,SubnetId=subnet-04cad8713fd967cc0 --steps Type=HIVE,Name="HiveProgram",ActionOnFailure=CONTINUE,Args=[-f,s3://rkamle-emr/hive-demo/query/Hive_CloudFront.q,-d,INPUT=s3://rkamle-emr/hive-demo,-d,OUTPUT=s3://rkamle-emr/hive-demo/output] --instance-type m5.xlarge --instance-count 1 --auto-terminate

# get the cluster id .... 
j-3RFR9K41P31CR
# Run below command <replace cluster id >
aws emr describe-cluster --cluster-id j-3RFR9K41P31CR --query Cluster.Status
