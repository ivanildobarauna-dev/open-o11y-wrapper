from typing import Type
from src.otel_wrapper.infrastructure.ports.outbound_trace_exporter import iTracesExporter


class TraceProcessorService:
    def __init__(self, trace_exporter: Type[iTracesExporter]):
        self.exporter = trace_exporter
        self.tracer = self.exporter.get_tracer()

    def get_tracer(self):
        return self.tracer
