
# 🚀 Python + Terraform Automation (Week 4 - Task 1)

This project demonstrates how to **automate Terraform commands using Python** to provision basic AWS infrastructure.  

## 📦 Infrastructure Provisioned
- **VPC** (10.0.0.0/16)  
- **EC2 instance** (`t2.micro`, Amazon Linux 2 AMI)  
- **S3 bucket** (with random suffix for uniqueness)  

## 🛠️ Requirements
- Python 3.8+  
- [Terraform](https://developer.hashicorp.com/terraform/downloads) installed and accessible in `$PATH`  
- AWS CLI configured with valid credentials (`aws configure`)  
- Python dependencies:  

```bash
pip install python-terraform argparse
````

## ▶️ Usage

Run the Python script to execute Terraform actions:

```bash
# Initialize terraform
python main.py --action init

# Plan resources
python main.py --action plan

# Apply changes (create resources)
python main.py --action apply

# Destroy resources
python main.py --action destroy
```


