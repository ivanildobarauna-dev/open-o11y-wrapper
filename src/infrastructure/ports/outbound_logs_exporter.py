from abc import ABC, abstractmethod


class iLogsExporter(ABC):
    @abstractmethod
    def send_log():
        pass
