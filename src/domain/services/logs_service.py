from typing import Type
from src.infrastructure.ports.outbound_logs_exporter import iLogsExporter


class LogsProcessorService:
    def __init__(self, log_exporter: Type[iLogsExporter]):
        self.exporter = log_exporter
