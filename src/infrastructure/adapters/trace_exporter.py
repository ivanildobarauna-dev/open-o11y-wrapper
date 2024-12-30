from src.infrastructure.ports.outbound_trace_exporter import iTracesExporter


class TraceExporterAdapter(iTracesExporter):
    def __init__(self, endpoint: str):
        self.endpoint = endpoint
        self.tracer = self.setup()

    def setup(self): ...

    def get_tracer(self):
        return self.tracer
