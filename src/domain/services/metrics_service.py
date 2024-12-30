from typing import Type
from src.infrastructure.ports.outbound_metrics_exporter import iMetricsExporter


class MetricsProcessorService:
    def __init__(self, metric_exporter: Type[iMetricsExporter]):
        self.exporter = metric_exporter
