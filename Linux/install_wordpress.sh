# Install Wordpress
sudo su
yum update -y
yum install httpd php php-mysql -y
cd /var/www/html
wget https://wordpress.org/latest.tar.gz
tar -xzf latest.tar.gz
cp -r wordpress/* /var/www/html
rm -rf wordpress
rm -f latest.tar.gz
chmod -R 755 wp-content
chown -R apache:apache wp-content
chkconfig httpd on
service httpd start




