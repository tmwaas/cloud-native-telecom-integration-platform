import time
from prometheus_client import start_http_server, Gauge

DCR_GAUGE = Gauge('telco_drop_call_rate_percent', 'Drop Call Rate percentage per cell', ['cell_id', 'vendor'])
LATENCY_GAUGE = Gauge('telco_cell_latency_ms', 'Cell latency in milliseconds', ['cell_id', 'vendor'])

def update_metrics():
    # Metrics injection matching Phase 1-4 data
    cells = [
        {"cell_id": "DELFT-5G-01", "vendor": "Ericsson", "dcr": 0.42, "latency": 12},
        {"cell_id": "DELFT-5G-02", "vendor": "Huawei", "dcr": 1.12, "latency": 18},
        {"cell_id": "DELFT-5G-03", "vendor": "Ericsson", "dcr": 4.92, "latency": 85},
        {"cell_id": "DELFT-5G-04", "vendor": "Nokia", "dcr": 0.65, "latency": 14}
    ]
    for cell in cells:
        DCR_GAUGE.labels(cell_id=cell["cell_id"], vendor=cell["vendor"]).set(cell["dcr"])
        LATENCY_GAUGE.labels(cell_id=cell["cell_id"], vendor=cell["vendor"]).set(cell["latency"])

if __name__ == '__main__':
    start_http_server(8000)
    print("📡 Prometheus Telco Exporter running on port :8000...")
    while True:
        update_metrics()
        time.sleep(5)
