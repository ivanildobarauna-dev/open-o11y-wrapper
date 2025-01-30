from typing import Type
from ...infrastructure.ports.outbound_logs_exporter import iLogsExporter


class LogsProcessorService:
    def __init__(self, log_exporter: Type[iLogsExporter]):
        self.exporter = log_exporter
    
    def get_logger(self):
        return self.exporter.get_logger()
    
    def new_log(self, msg: str, tags: dict, level: str):
        logger = self.get_logger()
        logger.log(level, msg, extra=tags)
