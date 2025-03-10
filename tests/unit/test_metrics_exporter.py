import pytest
from unittest.mock import patch, MagicMock
from otel_wrapper.infrastructure.adapters.metrics_exporter import MetricsExporterAdapter


class TestMetricsExporterAdapter:
    """Test suite for MetricsExporterAdapter."""

    @patch(
        "otel_wrapper.infrastructure.adapters.metrics_exporter.ApplicationAttributes"
    )
    @patch("otel_wrapper.infrastructure.adapters.metrics_exporter.Resource.create")
    @patch(
        "otel_wrapper.infrastructure.adapters.metrics_exporter.PeriodicExportingMetricReader"
    )
    @patch("otel_wrapper.infrastructure.adapters.metrics_exporter.OTLPMetricExporter")
    @patch("otel_wrapper.infrastructure.adapters.metrics_exporter.MeterProvider")
    @patch("otel_wrapper.infrastructure.adapters.metrics_exporter.get_meter")
    def test_initialization(
        self,
        mock_get_meter,
        mock_meter_provider,
        mock_otlp_exporter,
        mock_metric_reader,
        mock_resource_create,
        mock_app_attrs,
    ):
        """Test the initialization of MetricsExporterAdapter."""
        # Setup mocks
        mock_resource = MagicMock()
        mock_resource_create.return_value = mock_resource

        mock_app_attrs_instance = MagicMock()
        mock_app_attrs_instance.application_name = "test-app"
        mock_app_attrs_instance.environment = "Testing"
        mock_app_attrs_instance.endpoints.get_metrics_endpoint.return_value = (
            "http://test-endpoint:4317"
        )
        mock_app_attrs.return_value = mock_app_attrs_instance

        mock_exporter = MagicMock()
        mock_otlp_exporter.return_value = mock_exporter

        mock_reader = MagicMock()
        mock_metric_reader.return_value = mock_reader

        mock_provider = MagicMock()
        mock_meter_provider.return_value = mock_provider

        mock_meter = MagicMock()
        mock_get_meter.return_value = mock_meter

        # Call the singleton's __new__ method
        with patch(
            "otel_wrapper.infrastructure.adapters.metrics_exporter.MetricsExporterAdapter._instance",
            None,
        ):
            adapter = MetricsExporterAdapter(application_name="test-app")

            # Verify the initialization
            mock_app_attrs.assert_called_once_with(application_name="test-app")
            mock_app_attrs_instance.endpoints.get_metrics_endpoint.assert_called_once()
            mock_resource_create.assert_called_once()
            mock_otlp_exporter.assert_called_once_with(
                endpoint="http://test-endpoint:4317", timeout=10
            )
            mock_metric_reader.assert_called_once_with(exporter=mock_exporter)
            mock_meter_provider.assert_called_once_with(
                resource=mock_resource, metric_readers=[mock_reader]
            )
            mock_get_meter.assert_called_once()

            # Verify singleton pattern
            assert MetricsExporterAdapter._instance is not None

            # Create another instance should return the same instance
            adapter2 = MetricsExporterAdapter(application_name="another-app")
            assert adapter is adapter2

    def test_metric_increment(self):
        """Test the metric_increment method."""
        # Setup mock objects
        with patch.object(MetricsExporterAdapter, "_initialize"), patch(
            "otel_wrapper.infrastructure.adapters.metrics_exporter.MetricsExporterAdapter._instance",
            None,
        ):

            adapter = MetricsExporterAdapter(application_name="test-app")
            adapter.meter = MagicMock()
            mock_counter = MagicMock()
            adapter.meter.create_counter.return_value = mock_counter

            # Call metric_increment
            name = "test-counter"
            tags = {"test-key": "test-value"}
            value = 1.5

            adapter.metric_increment(name=name, tags=tags, value=value)

            # Verify the meter was used
            adapter.meter.create_counter.assert_called_once_with(
                name=name, description=f"Counter metric: {name}", unit="1"
            )
            mock_counter.add.assert_called_once_with(amount=value, attributes=tags)

    def test_record_gauge(self):
        """Test the record_gauge method."""
        # Setup mock objects
        with patch.object(MetricsExporterAdapter, "_initialize"), patch(
            "otel_wrapper.infrastructure.adapters.metrics_exporter.MetricsExporterAdapter._instance",
            None,
        ):

            adapter = MetricsExporterAdapter(application_name="test-app")
            adapter.meter = MagicMock()
            mock_gauge = MagicMock()
            adapter.meter.create_observable_gauge.return_value = mock_gauge

            # Call record_gauge
            name = "test-gauge"
            tags = {"test-key": "test-value"}
            value = 42.0

            adapter.record_gauge(name=name, tags=tags, value=value)

            # Verify the meter was used
            adapter.meter.create_observable_gauge.assert_called_once()
            assert name in adapter.meter.create_observable_gauge.call_args[1]["name"]
            assert "1" == adapter.meter.create_observable_gauge.call_args[1]["unit"]

    def test_record_histogram(self):
        """Test the record_histogram method."""
        # Setup mock objects
        with patch.object(MetricsExporterAdapter, "_initialize"), patch(
            "otel_wrapper.infrastructure.adapters.metrics_exporter.MetricsExporterAdapter._instance",
            None,
        ):

            adapter = MetricsExporterAdapter(application_name="test-app")
            adapter.meter = MagicMock()
            mock_histogram = MagicMock()
            adapter.meter.create_histogram.return_value = mock_histogram

            # Call record_histogram
            name = "test-histogram"
            tags = {"test-key": "test-value"}
            value = 0.123

            adapter.record_histogram(name=name, tags=tags, value=value)

            # Verify the meter was used
            adapter.meter.create_histogram.assert_called_once_with(
                name=name, description=f"Histogram metric: {name}", unit="1"
            )
            mock_histogram.record.assert_called_once_with(value, attributes=tags)
