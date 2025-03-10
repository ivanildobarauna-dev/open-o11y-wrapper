import pytest
from unittest.mock import patch, MagicMock
from otel_wrapper.deps_injector import wrapper_builder
from otel_wrapper.builder import Wrapper


class TestDepsInjector:
    """Test suite for the dependency injector module."""
    
    def test_wrapper_builder(self):
        """Test the wrapper_builder factory function."""
        # Create patches for all the adapters
        with patch('otel_wrapper.deps_injector.TraceExporterAdapter') as mock_trace_adapter, \
             patch('otel_wrapper.deps_injector.LogExporterAdapter') as mock_log_adapter, \
             patch('otel_wrapper.deps_injector.MetricsExporterAdapter') as mock_metrics_adapter, \
             patch('otel_wrapper.deps_injector.TraceProcessorService') as mock_trace_service, \
             patch('otel_wrapper.deps_injector.LogsProcessorService') as mock_log_service, \
             patch('otel_wrapper.deps_injector.MetricsProcessorService') as mock_metrics_service, \
             patch('otel_wrapper.deps_injector.Wrapper') as mock_wrapper:
            
            # Setup mock returns
            mock_trace_adapter_instance = MagicMock()
            mock_log_adapter_instance = MagicMock()
            mock_metrics_adapter_instance = MagicMock()
            
            mock_trace_adapter.return_value = mock_trace_adapter_instance
            mock_log_adapter.return_value = mock_log_adapter_instance
            mock_metrics_adapter.return_value = mock_metrics_adapter_instance
            
            mock_trace_service_instance = MagicMock()
            mock_log_service_instance = MagicMock()
            mock_metrics_service_instance = MagicMock()
            
            mock_trace_service.return_value = mock_trace_service_instance
            mock_log_service.return_value = mock_log_service_instance
            mock_metrics_service.return_value = mock_metrics_service_instance
            
            mock_wrapper_instance = MagicMock()
            mock_wrapper.return_value = mock_wrapper_instance
            
            # Call the wrapper_builder
            app_name = "test-app"
            result = wrapper_builder(application_name=app_name)
            
            # Verify all the expected calls were made
            mock_trace_adapter.assert_called_once_with(application_name=app_name)
            mock_log_adapter.assert_called_once_with(application_name=app_name)
            mock_metrics_adapter.assert_called_once_with(application_name=app_name)
            
            mock_trace_service.assert_called_once_with(trace_exporter=mock_trace_adapter_instance)
            mock_log_service.assert_called_once_with(log_exporter=mock_log_adapter_instance)
            mock_metrics_service.assert_called_once_with(metric_exporter=mock_metrics_adapter_instance)
            
            mock_wrapper.assert_called_once_with(
                trace_service=mock_trace_service_instance,
                log_service=mock_log_service_instance,
                metrics_service=mock_metrics_service_instance
            )
            
            # Verify the result is the wrapper instance
            assert result == mock_wrapper_instance


@pytest.mark.skip(reason="This test creates actual singleton instances which may affect other tests")
def test_wrapper_builder_integration():
    """Test the wrapper_builder factory function with actual objects (integration test)."""
    # Call the wrapper_builder
    app_name = "test-app-integration"
    wrapper = wrapper_builder(application_name=app_name)
    
    # Verify the wrapper is created and has the right structure
    assert isinstance(wrapper, Wrapper)
    assert wrapper.traces() is not None
    assert wrapper.logs() is not None
    assert wrapper.metrics() is not None