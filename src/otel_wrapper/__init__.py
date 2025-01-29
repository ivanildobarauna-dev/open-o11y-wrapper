from .deps_injector import wrapper_builder


class OpenObservabilityWrapper:
    def __init__(self, application_name: str):
        self.wrapper = wrapper_builder(application_name=application_name)

    def get_trace(self):
        return self.wrapper.traces().get_tracer()

    def send_log(self):
        self.wrapper.logs().send_log()

    def increment_metric(self, name: str, tags: dict):
        self.wrapper.metrics().metric_increment(name=name, tags=tags)


__all__ = [OpenObservabilityWrapper]
