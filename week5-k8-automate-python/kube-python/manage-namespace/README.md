
#  Python + Kubernetes Automation (Week 5 - Task 1)

This project demonstrates how to **manage Kubernetes objects dynamically with Python** using the official Kubernetes Python SDK.

##  What it Does
- Creates or deletes Kubernetes namespaces from Python.  
- Handles common errors (namespace already exists / not found).  

## 🛠️ Requirements
- Python 3.8+  
- Access to a Kubernetes cluster (via `~/.kube/config`)  
- Install dependencies:  

```bash
pip install kubernetes argparse
````

## ▶️ Usage

Run the script with desired action:

```bash
# Create a namespace
python main.py --action create --name dev-namespace

# Delete a namespace
python main.py --action delete --name dev-namespace
```

