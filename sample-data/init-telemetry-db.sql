CREATE TABLE IF NOT EXISTS multi_vendor_cell_kpis (
    id SERIAL PRIMARY KEY,
    cell_id VARCHAR(50) NOT NULL,
    vendor VARCHAR(50) NOT NULL,
    drop_call_rate NUMERIC(5,2),
    latency_ms INT,
    active_users INT,
    is_critical BOOLEAN DEFAULT false,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

TRUNCATE TABLE multi_vendor_cell_kpis;

INSERT INTO multi_vendor_cell_kpis (cell_id, vendor, drop_call_rate, latency_ms, active_users, is_critical) VALUES
('DELFT-5G-01', 'Ericsson', 0.42, 12, 1420, false),
('DELFT-5G-02', 'Huawei', 1.12, 18, 890, false),
('DELFT-5G-03', 'Ericsson', 4.92, 85, 3100, true),
('DELFT-5G-04', 'Nokia', 0.65, 14, 1150, false);
