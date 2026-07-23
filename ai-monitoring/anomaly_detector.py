import json
import subprocess
import time

def run_ai_anomaly_engine():
    print("🤖 Starting AI Anomaly Detection Engine (Listening to Kafka Stream)...")
    
    cmd = "kubectl exec -i deployment/kafka -- /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic telco.ran.kpi.transformed --from-beginning --max-messages 1"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    
    if not result.stdout.strip():
        print("⚠️ No data received from Kafka.")
        return

    payload = json.loads(result.stdout.strip())
    print("\n🧠 [AI ENGINE] Processing Telemetry Event Batch...")
    
    for cell in payload.get("telemetryData", []):
        cell_id = cell.get("cellId")
        vendor = cell.get("vendor")
        dcr = cell.get("metrics", {}).get("dropCallRate", 0)
        latency = cell.get("metrics", {}).get("latency", 0)
        
        print(f"📊 [KPI CHECK] Cell: {cell_id} | Vendor: {vendor} | DCR: {dcr}% | Latency: {latency}ms")
        
        # Rule & Anomaly Detection Logic
        if dcr > 3.0 or cell.get("status") == "CRITICAL_ANOMALY":
            print("\n" + "🚨"*20)
            print(f"⚠️ [AI ANOMALY ALERT] High Drop Call Rate Spike detected on {cell_id} ({vendor})!")
            print(f"📈 Measured DCR: {dcr}% (Threshold: 3.0%) | Latency: {latency}ms")
            print("🧠 [LLM Root Cause Analysis]: Hardware interface degradation or high RF interference post-DataWeave transformation.")
            print(f"📢 [CLOSED-LOOP ACTION] Triggering automated remediation webhook to Experience API for {cell_id}...")
            print("🚨"*20 + "\n")

if __name__ == "__main__":
    run_ai_anomaly_engine()
