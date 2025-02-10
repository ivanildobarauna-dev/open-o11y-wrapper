import os
import logging
from opentelemetry.sdk.resources import Resource, SERVICE_NAME, DEPLOYMENT_ENVIRONMENT
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import OTLPLogExporter
from opentelemetry._logs import set_logger_provider
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import SERVICE_NAME, SERVICE_VERSION, Resource
from ...infrastructure.ports.outbound_logs_exporter import iLogsExporter
from ...domain.dto.application_attributes import ApplicationAttributes

class LogExporterAdapter(iLogsExporter):
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
        self.provider = LoggerProvider(resource=self.resource)
        self.processor = BatchLogRecordProcessor(OTLPLogExporter(endpoint=self.exporter_endpoint))
        self.provider.add_log_record_processor(self.processor)
        set_logger_provider(self.provider)

        self.handler = LoggingHandler(level=logging.DEBUG, logger_provider=self.provider)

        self.logger = logging.getLogger()
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.DEBUG)

    def get_logger(self):
        return self.logger
