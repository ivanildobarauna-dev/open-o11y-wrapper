from abc import ABC, abstractmethod


class iMetricsExporter(ABC):
    @abstractmethod
    def metric_increment(self, name: str, tags: dict):
        pass
