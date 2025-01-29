from .deps_injector import wrapper_builder


class OpenObservabilityWrapper:
    def __init__(self, application_name: str):
        self.wrapper = wrapper_builder(application_name=application_name)

    def get_trace(self):
        return self.wrapper.traces().get_tracer()

    def get_logger(self):
        return self.wrapper.logs().get_logger()

    def increment_metric(self, name: str, tags: dict, value: float):
        self.wrapper.metrics().metric_increment(name=name, tags=tags, value=value)


__all__ = [OpenObservabilityWrapper]
