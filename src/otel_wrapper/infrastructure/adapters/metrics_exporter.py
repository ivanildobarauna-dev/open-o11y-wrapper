import os
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, DEPLOYMENT_ENVIRONMENT
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.metrics import get_meter
from ...infrastructure.ports.outbound_metrics_exporter import iMetricsExporter
from ...domain.dto.application_attributes import ApplicationAttributes

class MetricsExporterAdapter(iMetricsExporter):
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
        self.reader = PeriodicExportingMetricReader(exporter=OTLPMetricExporter(endpoint=self.exporter_endpoint, timeout=1))
        self.provider = MeterProvider(resource=self.resource, metric_readers=[self.reader])
        self.meter = get_meter("meters", meter_provider=self.provider)


    def metric_increment(self, name: str, tags: dict, value: float):
        counter = self.meter.create_counter(
            name=name
            # description="The quantity of requests on method",
            # unit="requests",
        )

        counter.add(amount=value, attributes=tags)
