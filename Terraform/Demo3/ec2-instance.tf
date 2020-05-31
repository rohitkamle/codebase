
resource "aws_instance" "web" {
  ami           = var.ImageId
  instance_type = "t2.micro"
  subnet_id = aws_subnet.My_VPC_Subnet.id

 
  tags = {
    Name = "webserver"
  }
}

output "instance_id" {
  value = aws_instance.web.private_ip
}