from src.infrastructure.ports.outbound_logs_exporter import iLogsExporter


class LogExporterAdapter(iLogsExporter):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint

    def setup(self): ...
