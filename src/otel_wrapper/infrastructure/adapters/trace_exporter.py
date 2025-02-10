import os
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, DEPLOYMENT_ENVIRONMENT
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace import get_tracer, set_tracer_provider
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from ...infrastructure.ports.outbound_trace_exporter import iTracesExporter
from ...domain.dto.application_attributes import ApplicationAttributes


class TraceExporterAdapter(iTracesExporter):
    DEFAULT_ENDPOINT: str = "https://o11y-proxy.ivanildobarauna.dev/"

    def __init__(self, application_name: str):
        self.exporter_endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", self.DEFAULT_ENDPOINT)
        self.application_atrributes = ApplicationAttributes(
            application_name=application_name
        )
        self.resource = Resource.create(
            attributes={
                SERVICE_NAME: self.application_atrributes.application_name,
                DEPLOYMENT_ENVIRONMENT: self.application_atrributes.environment,
            }
        )
        self.provider = TracerProvider(resource=self.resource)
        self.processor = BatchSpanProcessor(OTLPSpanExporter(endpoint=self.exporter_endpoint))
        self.provider.add_span_processor(self.processor)
        set_tracer_provider(self.provider)

    def get_tracer(self):
        return get_tracer(
            "host-" + self.application_atrributes.application_name,
        )
        
    
        
