"""Performance and latency integration benchmarks for wrap_client."""

from __future__ import annotations

import time

import botocore.session

from aws_resource_validator.client_wrapper.validator import ShapeValidator


def test_validation_latency_sub_millisecond() -> None:
    session = botocore.session.get_session()
    client = session.create_client("s3", region_name="us-east-1")
    op = client.meta.service_model.operation_model("CreateBucket")

    validator = ShapeValidator()
    # Warm up cache
    validator.validate_operation_parameters("s3", op, {"Bucket": "warmup-bucket-1"})

    iterations = 1000
    start = time.perf_counter()
    for i in range(iterations):
        validator.validate_operation_parameters("s3", op, {"Bucket": f"test-valid-bucket-{i}"})
    duration = time.perf_counter() - start

    avg_ms = (duration / iterations) * 1000
    print(f"\nAverage validation latency: {avg_ms:.4f} ms per call")

    # Assert average latency is strictly under 0.2ms (typically <0.02ms)
    assert avg_ms < 0.2, f"Validation too slow: {avg_ms:.4f} ms per call"
