"""Deployment smoke test.

This test is intended to be run against a deployed instance (e.g., after
deployment). It sends an HTTP GET to http://localhost:5000/health and asserts
that the service returns status 200 and body "OK".

The test uses the standard library only and performs a few short retries to
be more reliable when the service is starting up.
"""

import time
import pytest
from urllib.request import urlopen

# Mark this module as deployment-only so CI doesn't run it during commit/unit stages
pytestmark = pytest.mark.deployment


def test_health_endpoint_deployed():
    url = "http://localhost:5000/health"
    attempts = 5
    delay = 0.2  # seconds between retries

    last_exc = None
    for _ in range(attempts):
        try:
            resp = urlopen(url, timeout=2)
            status = resp.getcode()
            body = resp.read().decode()

            assert status == 200
            assert body == "OK"
            return
        except Exception as exc:
            last_exc = exc
            time.sleep(delay)

    assert False, f"Failed to get healthy response from {url}: {last_exc}"
