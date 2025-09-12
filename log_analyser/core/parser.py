# core/parser.py

import os
import re
import pandas as pd

# Regex to match timestamps like "2025-03-27 10:00:36"
TIMESTAMP_REGEX = r"^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\s*"

def parse_log_file(file_path):
    """
    Reads a .log or .txt file and returns a DataFrame with 'line' column,
    removing leading timestamps.
    """
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")

    if not (file_path.endswith(".log") or file_path.endswith(".txt")):
        raise ValueError("Only .log or .txt files are supported.")

    log_entries = []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
        for line in file:
            raw_line = line.strip()
            if raw_line:
                # Remove timestamp if present
                cleaned_line = re.sub(TIMESTAMP_REGEX, "", raw_line)
                log_entries.append({"line": cleaned_line})

    return pd.DataFrame(log_entries)
