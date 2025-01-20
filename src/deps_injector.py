from src.builder import Wrapper
from src.domain.services.trace_service import TraceProcessorService
from src.domain.services.logs_service import LogsProcessorService
from src.domain.services.metrics_service import MetricsProcessorService
from src.infrastructure.adapters.log_exporter import LogExporterAdapter
from src.infrastructure.adapters.metrics_exporter import MetricsExporterAdapter
from src.infrastructure.adapters.trace_exporter import TraceExporterAdapter


def wrapper_builder(application_name: str) -> Wrapper:
    _trace_exporter = TraceExporterAdapter(application_name=application_name)
    _log_exporter = LogExporterAdapter(application_name=application_name)
    _metrics_exporter = MetricsExporterAdapter(application_name=application_name)

    _trace_service = TraceProcessorService(exporter=_trace_exporter)
    _log_service = LogsProcessorService(exporter=_log_exporter)
    _metrics_service = MetricsProcessorService(exporter=_metrics_exporter)

    wrapper = Wrapper(
        trace_service=_trace_service,
        log_service=_log_service,
        metrics_service=_metrics_service,
    )

    return wrapper
