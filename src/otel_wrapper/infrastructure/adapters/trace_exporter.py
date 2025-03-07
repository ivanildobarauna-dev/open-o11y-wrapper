import os
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, DEPLOYMENT_ENVIRONMENT
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from ...infrastructure.ports.outbound_trace_exporter import iTracesExporter
from ...domain.dto.application_attributes import ApplicationAttributes

class TraceExporterAdapter(iTracesExporter):
    DEFAULT_ENDPOINT: str = "https://o11y-proxy.ivanildobarauna.dev/"
    _instance = None

    def __new__(cls, application_name: str):
        if cls._instance is None:
            cls._instance = super(TraceExporterAdapter, cls).__new__(cls)
            cls._instance._initialize(application_name)
        return cls._instance

    def _initialize(self, application_name: str):
        self.exporter_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", self.DEFAULT_ENDPOINT)
        self.application_attributes = ApplicationAttributes(application_name=application_name)

        if not isinstance(trace.get_tracer_provider(), TracerProvider):
            self.resource = Resource.create(
                attributes={
                    SERVICE_NAME: self.application_attributes.application_name,
                    DEPLOYMENT_ENVIRONMENT: self.application_attributes.environment,
                }
            )
            self.provider = TracerProvider(resource=self.resource)
            self.processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=self.exporter_endpoint))
            self.provider.add_span_processor(self.processor)
            trace.set_tracer_provider(self.provider)
        else:
            self.provider = trace.get_tracer_provider()

        self._tracer = self.provider.get_tracer(f"host-{self.application_attributes.application_name}")

    def get_tracer(self):
        return self._tracer
