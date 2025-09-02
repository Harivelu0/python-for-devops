provider "aws" {
   region="us-east-1"
  }

resource "aws_vpc" "myvpc" {
  cidr_block="10.0.0.0/16"
}

resource "aws_instance" "myinstance"{
   ami= "ami-0c02fb55956c7d316"
   instance_type="t2.micro"
}
resource "aws_s3_bucket" "bucket" {
  bucket="python-ac-bucket-${random_id.bucket_id.hex}"
}
resource "random_id" "bucket_id" {
  byte_length = 4
}