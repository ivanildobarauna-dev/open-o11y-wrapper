from typing import Type
from ...infrastructure.ports.outbound_trace_exporter import iTracesExporter


class TraceProcessorService:
    def __init__(self, trace_exporter: Type[iTracesExporter]):
        self._exporter = trace_exporter
        self._tracer = self._exporter.get_tracer()

    def new_span(self, name: str):
        return self._tracer.start_span(name=name)

    def get_tracer(self):
        return self._tracer