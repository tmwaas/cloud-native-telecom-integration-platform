import subprocess

print("📥 Consuming latest message from Kafka Topic 'telco.ran.kpi.transformed'...")
cmd = "kubectl exec -i deployment/kafka -- /opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic telco.ran.kpi.transformed --from-beginning --max-messages 1"

result = subprocess.run(cmd, shell=True, capture_output=True, text=True)

print("\n--- RECEIVED KAFKA EVENT PAYLOAD ---")
print(result.stdout)
