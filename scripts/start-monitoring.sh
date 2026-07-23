#!/bin/bash
echo "🚀 Applying Prometheus & Grafana Stack to Kubernetes..."
kubectl apply -f monitoring/k8s-monitoring.yaml

echo "📡 Starting Telco Prometheus Exporter in background..."
# Gunakan binary python3 langsung dari .venv
./.venv/bin/python3 monitoring/telco_exporter.py &

echo "✅ Monitoring stack up and running!"
