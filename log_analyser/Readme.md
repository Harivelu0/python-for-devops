
#  Log Anomaly Detection System (v1)

A Python + Flask-based tool that detects anomalies in CI/CD logs (e.g., GitHub Actions) using machine learning (Isolation Forest) and visualizes them for easy debugging.

---

## 🚀 Features

- 📦 Upload `.zip` of GitHub Actions or CI logs
- 📂 Auto-extract and parse `.txt` logs
- 🤖 Detect anomalies using Isolation Forest
- 📊 Visualize anomalies with a red/green bar chart
- 📄 View anomalies in a table (with CSV export)
- 🌐 Lightweight Flask-based web UI

---

## 🧰 Tech Stack

- Python 3.10+
- Flask
- scikit-learn
- pandas
- matplotlib

---

## 🗂️ Project Structure

```

log\_analyser/
├── app/
│   ├── main.py
│   ├── static/
│   │   └── anomaly\_chart.png
│   └── templates/
│       └── index.html
├── core/
│   ├── parser.py
│   ├── preprocessor.py
│   └── anamoly\_detector.py
├── logs/
│   ├── uploaded.zip
│   └── unzipped/
├── requirements.txt
└── README.md

````

---

## ⚙️ Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/log-anomaly-detector.git
cd log-anomaly-detector
````

### 2️⃣ Create & Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Flask App

```bash
python3 -m app.main
```

App will be available at:

```
http://127.0.0.1:5000/
```

---

## 📝 Usage

1. Open the web UI
2. Upload a `.zip` file that contains one or more `.txt` log files (e.g., GitHub Actions logs)
3. The app will:

   * Parse the logs
   * Preprocess log messages
   * Detect anomalies using ML
   * Show results in a chart and a table
4. You can download the results as `anomalies.csv`

---

## 📊 Sample Output

### Anomaly Chart

![Anomaly Chart](log_analyser/static/anomaly_chart.png)

---

## 📌 What’s Next (v2 Plan: CI/CD Analyzer)

* 🔁 Auto-analysis during every GitHub Actions run
* 🤖 Root cause suggestions via LLMs (Gemini/OpenAI)
* 🧠 Smarter error classification
* 🌍 Multi-user dashboard and log history

---

## 👤 Author

Made with ❤️ by [Hari](https://github.com/Harivelu0)

