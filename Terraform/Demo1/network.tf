provider "aws" {
  region = "us-east-1"
}
variable "region" {
     default = "us-east-1"
}
variable "availabilityZone" {
     default = "us-east-1a"
}
variable "instanceTenancy" {
    default = "default"
}
variable "vpcCIDRblock" {
    default = "20.0.0.0/16"
}
variable "subnetCIDRblock" {
    default = "20.0.1.0/24"
}

# create the VPC
resource "aws_vpc" "simplevpc" {
  cidr_block           = var.vpcCIDRblock
  instance_tenancy     = var.instanceTenancy
tags = {
    Name = "TF-vpc-simple"
}
}



# create the Subnet
resource "aws_subnet" "simplesubnet" {
  vpc_id                  = aws_vpc.simplevpc.id
  cidr_block              = var.subnetCIDRblock
  availability_zone       = var.availabilityZone
tags = {
   Name = "TF-SN-simple"
}

} 
  
output "vpc_id" {
  value = aws_vpc.simplevpc.id
}

output "subnet_id" {
  value = aws_subnet.simplesubnet.id
}