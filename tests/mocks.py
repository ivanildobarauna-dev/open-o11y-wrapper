"""
Mock classes for OpenTelemetry modules for testing.
"""

import sys
from types import ModuleType
from unittest.mock import MagicMock


# Create module structure
class MockModule(ModuleType):
    """A mock module that allows arbitrary attributes."""

    def __init__(self, name):
        super().__init__(name)
        self.__dict__["_mock_dict"] = {}

    def __getattr__(self, key):
        if key not in self._mock_dict:
            self._mock_dict[key] = MagicMock()
        return self._mock_dict[key]

    def __setattr__(self, key, value):
        self._mock_dict[key] = value


# Mock the base modules
opentelemetry = MockModule("opentelemetry")
opentelemetry.sdk = MockModule("opentelemetry.sdk")
opentelemetry.trace = MockModule("opentelemetry.trace")
opentelemetry.metrics = MockModule("opentelemetry.metrics")
opentelemetry._logs = MockModule("opentelemetry._logs")
opentelemetry.context = MockModule("opentelemetry.context")
opentelemetry.baggage = MockModule("opentelemetry.baggage")
opentelemetry.exporter = MockModule("opentelemetry.exporter")

# Mock sub-modules
opentelemetry.sdk.trace = MockModule("opentelemetry.sdk.trace")
opentelemetry.sdk.metrics = MockModule("opentelemetry.sdk.metrics")
opentelemetry.sdk._logs = MockModule("opentelemetry.sdk._logs")
opentelemetry.sdk.resources = MockModule("opentelemetry.sdk.resources")
opentelemetry.sdk.trace.export = MockModule("opentelemetry.sdk.trace.export")
opentelemetry.sdk.metrics.export = MockModule("opentelemetry.sdk.metrics.export")
opentelemetry.sdk._logs.export = MockModule("opentelemetry.sdk._logs.export")
opentelemetry.trace.propagation = MockModule("opentelemetry.trace.propagation")
opentelemetry.trace.propagation.tracecontext = MockModule(
    "opentelemetry.trace.propagation.tracecontext"
)
opentelemetry.baggage.propagation = MockModule("opentelemetry.baggage.propagation")
opentelemetry.exporter.otlp = MockModule("opentelemetry.exporter.otlp")
opentelemetry.exporter.otlp.proto = MockModule("opentelemetry.exporter.otlp.proto")
opentelemetry.exporter.otlp.proto.grpc = MockModule(
    "opentelemetry.exporter.otlp.proto.grpc"
)
opentelemetry.exporter.otlp.proto.grpc.trace_exporter = MockModule(
    "opentelemetry.exporter.otlp.proto.grpc.trace_exporter"
)
opentelemetry.exporter.otlp.proto.grpc.metric_exporter = MockModule(
    "opentelemetry.exporter.otlp.proto.grpc.metric_exporter"
)
opentelemetry.exporter.otlp.proto.grpc._log_exporter = MockModule(
    "opentelemetry.exporter.otlp.proto.grpc._log_exporter"
)

# Add constants
opentelemetry.sdk.resources.SERVICE_NAME = "service.name"
opentelemetry.sdk.resources.DEPLOYMENT_ENVIRONMENT = "deployment.environment"
opentelemetry.sdk.resources.SERVICE_VERSION = "service.version"


# Add enum values for SpanKind
class MockSpanKind:
    INTERNAL = "internal"
    SERVER = "server"
    CLIENT = "client"
    PRODUCER = "producer"
    CONSUMER = "consumer"


opentelemetry.trace.SpanKind = MockSpanKind


# Add specific classes
class MockTracer:
    def __init__(self, *args, **kwargs):
        pass

    def start_span(self, name, kind=None, attributes=None):
        span = MagicMock()
        span.name = name
        return span

    def get_current_span(self):
        return MagicMock()


# Add classes to the modules
opentelemetry.sdk.trace.TracerProvider = MagicMock()
opentelemetry.sdk.trace.Tracer = MockTracer
opentelemetry.sdk.resources.Resource = MagicMock()
opentelemetry.sdk.resources.Resource.create = MagicMock(return_value=MagicMock())
opentelemetry.sdk.trace.export.BatchSpanProcessor = MagicMock()
opentelemetry.exporter.otlp.proto.grpc.trace_exporter.OTLPSpanExporter = MagicMock()
opentelemetry.exporter.otlp.proto.grpc.metric_exporter.OTLPMetricExporter = MagicMock()
opentelemetry.exporter.otlp.proto.grpc._log_exporter.OTLPLogExporter = MagicMock()
opentelemetry.sdk.metrics.export.PeriodicExportingMetricReader = MagicMock()
opentelemetry.sdk.metrics.MeterProvider = MagicMock()
opentelemetry.metrics.get_meter = MagicMock(return_value=MagicMock())
opentelemetry._logs.set_logger_provider = MagicMock()
opentelemetry.sdk._logs.LoggerProvider = MagicMock()
opentelemetry.sdk._logs.LoggingHandler = MagicMock()
opentelemetry.sdk._logs.export.BatchLogRecordProcessor = MagicMock()
opentelemetry.trace.set_tracer_provider = MagicMock()
opentelemetry.trace.get_tracer_provider = MagicMock(return_value=MagicMock())
opentelemetry.trace.set_span_in_context = MagicMock()
opentelemetry.trace.propagation.tracecontext.TraceContextTextMapPropagator = MagicMock
opentelemetry.baggage.propagation.W3CBaggagePropagator = MagicMock

# Register the mocks in sys.modules
sys.modules["opentelemetry"] = opentelemetry
sys.modules["opentelemetry.sdk"] = opentelemetry.sdk
sys.modules["opentelemetry.trace"] = opentelemetry.trace
sys.modules["opentelemetry.metrics"] = opentelemetry.metrics
sys.modules["opentelemetry._logs"] = opentelemetry._logs
sys.modules["opentelemetry.context"] = opentelemetry.context
sys.modules["opentelemetry.baggage"] = opentelemetry.baggage
sys.modules["opentelemetry.exporter"] = opentelemetry.exporter
sys.modules["opentelemetry.sdk.trace"] = opentelemetry.sdk.trace
sys.modules["opentelemetry.sdk.metrics"] = opentelemetry.sdk.metrics
sys.modules["opentelemetry.sdk._logs"] = opentelemetry.sdk._logs
sys.modules["opentelemetry.sdk.resources"] = opentelemetry.sdk.resources
sys.modules["opentelemetry.sdk.trace.export"] = opentelemetry.sdk.trace.export
sys.modules["opentelemetry.sdk.metrics.export"] = opentelemetry.sdk.metrics.export
sys.modules["opentelemetry.sdk._logs.export"] = opentelemetry.sdk._logs.export
sys.modules["opentelemetry.trace.propagation"] = opentelemetry.trace.propagation
sys.modules["opentelemetry.trace.propagation.tracecontext"] = (
    opentelemetry.trace.propagation.tracecontext
)
sys.modules["opentelemetry.baggage.propagation"] = opentelemetry.baggage.propagation
sys.modules["opentelemetry.exporter.otlp"] = opentelemetry.exporter.otlp
sys.modules["opentelemetry.exporter.otlp.proto"] = opentelemetry.exporter.otlp.proto
sys.modules["opentelemetry.exporter.otlp.proto.grpc"] = (
    opentelemetry.exporter.otlp.proto.grpc
)
sys.modules["opentelemetry.exporter.otlp.proto.grpc.trace_exporter"] = (
    opentelemetry.exporter.otlp.proto.grpc.trace_exporter
)
sys.modules["opentelemetry.exporter.otlp.proto.grpc.metric_exporter"] = (
    opentelemetry.exporter.otlp.proto.grpc.metric_exporter
)
sys.modules["opentelemetry.exporter.otlp.proto.grpc._log_exporter"] = (
    opentelemetry.exporter.otlp.proto.grpc._log_exporter
)
