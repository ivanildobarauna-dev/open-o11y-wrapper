import pytest
import logging
from unittest.mock import MagicMock
from otel_wrapper.domain.services.logs_service import LogsProcessorService


class TestLogsProcessorService:
    """Test suite for LogsProcessorService."""

    def test_init(self):
        """Test initialization of logs service."""
        # Create a mock log exporter
        mock_exporter = MagicMock()

        # Initialize the service
        service = LogsProcessorService(log_exporter=mock_exporter)

        # Verify initialization
        assert service._exporter == mock_exporter

    def test_new_log(self, mock_logger):
        """Test creating a new log."""
        # Create a mock log exporter
        mock_exporter = MagicMock()
        mock_exporter.get_logger.return_value = mock_logger

        # Initialize the service
        service = LogsProcessorService(log_exporter=mock_exporter)

        # Test creating a log
        msg = "Test log message"
        tags = {"test-key": "test-value"}
        level = logging.INFO

        service.new_log(msg=msg, tags=tags, level=level)

        # Verify the logger was called
        mock_exporter.get_logger.assert_called_once()
        mock_logger.log.assert_called_once_with(level, msg, extra=tags)

    def test_get_logger(self, mock_logger):
        """Test getting the logger."""
        # Create a mock log exporter
        mock_exporter = MagicMock()
        mock_exporter.get_logger.return_value = mock_logger

        # Initialize the service
        service = LogsProcessorService(log_exporter=mock_exporter)

        # Test getting the logger
        logger = service.get_logger()

        # Verify the exporter was called
        mock_exporter.get_logger.assert_called_once()
        assert logger == mock_logger
