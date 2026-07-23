%dw 2.0
output application/json
var DCR_THRESHOLD = 3.0
---
{
    eventHeader: {
        eventType: "RAN_KPI_TELEMETRY_INGESTION",
        apiVersion: "v2.0",
        processedTimestamp: now()
    },
    telemetryData: payload map (record) -> {
        cellId: record.cellId,
        vendor: record.vendorName,
        metrics: {
            dropCallRate: record.dropCallRatePercent,
            latency: record.latencyMs,
            activeUsers: record.activeUserCount
        },
        status: if (record.dropCallRatePercent > DCR_THRESHOLD) "CRITICAL_ANOMALY" else "NORMAL"
    }
}
