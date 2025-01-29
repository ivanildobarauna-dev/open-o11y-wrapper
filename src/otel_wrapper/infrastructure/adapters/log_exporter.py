from ...infrastructure.ports.outbound_logs_exporter import iLogsExporter


class LogExporterAdapter(iLogsExporter):
    ENDPOINT: str = "https://o11y-proxy.ivanildobarauna.dev/"
    def __init__(self, application_name: str):
        pass

    def setup(self):
        pass
    
    def send_log(self): 
        pass
