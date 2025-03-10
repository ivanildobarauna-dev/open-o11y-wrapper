import pytest
from unittest.mock import MagicMock
from otel_wrapper.domain.services.metrics_service import MetricsProcessorService


class TestMetricsProcessorService:
    """Test suite for MetricsProcessorService."""

    def test_init(self):
        """Test initialization of metrics service."""
        # Create a mock metrics exporter
        mock_exporter = MagicMock()

        # Initialize the service
        service = MetricsProcessorService(metric_exporter=mock_exporter)

        # Verify initialization
        assert service._exporter == mock_exporter

    def test_metric_increment(self):
        """Test incrementing a metric."""
        # Create a mock metrics exporter
        mock_exporter = MagicMock()

        # Initialize the service
        service = MetricsProcessorService(metric_exporter=mock_exporter)

        # Test incrementing a metric
        name = "test-counter"
        tags = {"test-key": "test-value"}
        value = 1.5

        service.metric_increment(name=name, tags=tags, value=value)

        # Verify the exporter was called
        mock_exporter.metric_increment.assert_called_once_with(
            name=name, tags=tags, value=value
        )

    def test_metric_increment_default_value(self):
        """Test incrementing a metric with default value."""
        # Create a mock metrics exporter
        mock_exporter = MagicMock()

        # Initialize the service
        service = MetricsProcessorService(metric_exporter=mock_exporter)

        # Test incrementing a metric with default value
        name = "test-counter"
        tags = {"test-key": "test-value"}

        service.metric_increment(name=name, tags=tags)

        # Verify the exporter was called with default value of 1.0
        mock_exporter.metric_increment.assert_called_once_with(
            name=name, tags=tags, value=1.0
        )

    def test_record_gauge(self):
        """Test recording a gauge value."""
        # Create a mock metrics exporter
        mock_exporter = MagicMock()

        # Initialize the service
        service = MetricsProcessorService(metric_exporter=mock_exporter)

        # Test recording a gauge value
        name = "test-gauge"
        tags = {"test-key": "test-value"}
        value = 42.0

        service.record_gauge(name=name, tags=tags, value=value)

        # Verify the exporter was called
        mock_exporter.record_gauge.assert_called_once_with(
            name=name, tags=tags, value=value
        )

    def test_record_histogram(self):
        """Test recording a histogram value."""
        # Create a mock metrics exporter
        mock_exporter = MagicMock()

        # Initialize the service
        service = MetricsProcessorService(metric_exporter=mock_exporter)

        # Test recording a histogram value
        name = "test-histogram"
        tags = {"test-key": "test-value"}
        value = 0.123

        service.record_histogram(name=name, tags=tags, value=value)

        # Verify the exporter was called
        mock_exporter.record_histogram.assert_called_once_with(
            name=name, tags=tags, value=value
        )
