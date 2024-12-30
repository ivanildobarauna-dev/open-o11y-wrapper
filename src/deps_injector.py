from src.builder import Wrapper
from src.domain.services.trace_service import TraceProcessorService
from src.domain.services.logs_service import LogsProcessorService
from src.domain.services.metrics_service import MetricsProcessorService
from src.infrastructure.adapters.log_exporter import LogExporterAdapter
from src.infrastructure.adapters.metrics_exporter import MetricsExporterAdapter
from src.infrastructure.adapters.trace_exporter import TraceExporterAdapter
from src.infrastructure._contants import PROXY_ENDPOINT


def wrapper_builder() -> Wrapper:
    trace_exporter = TraceExporterAdapter(endpoint=PROXY_ENDPOINT)
    log_exporter = LogExporterAdapter(endpoint=PROXY_ENDPOINT)
    metrics_exporter = MetricsExporterAdapter(endpoint=PROXY_ENDPOINT)

    trace_service = TraceProcessorService(exporter=trace_exporter)
    log_service = LogsProcessorService(exporter=log_exporter)
    metrics_service = MetricsProcessorService(exporter=metrics_exporter)

    wrapper = Wrapper(
        trace_service=trace_service,
        log_service=log_service,
        metrics_service=metrics_service,
    )

    return wrapper
