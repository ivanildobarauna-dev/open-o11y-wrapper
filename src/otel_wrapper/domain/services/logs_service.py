from typing import Type
from ...infrastructure.ports.outbound_logs_exporter import iLogsExporter


class LogsProcessorService:
    def __init__(self, log_exporter: Type[iLogsExporter]):
        self.exporter = log_exporter
        
    def new_log(self, msg: str, tags: dict, level: int):
        logger = self.get_logger()
        logger.log(level, msg, extra=tags)
