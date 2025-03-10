import pytest
from unittest.mock import MagicMock, patch
from otel_wrapper.domain.services.trace_service import TraceProcessorService


# Mock SpanKind since we might not have OpenTelemetry installed during tests
class MockSpanKind:
    INTERNAL = "internal"
    SERVER = "server"
    CLIENT = "client"
    PRODUCER = "producer"
    CONSUMER = "consumer"


# Use the mock
SpanKind = MockSpanKind


class TestTraceProcessorService:
    """Test suite for TraceProcessorService."""

    def test_init(self, mock_tracer):
        """Test initialization of trace service."""
        # Create a mock trace exporter
        mock_exporter = MagicMock()
        mock_exporter.get_tracer.return_value = mock_tracer

        # Initialize the service
        service = TraceProcessorService(trace_exporter=mock_exporter)

        # Verify initialization
        assert service._exporter == mock_exporter
        assert service._tracer == mock_tracer

    def test_new_span(self, mock_tracer):
        """Test creating a new span."""
        # Create a mock trace exporter
        mock_exporter = MagicMock()
        mock_exporter.get_tracer.return_value = mock_tracer

        # Initialize the service
        service = TraceProcessorService(trace_exporter=mock_exporter)

        # Test creating a span
        span = service.new_span("test-span")

        # Verify span creation
        mock_tracer.start_span.assert_called_once_with(
            name="test-span", kind=SpanKind.INTERNAL, attributes={}
        )
        assert span == mock_tracer.start_span.return_value

    def test_new_span_with_attributes(self, mock_tracer):
        """Test creating a new span with attributes."""
        # Create a mock trace exporter
        mock_exporter = MagicMock()
        mock_exporter.get_tracer.return_value = mock_tracer

        # Initialize the service
        service = TraceProcessorService(trace_exporter=mock_exporter)

        # Test creating a span with attributes
        attributes = {"test-key": "test-value"}
        span = service.new_span("test-span", attributes=attributes)

        # Verify span creation with attributes
        mock_tracer.start_span.assert_called_once_with(
            name="test-span", kind=SpanKind.INTERNAL, attributes=attributes
        )
        assert span == mock_tracer.start_span.return_value

    def test_span_in_context(self, mock_tracer):
        """Test using a span as a context manager."""
        # Create mock objects
        mock_exporter = MagicMock()
        mock_exporter.get_tracer.return_value = mock_tracer
        mock_span = MagicMock()
        mock_tracer.start_span.return_value = mock_span

        # Initialize the service
        service = TraceProcessorService(trace_exporter=mock_exporter)

        # Use the context manager
        with patch(
            "otel_wrapper.domain.services.trace_service.set_span_in_context"
        ) as mock_set_context:
            mock_context = MagicMock()
            mock_set_context.return_value.__enter__.return_value = mock_context

            with service.span_in_context("test-context-span") as (span, context):
                assert span == mock_span
                assert context == mock_context

            # Verify the span was ended
            mock_span.end.assert_called_once()

    def test_inject_context_into_headers(self):
        """Test injecting trace context into headers."""
        # Create mock objects
        mock_exporter = MagicMock()
        mock_tracer = MagicMock()
        mock_exporter.get_tracer.return_value = mock_tracer

        # Initialize the service
        service = TraceProcessorService(trace_exporter=mock_exporter)

        # Mock the propagators
        service._trace_context_propagator = MagicMock()
        service._baggage_propagator = MagicMock()

        # Test injecting context
        headers = {}
        context = MagicMock()

        result = service.inject_context_into_headers(headers, context)

        # Verify the propagators were called
        service._trace_context_propagator.inject.assert_called_once_with(
            carrier=headers, context=context
        )
        service._baggage_propagator.inject.assert_called_once_with(
            carrier=headers, context=context
        )
        assert result == headers

    def test_extract_context_from_headers(self):
        """Test extracting trace context from headers."""
        # Create mock objects
        mock_exporter = MagicMock()
        mock_tracer = MagicMock()
        mock_exporter.get_tracer.return_value = mock_tracer

        # Initialize the service
        service = TraceProcessorService(trace_exporter=mock_exporter)

        # Mock the propagators
        service._trace_context_propagator = MagicMock()
        service._baggage_propagator = MagicMock()

        extracted_context1 = MagicMock()
        extracted_context2 = MagicMock()
        service._trace_context_propagator.extract.return_value = extracted_context1
        service._baggage_propagator.extract.return_value = extracted_context2

        # Test extracting context
        headers = {
            "traceparent": "00-0af7651916cd43dd8448eb211c80319c-b7ad6b7169203331-01"
        }

        result = service.extract_context_from_headers(headers)

        # Verify the propagators were called
        service._trace_context_propagator.extract.assert_called_once_with(
            carrier=headers
        )
        service._baggage_propagator.extract.assert_called_once_with(
            carrier=headers, context=extracted_context1
        )
        assert result == extracted_context2
