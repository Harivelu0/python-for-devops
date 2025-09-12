import pandas as pd
import re
from collections import Counter

def preprocess_features(df):
    """
    Enhanced preprocessing for anomaly detection in logs.
    """
    # Basic type detection
    def detect_type(log_line):
        if "ERROR" in log_line:
            return "ERROR"
        elif "WARNING" in log_line:
            return "WARNING"
        elif "SUMMARY" in log_line:
            return "SUMMARY"
        elif "INFO" in log_line:
            return "INFO"
        else:
            return "INFO"  # default
    
    df["type"] = df["line"].apply(detect_type)
    
    # Extract message content
    def extract_message(log_line):
        parts = log_line.split()
        if len(parts) > 2:
            return " ".join(parts[2:])
        return ""
    
    df["message"] = df["line"].apply(extract_message)
    
    # Enhanced features
    # 1. Basic type encoding
    mapping = {
        "ERROR": 0,
        "WARNING": 1,
        "INFO": 2,
        "SUMMARY": 3
    }
    df["type_code"] = df["type"].map(mapping)
    
    # 2. Message-based features
    df["has_failure"] = df["message"].apply(lambda x: 1 if re.search(r'fail(ed|ure)?', x.lower()) else 0)
    df["has_exception"] = df["message"].apply(lambda x: 1 if "exception" in x.lower() else 0)
    df["is_unauthorized"] = df["message"].apply(lambda x: 1 if "unauthorized" in x.lower() else 0)
    df["is_connection_issue"] = df["message"].apply(lambda x: 1 if any(term in x.lower() for term in ["connection", "network", "latency"]) else 0)
    
    # 3. Frequency-based features (rare messages are more likely to be anomalies)
    message_counts = Counter(df["message"])
    df["message_frequency"] = df["message"].apply(lambda x: message_counts[x])
    
    # 4. Derived metrics
    df["msg_len"] = df["message"].apply(len)
    df["has_error"] = df["type"].apply(lambda x: 1 if x == "ERROR" else 0)
    df["has_number"] = df["message"].apply(lambda x: 1 if re.search(r'\d+', x) else 0)
    
    selected_cols = ["type_code", "msg_len", "has_error", "has_failure", 
                     "has_exception", "is_unauthorized", "is_connection_issue", 
                     "message_frequency", "has_number"]
    
    return df[selected_cols]