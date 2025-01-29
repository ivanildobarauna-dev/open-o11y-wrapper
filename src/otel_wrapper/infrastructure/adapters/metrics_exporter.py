from otel_wrapper.infrastructure.ports.outbound_metrics_exporter import iMetricsExporter


class MetricsExporterAdapter(iMetricsExporter):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def metric_increment(self, name: str, tags: dict): ...
