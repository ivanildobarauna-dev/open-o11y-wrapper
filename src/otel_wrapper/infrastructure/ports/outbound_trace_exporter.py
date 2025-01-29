from abc import ABC, abstractmethod


class iTracesExporter(ABC):
    @abstractmethod
    def get_tracer(self):
        pass
