from flask import Flask,jsonify,request
import psutil

app=Flask(__name__)
@app.route("/")
def index():
    return jsonify({
        "status": "API is running to get the system metrices checkout /metrics"
    })
@app.route("/metrics")
def metrics():
    cpu=psutil.cpu_percent(interval=1)
    memory=psutil.virtual_memory().percent
    return jsonify({
        "cpu_usage":f"{cpu}%",
        "memory_usage":f"{memory}%"
    
    })
    
if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000)    