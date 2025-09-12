import pandas as pd
from sklearn.ensemble import IsolationForest
from core.parser import parse_log_file
from core.preprocessor import preprocess_features  

def detect_anomalies(df_features, contamination=0.05):
    """
    Detects anomalies in the log feature data using Isolation Forest.
    
    Args:
        df_features (pd.DataFrame): DataFrame with enhanced features including:
            'type_code', 'msg_len', 'has_error', 'has_failure', 'has_exception',
            'is_unauthorized', 'is_connection_issue', 'message_frequency', 'has_number'
        contamination (float): The percentage of anomalies to expect (default is 5%)
    
    Returns:
        pd.DataFrame: DataFrame with original features and new column 'anomaly_score'
                      -1 = anomaly, 1 = normal
    """
    # Create a copy of the dataframe to avoid modifying the original
    df_features = df_features.copy()
    
    # Initialize the Isolation Forest model
    model = IsolationForest(
        n_estimators=100,          # Number of trees in the forest
        contamination=contamination, # Expected % of anomalies
        random_state=42,           # For reproducibility
        max_samples='auto'         # Size of the subsamples
    )
    
    # Fit the model and predict anomalies
    # The fit_predict method returns 1 for normal points and -1 for anomalies
    df_features["anomaly_score"] = model.fit_predict(df_features)
    
    # Optional: Add an anomaly probability score (lower = more anomalous)
    # This requires scikit-learn 0.22 or later
    try:
        df_features["anomaly_probability"] = -model.score_samples(df_features)
    except:
        pass  # Skip if using older scikit-learn version
    
    return df_features

# Optional: standalone usage
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python core/anomaly_detector.py <log_or_txt_file>")
        sys.exit(1)
    
    log_file_path = sys.argv[1]
    
    print("[🔁] Parsing logs...")
    df = parse_log_file(log_file_path)
    
    print("[⚙️] Preprocessing features...")
    df_features = preprocess_features(df)
    
    print("[🤖] Running anomaly detection...")
    # You might want to adjust contamination based on your expected anomaly rate
    # If about 10% of logs are anomalies, use contamination=0.1
    df_anomalies = detect_anomalies(df_features, contamination=0.1)
    
    print("[📉] Detected Anomalies:")
    anomalies = df_anomalies[df_anomalies["anomaly_score"] == -1]
    
    # Show full information for detected anomalies
    if not anomalies.empty:
        # Join back with original data to see the full log messages
        if 'line' in df.columns:
            anomalies = anomalies.merge(
                df[['line']], 
                left_index=True, 
                right_index=True
            )
        
        # Display top anomalies, sorted by probability if available
        if 'anomaly_probability' in anomalies.columns:
            anomalies = anomalies.sort_values('anomaly_probability', ascending=False)
        
        print(anomalies)
        print(f"Found {len(anomalies)} anomalies out of {len(df_features)} logs ({len(anomalies)/len(df_features)*100:.2f}%)")
    else:
        print("No anomalies detected!")
    
    # Save results to CSV
    df_anomalies.to_csv("detected_anomalies.csv", index=False)
    print("[💾] Results saved to detected_anomalies.csv")