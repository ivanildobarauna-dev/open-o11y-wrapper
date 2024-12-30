from src.domain.services.logs_service import LogsService
from src.domain.services.metrics_service import MetricsService
from src.domain.services.trace_service import TraceService


class Wrapper:
    def __init__(
        self,
        trace_service: TraceService,
        log_service: LogsService,
        metrics_service: MetricsService,
    ):
        self.trace_service = trace_service
        self.log_service = log_service
        self.metrics_service = metrics_service

    def get_trace_service(self):
        return self.trace_service

    def get_log_service(self):
        return self.log_service

    def get_metrics_service(self):
        return self.metrics_service
