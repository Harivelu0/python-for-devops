

# 🐳 Week 3: Docker & Python for Containerized Applications

## 📌 Overview

This week focuses on integrating Python with Docker to manage containers and create containerized applications for DevOps automation.

You’ll build:

1. **Docker Manager CLI** – Start, stop, restart, or remove containers.
2. **Dockerized Flask App** – Exposes system CPU and memory metrics via API.

---

## 🚀 Features

✅ Manage Docker containers from the command line using Python & `subprocess`.
✅ Build a Flask API that returns real-time CPU & memory usage.
✅ Containerize Python apps with Docker.
✅ Use `psutil` for system metrics.

---

## ⚙️ Requirements

* Python 3.8+
* Docker installed & running
* Flask
* psutil

---

## 📦 Installation

```bash
pip install flask psutil
```

---

## 💻 Usage

### **1. Docker Manager CLI**

Manage containers directly from Python.

**Syntax:**

```bash
python docker_manager.py --action <start|stop|restart|rm> --container <container_id_or_name>
```

**Example:**

```bash
python docker_manager.py --action start --container my_container
python docker_manager.py --action stop --container my_container
```

---

### **2. Flask Metrics API**

Run locally:

```bash
python docker_metric.py
```

Access in browser:

```
http://localhost:5000
http://localhost:5000/metrics
```

---

### **3. Containerizing the Flask App**

**`requirements.txt`**

```
flask
psutil
```

**`Dockerfile`**

```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY docker_metric.py .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD ["python3", "docker_metric.py"]
```

**Build & Run**

```bash
docker build -t metrics-app .
docker run -p 5000:5000 metrics-app
```

---
