
# 🛠 Week 2: Automating DevOps Tasks with Python

## 📌 Overview

This project contains two Python-based CLI tools for automating daily DevOps operations:

1. **AWS EC2 Instance Manager** – Start, stop, or terminate EC2 instances.
2. **Kubernetes Pod Status Checker** – Get the list and status of pods in a specific namespace.

## 🚀 Features

✅ Manage AWS EC2 instances via CLI (`start`, `stop`, `terminate`).
✅ Check Kubernetes pod statuses for a given namespace.
✅ Built using `boto3`, `argparse`, and `subprocess`.
✅ Simple CLI-based workflow for quick DevOps automation.

---

## ⚙️ Requirements

* Python 3.8+
* AWS credentials configured locally (`aws configure`)
* `boto3` library
* `kubectl` installed & configured to access your Kubernetes cluster

---

## 📦 Installation

```bash
pip install boto3
```

---

## 💻 Usage

### **1. AWS EC2 Instance Manager**

Start, stop, or terminate EC2 instances.

**Syntax:**

```bash
python ec2_manager.py --action <start|stop|terminate> --instance-ids <id1> <id2> ...
```

**Example:**

```bash
python ec2_manager.py --action start --instance-ids i-0123456789abcdef0
python ec2_manager.py --action stop --instance-ids i-0123456789abcdef0
python ec2_manager.py --action terminate --instance-ids i-0123456789abcdef0
```

> 💡 **Note:** Termination requires confirmation in the CLI.

---

### **2. Kubernetes Pod Status Checker**

Check pods in a given namespace.

**Syntax:**

```bash
python k8s_pod_checker.py --namespace <namespace>
```

**Example:**

```bash
python k8s_pod_checker.py --namespace default
python k8s_pod_checker.py --namespace kube-system
```

---
