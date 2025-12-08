"""
Pytest configuration for the Interactive CLI Todo Application tests.
"""
import pytest
import sys
from unittest.mock import patch


def pytest_configure(config):
    """Configure pytest settings."""
    config.addinivalue_line(
        "markers", "integration: mark test as integration test"
    )
    config.addinivalue_line(
        "markers", "unit: mark test as unit test"
    )


@pytest.fixture(autouse=True)
def mock_curses():
    """
    Auto-mock curses module to prevent issues when running tests
    in non-terminal environments.
    """
    with patch.dict('sys.modules', {
        'curses': None,  # This will cause import to fail and be handled
    }):
        # We'll handle the curses import in the actual code
        yield


@pytest.fixture
def sample_task_manager():
    """Provide a fresh TaskManager instance for tests."""
    from src.todo_app.models.task_manager import TaskManager
    return TaskManager()


@pytest.fixture
def sample_task():
    """Provide a sample Task instance for tests."""
    from src.todo_app.models.task import Task
    return Task(id=1, title="Sample Task", description="Sample Description")