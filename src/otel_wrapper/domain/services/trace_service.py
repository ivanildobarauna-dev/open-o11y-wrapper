from typing import Type
from ...infrastructure.ports.outbound_trace_exporter import iTracesExporter


class TraceProcessorService:
    def __init__(self, trace_exporter: Type[iTracesExporter]):
        self.exporter = trace_exporter
        self.tracer = self.exporter.get_tracer()

    def new_span(self, name: str):
        return self.tracer.start_as_current_span(name)

    def get_tracer(self):
        return self.tracer