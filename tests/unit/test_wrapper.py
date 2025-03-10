import pytest
from unittest.mock import MagicMock
from otel_wrapper.builder import Wrapper
from otel_wrapper.domain.services.logs_service import LogsProcessorService
from otel_wrapper.domain.services.metrics_service import MetricsProcessorService
from otel_wrapper.domain.services.trace_service import TraceProcessorService


class TestWrapper:
    """Test suite for the Wrapper class."""

    def test_init(self):
        """Test initialization of the wrapper."""
        # Create mock services
        mock_trace_service = MagicMock(spec=TraceProcessorService)
        mock_log_service = MagicMock(spec=LogsProcessorService)
        mock_metrics_service = MagicMock(spec=MetricsProcessorService)

        # Initialize the wrapper
        wrapper = Wrapper(
            trace_service=mock_trace_service,
            log_service=mock_log_service,
            metrics_service=mock_metrics_service,
        )

        # Verify initialization
        assert wrapper._trace_service == mock_trace_service
        assert wrapper._log_service == mock_log_service
        assert wrapper._metrics_service == mock_metrics_service

    def test_traces(self):
        """Test getting the trace service."""
        # Create mock services
        mock_trace_service = MagicMock(spec=TraceProcessorService)
        mock_log_service = MagicMock(spec=LogsProcessorService)
        mock_metrics_service = MagicMock(spec=MetricsProcessorService)

        # Initialize the wrapper
        wrapper = Wrapper(
            trace_service=mock_trace_service,
            log_service=mock_log_service,
            metrics_service=mock_metrics_service,
        )

        # Test getting the trace service
        trace_service = wrapper.traces()

        # Verify the trace service was returned
        assert trace_service == mock_trace_service

    def test_logs(self):
        """Test getting the log service."""
        # Create mock services
        mock_trace_service = MagicMock(spec=TraceProcessorService)
        mock_log_service = MagicMock(spec=LogsProcessorService)
        mock_metrics_service = MagicMock(spec=MetricsProcessorService)

        # Initialize the wrapper
        wrapper = Wrapper(
            trace_service=mock_trace_service,
            log_service=mock_log_service,
            metrics_service=mock_metrics_service,
        )

        # Test getting the log service
        log_service = wrapper.logs()

        # Verify the log service was returned
        assert log_service == mock_log_service

    def test_metrics(self):
        """Test getting the metrics service."""
        # Create mock services
        mock_trace_service = MagicMock(spec=TraceProcessorService)
        mock_log_service = MagicMock(spec=LogsProcessorService)
        mock_metrics_service = MagicMock(spec=MetricsProcessorService)

        # Initialize the wrapper
        wrapper = Wrapper(
            trace_service=mock_trace_service,
            log_service=mock_log_service,
            metrics_service=mock_metrics_service,
        )

        # Test getting the metrics service
        metrics_service = wrapper.metrics()

        # Verify the metrics service was returned
        assert metrics_service == mock_metrics_service
