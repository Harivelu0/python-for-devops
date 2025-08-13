import os 
import glob
from collections import defaultdict

log_dir="/var/log/"
log_files=glob.glob(os.path.join(log_dir,"*.log"))

print("available files are:")
for file in log_files:
    print(file)
    
log_file_path="/var/log/syslog"
keywords=["ERROR","WARNING","FAILED","INVALID"]
keywords_count=defaultdict(int)


with open(log_file_path,"r") as f:
    for line in f:
        for keyword in keywords:
            if keyword in line:
                keywords_count[keyword]+=1
report_path="log_report.txt"
with open(report_path,"w") as report:
    report.write("Log summary")
    report.write("\n************\n")
    for keyword,count in keywords_count.items():
        report.write(f"{keyword}:{count}\n")
        
print(f"\n LOG analysed completed successfully file saved in {report_path}")
    
