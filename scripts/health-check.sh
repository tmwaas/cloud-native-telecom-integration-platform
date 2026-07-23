#!/bin/bash
echo "🔍 Running Verbose End-to-End Telecom Platform Health Checks..."
./.venv/bin/python3 -m unittest -v tests/e2e_pipeline_test.py
