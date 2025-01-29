from typing import Type
from src.otel_wrapper.infrastructure.ports.outbound_logs_exporter import iLogsExporter


class LogsProcessorService:
    def __init__(self, log_exporter: Type[iLogsExporter]):
        self.exporter = log_exporter
    
    def send_log(self):
        ...
