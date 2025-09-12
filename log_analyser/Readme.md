
# Log Anomaly Detection System

A Python + Flask web application that detects anomalies in logs using machine learning (Isolation Forest) and visualizes them for easy debugging.

## 🚀 Features

- Upload log files (.log or .txt)
- Intelligent anomaly detection beyond simple ERROR filtering
- Advanced feature extraction from log messages
- Visualization with highlighted anomalies
- Export results as CSV for further analysis

## 🧰 Tech Stack

- Python 3.10+
- Flask for the web interface
- scikit-learn for Isolation Forest algorithm
- pandas for data manipulation
- matplotlib for visualization

## 🏃‍♂️ Quick Start

1. Clone the repository
   ```bash
   git clone https://github.com/Harivelu0/log-anomaly-detector.git
   cd log-anomaly-detector
   ```

2. Create & activate virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application
   ```bash
   python main.py
   ```

5. Open http://127.0.0.1:5000/ in your browser

## 🗂️ Project Structure

```
log_analyser/
├── Readme.md
├── core/
│   ├── anamoly_detector.py  # ML algorithm implementation
│   ├── parser.py            # Log file parsing
│   └── preprocessor.py      # Feature extraction
├── logs/                    # Uploaded logs storage
├── main.py                  # Flask application
├── requirements.txt         # Dependencies
├── static/                  # Static assets (charts)
│   └── anomaly_chart.png
└── templates/               # HTML templates
    └── index.html           # Main UI
```

## 📊 How It Works

1. **Log Parsing**: Convert raw logs to structured data
2. **Feature Extraction**: Generate numeric features from log content
3. **Anomaly Detection**: Use Isolation Forest to identify outliers
4. **Visualization**: Display anomalies in chart and table format

## 📝 Usage

1. Open the web UI
2. Upload a log file (.log or .txt)
3. The app will:
   * Parse the logs
   * Preprocess log messages
   * Detect anomalies using ML
   * Show results in a chart and a table
4. You can download the results as `anomalies.csv`

## 📈 Future Improvements

- Add support for more log formats
- Implement adaptive learning based on user feedback
- Add clustering to group similar anomalies
- Create API endpoints for integration with other systems
- Add real-time processing capability for streaming logs

## 👤 Author

Made with ❤️ by [Hari](https://github.com/Harivelu0)
```