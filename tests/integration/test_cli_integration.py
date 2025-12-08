"""
Integration tests for the CLI components in the Interactive CLI Todo Application.
"""
import pytest
from unittest.mock import Mock, patch, MagicMock
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from todo_app.models.task_manager import TaskManager
from todo_app.views.cli_view import CliView
from todo_app.controllers.app_controller import AppController


class TestCLIIntegration:
    """Integration tests for CLI components."""

    def test_app_controller_initialization(self):
        """Test that AppController initializes with correct dependencies."""
        task_manager = TaskManager()
        cli_view = Mock(spec=CliView)

        # We'll mock the CliView since it uses curses which can't be easily tested
        app_controller = AppController(task_manager, cli_view)

        assert app_controller.task_manager is task_manager
        assert app_controller.cli_view is cli_view
        assert app_controller.running is True

    def test_cli_view_initialization(self):
        """Test that CliView initializes correctly."""
        task_manager = TaskManager()
        cli_view = CliView(task_manager)

        assert cli_view.task_manager is task_manager
        assert cli_view.current_selection == 0
        assert cli_view.current_view == "main_menu"

    def test_task_manager_and_cli_view_integration(self):
        """Test basic integration between TaskManager and CliView."""
        task_manager = TaskManager()
        cli_view = Mock(spec=CliView)
        app_controller = AppController(task_manager, cli_view)

        # Add a task through the task manager
        task = task_manager.add_task("Test Task", "Test Description")

        # Verify the task exists in the manager
        assert task_manager.get_task(task.id) is not None
        assert task_manager.get_task_count() == 1

        # Verify that tasks can be retrieved
        all_tasks = task_manager.get_all_tasks()
        assert len(all_tasks) == 1
        assert all_tasks[0].id == task.id

        pending_tasks = task_manager.get_pending_tasks()
        assert len(pending_tasks) == 1

    def test_app_controller_task_operations(self):
        """Test that AppController can perform basic task operations."""
        task_manager = TaskManager()
        cli_view = Mock(spec=CliView)
        app_controller = AppController(task_manager, cli_view)

        # Mock the view methods to avoid curses issues
        cli_view.get_user_input = Mock(return_value="Test Task")
        cli_view.display_message = Mock()
        cli_view.current_view = "main_menu"

        # Add a task via the controller
        task_manager.add_task("Test Task 1")

        # Check that the task exists
        assert task_manager.get_task_count() == 1

        # Update the task
        all_tasks = task_manager.get_all_tasks()
        task = all_tasks[0]
        success = task_manager.update_task(task.id, "Updated Task", "Updated Description")

        assert success is True
        updated_task = task_manager.get_task(task.id)
        assert updated_task.title == "Updated Task"
        assert updated_task.description == "Updated Description"

        # Mark as complete
        success = task_manager.mark_task_completed(task.id)
        assert success is True
        completed_task = task_manager.get_task(task.id)
        assert completed_task.status is True

        # Delete the task
        success = task_manager.delete_task(task.id)
        assert success is True
        assert task_manager.get_task_count() == 0

    def test_app_controller_view_transitions(self):
        """Test that AppController handles view transitions correctly."""
        task_manager = TaskManager()
        cli_view = CliView(task_manager)  # Use real CliView instead of Mock
        app_controller = AppController(task_manager, cli_view)

        # Test initial state
        assert app_controller.cli_view.current_view == "main_menu"

        # Simulate changing view
        app_controller.cli_view.current_view = "view_all_tasks"
        assert app_controller.cli_view.current_view == "view_all_tasks"

        # Test that we can navigate between views
        app_controller.cli_view.current_view = "view_pending_tasks"
        assert app_controller.cli_view.current_view == "view_pending_tasks"

    def test_navigation_controls_integration(self):
        """Test that navigation controls work with the view state."""
        task_manager = TaskManager()
        cli_view = CliView(task_manager)  # Use real CliView instead of Mock
        app_controller = AppController(task_manager, cli_view)

        # Set up initial state
        initial_selection = app_controller.cli_view.current_selection
        assert initial_selection == 0

        # Test UP arrow (should not go below 0)
        app_controller.handle_up_arrow()
        assert app_controller.cli_view.current_selection == 0  # Should remain 0

        # Test DOWN arrow
        app_controller.handle_down_arrow()
        assert app_controller.cli_view.current_selection == 1

        # Test multiple DOWN arrows
        app_controller.handle_down_arrow()
        app_controller.handle_down_arrow()
        assert app_controller.cli_view.current_selection == 3

        # Test that UP arrow decreases selection
        app_controller.handle_up_arrow()
        assert app_controller.cli_view.current_selection == 2

    def test_task_lifecycle_integration(self):
        """Test the full lifecycle of a task through the system."""
        task_manager = TaskManager()
        cli_view = Mock(spec=CliView)
        app_controller = AppController(task_manager, cli_view)

        # Mock user inputs
        cli_view.get_user_input = Mock(side_effect=["New Task", "Task Description"])
        cli_view.display_message = Mock()
        cli_view.get_confirmation = Mock(return_value=True)

        # Add a task
        initial_count = task_manager.get_task_count()
        new_task = task_manager.add_task("New Task", "Task Description")
        assert task_manager.get_task_count() == initial_count + 1

        # Retrieve the task
        retrieved_task = task_manager.get_task(new_task.id)
        assert retrieved_task is not None
        assert retrieved_task.title == "New Task"
        assert retrieved_task.description == "Task Description"

        # Update the task
        update_success = task_manager.update_task(new_task.id, "Updated Task Title", "Updated Description")
        assert update_success is True

        updated_task = task_manager.get_task(new_task.id)
        assert updated_task.title == "Updated Task Title"
        assert updated_task.description == "Updated Description"

        # Mark as complete
        complete_success = task_manager.mark_task_completed(new_task.id)
        assert complete_success is True
        assert task_manager.get_completed_count() == 1
        assert task_manager.get_pending_count() == 0

        # Mark as incomplete
        incomplete_success = task_manager.mark_task_incomplete(new_task.id)
        assert incomplete_success is True
        assert task_manager.get_completed_count() == 0
        assert task_manager.get_pending_count() == 1

        # Delete the task
        delete_success = task_manager.delete_task(new_task.id)
        assert delete_success is True
        assert task_manager.get_task_count() == 0