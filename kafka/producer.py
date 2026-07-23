import json
import subprocess

payload = {
    "eventHeader": {"eventType": "RAN_KPI_TELEMETRY_INGESTION", "apiVersion": "v2.0"},
    "telemetryData": [
        {"cellId": "DELFT-5G-01", "vendor": "Ericsson", "metrics": {"dropCallRate": 0.42, "latency": 12}, "status": "NORMAL"},
        {"cellId": "DELFT-5G-02", "vendor": "Huawei", "metrics": {"dropCallRate": 1.12, "latency": 18}, "status": "NORMAL"},
        {"cellId": "DELFT-5G-03", "vendor": "Ericsson", "metrics": {"dropCallRate": 4.92, "latency": 85}, "status": "CRITICAL_ANOMALY"},
        {"cellId": "DELFT-5G-04", "vendor": "Nokia", "metrics": {"dropCallRate": 0.65, "latency": 14}, "status": "NORMAL"}
    ]
}

print("📡 Publishing Transformed Telemetry Stream to Kafka Topic 'telco.ran.kpi.transformed'...")
json_str = json.dumps(payload)

cmd = f"echo '{json_str}' | kubectl exec -i deployment/kafka -- /opt/kafka/bin/kafka-console-producer.sh --bootstrap-server localhost:9092 --topic telco.ran.kpi.transformed"

subprocess.run(cmd, shell=True, check=True)
print("✅ Payload successfully published to Kafka Event Bus!")
