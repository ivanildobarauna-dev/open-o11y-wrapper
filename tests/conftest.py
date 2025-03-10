import os
import pytest
from unittest.mock import patch, MagicMock

# Import mocks for OpenTelemetry
from tests.mocks import *


@pytest.fixture(autouse=True)
def mock_env_variables():
    """Mock environment variables used in the wrapper."""
    with patch.dict(os.environ, {
        "OTEL_EXPORTER_OTLP_ENDPOINT": "http://test-otel-collector:4317",
        "OTEL_LOG_LEVEL": "INFO",
        "__SCOPE__": "Testing"
    }):
        yield


@pytest.fixture
def mock_tracer():
    """Mock OpenTelemetry tracer."""
    tracer = MagicMock()
    span = MagicMock()
    tracer.start_span.return_value = span
    return tracer


@pytest.fixture
def mock_meter():
    """Mock OpenTelemetry meter."""
    meter = MagicMock()
    counter = MagicMock()
    histogram = MagicMock()
    gauge = MagicMock()
    
    meter.create_counter.return_value = counter
    meter.create_histogram.return_value = histogram
    meter.create_observable_gauge.return_value = gauge
    
    return meter


@pytest.fixture
def mock_logger():
    """Mock Python logger."""
    logger = MagicMock()
    return logger