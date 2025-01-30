from .deps_injector import wrapper_builder


class OpenObservabilityWrapper:
    def __init__(self, application_name: str):
        self.wrapper = wrapper_builder(application_name=application_name)

    def new_span(self, name: str):
        span = self.wrapper.traces().new_span(name=name)
        return span

    def new_log(self, msg: str, tags: dict, level: str):
        return self.wrapper.logs().new_log(msg=msg, tags=tags, level=level)

    def metric_increment(self, name: str, tags: dict, value: float):
        self.wrapper.metrics().metric_increment(name=name, tags=tags, value=value)


__all__ = [OpenObservabilityWrapper]
