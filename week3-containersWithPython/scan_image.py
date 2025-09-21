import subprocess
import json
import argparse
from datetime import datetime

def scan_image(image_name):
    try:
        print(f"scanning image:{image_name}")
        result=subprocess.run(["trivy","image","--quiet","--format","json",image_name],capture_output=True, text=True, check=True)
        return json.loads(result.stdout)
    except subprocess.CalledProcessError as e:
        print("error: running trivy", e.stderr)
        return None 
def save_report(data,image_name):
    timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_name=f"scan-report-of-{image_name}-{timestamp}.json"
    with open(file_name,"w") as f:
        json.dump(data,f,indent=4)
    print(f"full scan report saved in {file_name}")

def parse_result(data):
    if not data:
        print("No scan data to analyse")
        return        
    
    total_critical=0
    total_high=0
    crtical_vuln=[]
    
    print("\n vulnerability summary")
    for target in data.get("Results",[]):
        for vuln in target.get("Vulnerabilities",[]):
            severity=vuln.get("Severity","").lower()
            if severity=="critical":
                total_critical+=1
                crtical_vuln.append(vuln)
            elif severity=="high":
                total_high+=1
    print("critical: {total_critical}")
    print("high: {total_high}")
    
    if total_critical>0:
        print("\n detailed critical vulnerabilties:")
        for v in crtical_vuln:
            print(f"{v['PkgName']}:{v['InstalledVersion']}")
            print(f"{v['Title']}:{v['Description']}")
            print(f"Severity:{v['Severity']}")                    
            
if __name__=="__main__":
    parser=argparse.ArgumentParser(description="scan docker images to check vulnerabitly in trivy")
    parser.add_argument("--image",required=True,help="docker image name")
    args=parser.parse_args()
    
    results=scan_image(args.image)
    if results:
        parse_result(results)
        save_report(results,args.image)