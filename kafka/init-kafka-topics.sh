#!/bin/bash
echo "🚀 Creating Enterprise Kafka Topics in K8s Cluster..."

KAFKA_BIN="/opt/kafka/bin"

# Buat Topic Utama & DLQ
kubectl exec -i deployment/kafka -- $KAFKA_BIN/kafka-topics.sh --create --if-not-exists --bootstrap-server localhost:9092 --partitions 3 --replication-factor 1 --topic telco.ran.kpi.transformed
kubectl exec -i deployment/kafka -- $KAFKA_BIN/kafka-topics.sh --create --if-not-exists --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1 --topic telco.ran.kpi.dlq

echo "✅ Kafka Topics successfully provisioned:"
kubectl exec -i deployment/kafka -- $KAFKA_BIN/kafka-topics.sh --list --bootstrap-server localhost:9092
