from deps_injector import wrapper_builder

# Inicializa o Wrapper Builder
wrapper = wrapper_builder()

# Exponha os serviços diretamente para facilitar o uso
get_trace_service = wrapper.get_trace_service
get_log_service = wrapper.get_log_service
get_metrics_service = wrapper.get_metrics_service

__all__ = ["wrapper", "get_trace_service", "get_log_service", "get_metrics_service"]
