
#Run program using Super User / Admin
sudo su 
#Update yum packages
yum update -y
#install httpd server
yum install httpd -y
# keep it running after restart
chkconfig httpd on
#start httpd server
service httpd start
#check httpd service status
service httpd status
#make ec2-user as owner of /var/www/html
sudo chown -R ec2-user /var/www
# go to folder
cd /var/www/html
# create sample html file
echo '<h1> Welcome to my first EC2 Demo </h1>' > index.html









