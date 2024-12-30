from src.infrastructure.ports.outbound_metrics_exporter import iMetricsExporter


class MetricsExporterAdapter(iMetricsExporter):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def setup(self): ...
