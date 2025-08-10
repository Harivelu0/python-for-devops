#  Python for DevOps: Foundational Projects

This repository contains beginner-friendly yet practical Python scripts designed to help DevOps engineers strengthen their Python skills through real-world tasks.

---

## 📁 Project 1: Log Parser from `/var/log/`

**Description:**  
A Python script that automates log parsing from system log files (like `syslog`, `auth.log` etc.) located in `/var/log/`. It extracts useful insights such as error frequency, failed login attempts, and important timestamps.

**Features:**  
- Handles plain `.log` or zipped `.zip` log files
- Extracts timestamp, log level, and message
- Filters common patterns (e.g., `error`, `failed`, `warning`)
- Outputs a clean summary or CSV for analysis

**How to Run:**

```bash
python3 -m log_parser --input /var/log/syslog
```

---

## 📊 Project 2: CPU & Memory Usage Monitor

**Description:**  
A real-time system monitoring script using the `psutil` library to track CPU and memory usage. Useful for lightweight monitoring or learning system introspection with Python.

**Features:**  
- Displays CPU and memory usage every few seconds
- Alerts when usage exceeds defined thresholds
- Can be extended to monitor disk or network usage

**How to Run:**

```bash
python3 -m system_monitor
```

---

## 📦 Requirements

- Python 3.7+
- `psutil` (`pip install psutil`)

---

## 🛠️ Future Improvements

- Add a web UI (Flask) to display live monitoring
- Integrate log analyzer with alerting tools (Slack, email)
- Use Gemini LLM for smart log insights

---

## 🚀 Author

Built with ❤️ by Hari
