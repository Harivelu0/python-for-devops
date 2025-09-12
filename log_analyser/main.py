from flask import Flask, request, render_template
import os
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from core.parser import parse_log_file
from core.preprocessor import preprocess_features
from core.anamoly_detector import detect_anomalies

app = Flask(__name__)

UPLOAD_FOLDER = "logs/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs("static", exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["logfile"]

        if not uploaded_file or uploaded_file.filename == "":
            return render_template("index.html", message="⚠️ No file selected!", anomalies=None, chart_url=None)

        if not (uploaded_file.filename.endswith(".log") or uploaded_file.filename.endswith(".txt")):
            return render_template("index.html", message="⚠️ Please upload a .log or .txt file!", anomalies=None, chart_url=None)

        try:
            # Save uploaded file
            file_path = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(file_path)

            # Parse → preprocess → detect anomalies
            df_parsed = parse_log_file(file_path)
            df_features = preprocess_features(df_parsed)
            
            # Adjust contamination based on your expected anomaly rate
            # If you expect around 10% anomalies, use 0.1
            contamination = 0.1
            df_anomalies = detect_anomalies(df_features, contamination=contamination)
            
            # Add original data back
            df_anomalies["line"] = df_parsed["line"]
            df_anomalies["type"] = df_parsed["type"]
            
            # For message if it exists in df_parsed
            if "message" in df_parsed.columns:
                df_anomalies["message"] = df_parsed["message"]
            
            # Filter to show only anomalies and errors
            df_filtered = df_anomalies[
                (df_anomalies["anomaly_score"] == -1) | 
                (df_anomalies["has_error"] == 1)
            ]
            
            # Sort by anomaly probability if available
            if "anomaly_probability" in df_filtered.columns:
                df_filtered = df_filtered.sort_values("anomaly_probability", ascending=False)
            
            # Select columns for display
            display_cols = ["type", "line", "anomaly_score"]
            
            # Add anomaly probability if available
            if "anomaly_probability" in df_filtered.columns:
                display_cols.append("anomaly_probability")
            
            # Save filtered CSV
            df_filtered[display_cols].to_csv("anomalies.csv", index=False)

            # Generate charts
            plt.figure(figsize=(12, 8))
            
            # Plot 1: Message length with anomalies highlighted
            plt.subplot(2, 1, 1)
            colors = df_anomalies["anomaly_score"].map(lambda x: 'red' if x == -1 else 'green')
            plt.bar(df_anomalies.index, df_anomalies["msg_len"], color=colors)
            plt.xlabel("Log Line Index")
            plt.ylabel("Message Length")
            plt.title("📊 Log Message Lengths with Anomaly Highlight")
            
            # Plot 2: Feature importance visualization (if using enhanced features)
            plt.subplot(2, 1, 2)
            
            # Get feature columns excluding non-numeric ones
            feature_cols = [col for col in df_features.columns 
                           if col not in ["line", "type", "message", "anomaly_score", "anomaly_probability"]]
            
            # Calculate average value for each feature in anomalies vs normal
            anomaly_means = df_anomalies[df_anomalies["anomaly_score"] == -1][feature_cols].mean()
            normal_means = df_anomalies[df_anomalies["anomaly_score"] == 1][feature_cols].mean()
            
            # Bar positions
            x = np.arange(len(feature_cols))
            width = 0.35
            
            # Create grouped bar chart
            plt.bar(x - width/2, anomaly_means, width, label='Anomalies')
            plt.bar(x + width/2, normal_means, width, label='Normal')
            
            plt.xlabel('Features')
            plt.ylabel('Average Value')
            plt.title('Feature Comparison: Anomalies vs Normal Logs')
            plt.xticks(x, feature_cols, rotation=45)
            plt.legend()
            
            plt.tight_layout()
            chart_filename = "anomaly_chart.png"
            chart_path = os.path.join("static", chart_filename)
            plt.savefig(chart_path)
            plt.close()

            # Render page
            if df_filtered.empty:
                return render_template("index.html", message="✅ No anomalies or errors detected!", anomalies=None, chart_url=chart_filename)
            else:
                # Include number of anomalies in message
                anomaly_count = len(df_filtered[df_filtered["anomaly_score"] == -1])
                total_count = len(df_anomalies)
                message = f"Found {anomaly_count} anomalies out of {total_count} logs ({anomaly_count/total_count*100:.1f}%)"
                
                return render_template(
                    "index.html",
                    anomalies=df_filtered[display_cols].to_html(classes="table table-striped"),
                    message=message,
                    chart_url=chart_filename
                )
        
        except Exception as e:
            # Handle errors gracefully
            return render_template("index.html", message=f"⚠️ Error processing file: {str(e)}", anomalies=None, chart_url=None)

    # GET request
    return render_template("index.html", anomalies=None, chart_url=None, message=None)

if __name__ == "__main__":
    app.run(debug=True)