from .deps_injector import wrapper_builder


class OpenObservability:
    def __init__(self, application_name: str):
        self.wrapper = wrapper_builder(application_name=application_name)

    def get_wrapper(self):
        return self.wrapper


__all__ = [OpenObservability]
