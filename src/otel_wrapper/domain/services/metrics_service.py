from typing import Type
from ...infrastructure.ports.outbound_metrics_exporter import iMetricsExporter


class MetricsProcessorService:
    def __init__(self, metric_exporter: Type[iMetricsExporter]):
        self._exporter = metric_exporter

    def metric_increment(self, name: str, tags: dict, value: float):
        self._exporter.metric_increment(name=name, tags=tags, value=value)
