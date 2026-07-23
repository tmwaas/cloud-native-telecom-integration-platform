import subprocess
import unittest

class TestTelecomIntegrationPlatform(unittest.TestCase):

    def test_01_postgres_telemetry_db(self):
        """[DB] Verify Postgres Multi-Vendor Telemetry Table Ingestion"""
        cmd = "kubectl exec -i deployment/postgres -- psql -U postgres -d telco_telemetry -c 'SELECT cell_id, vendor, drop_call_rate FROM multi_vendor_cell_kpis;'"
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("\n--- 1. POSTGRES DATABASE OUTPUT ---")
        print(res.stdout.strip())
        self.assertIn("DELFT-5G-03", res.stdout)
        self.assertIn("4", res.stdout)

    def test_02_kafka_topic_existence(self):
        """[KAFKA] Verify Kafka Event Streaming Topics Provisioning"""
        cmd = "kubectl exec -i deployment/kafka -- /opt/kafka/bin/kafka-topics.sh --list --bootstrap-server localhost:9092"
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("\n--- 2. KAFKA TOPICS OUTPUT ---")
        print(res.stdout.strip())
        self.assertIn("telco.ran.kpi.transformed", res.stdout)

    def test_03_monitoring_stack_pods(self):
        """[K8S] Verify Prometheus & Grafana Monitoring Pods Status"""
        cmd = "kubectl get pods -l 'app in (prometheus, grafana)'"
        res = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print("\n--- 3. KUBERNETES MONITORING PODS ---")
        print(res.stdout.strip())
        self.assertIn("Running", res.stdout)

if __name__ == "__main__":
    unittest.main()
