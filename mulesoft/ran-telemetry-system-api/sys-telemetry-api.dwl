%dw 2.0
output application/json
---
payload map (item) -> {
    cellId: item.cell_id,
    vendorName: item.vendor,
    dropCallRatePercent: item.drop_call_rate as Number,
    latencyMs: item.latency_ms as Number,
    activeUserCount: item.active_users as Number,
    isCriticalFlag: item.is_critical
}
