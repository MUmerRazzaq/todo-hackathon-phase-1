"""
Unit tests for the TaskManager class in the Interactive CLI Todo Application.
"""
import pytest
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from todo_app.models.task import Task
from todo_app.models.task_manager import TaskManager


class TestTaskManager:
    """Test class for TaskManager functionality."""

    def test_initialization(self):
        """Test that TaskManager initializes with empty tasks and next_id of 1."""
        tm = TaskManager()

        assert len(tm.tasks) == 0
        assert tm.next_id == 1

    def test_add_task_success(self):
        """Test adding a task successfully."""
        tm = TaskManager()

        task = tm.add_task("Test Task", "Test Description")

        assert len(tm.tasks) == 1
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status is False

    def test_add_task_without_description(self):
        """Test adding a task without description."""
        tm = TaskManager()

        task = tm.add_task("Test Task")

        assert len(tm.tasks) == 1
        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.status is False

    def test_add_task_fails_with_empty_title(self):
        """Test that adding a task with empty title raises ValueError."""
        tm = TaskManager()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            tm.add_task("")

    def test_add_task_fails_with_whitespace_only_title(self):
        """Test that adding a task with whitespace-only title raises ValueError."""
        tm = TaskManager()

        with pytest.raises(ValueError, match="Title cannot be empty"):
            tm.add_task("   ")

    def test_add_task_fails_with_long_title(self):
        """Test that adding a task with title exceeding 100 chars raises ValueError."""
        tm = TaskManager()
        long_title = "x" * 101

        with pytest.raises(ValueError, match="Title cannot exceed 100 characters"):
            tm.add_task(long_title)

    def test_add_task_fails_with_long_description(self):
        """Test that adding a task with description exceeding 500 chars raises ValueError."""
        tm = TaskManager()
        long_description = "x" * 501

        with pytest.raises(ValueError, match="Description cannot exceed 500 characters"):
            tm.add_task("Test Title", long_description)

    def test_add_task_assigns_unique_ids(self):
        """Test that each added task gets a unique ID."""
        tm = TaskManager()

        task1 = tm.add_task("Task 1")
        task2 = tm.add_task("Task 2")
        task3 = tm.add_task("Task 3")

        assert task1.id == 1
        assert task2.id == 2
        assert task3.id == 3
        assert len(tm.tasks) == 3

    def test_get_task_success(self):
        """Test getting a task by ID."""
        tm = TaskManager()
        added_task = tm.add_task("Test Task")

        retrieved_task = tm.get_task(added_task.id)

        assert retrieved_task is not None
        assert retrieved_task.id == added_task.id
        assert retrieved_task.title == added_task.title

    def test_get_task_returns_none_for_nonexistent_id(self):
        """Test that get_task returns None for non-existent ID."""
        tm = TaskManager()

        retrieved_task = tm.get_task(999)

        assert retrieved_task is None

    def test_get_all_tasks(self):
        """Test getting all tasks."""
        tm = TaskManager()
        task1 = tm.add_task("Task 1")
        task2 = tm.add_task("Task 2")

        all_tasks = tm.get_all_tasks()

        assert len(all_tasks) == 2
        assert task1 in all_tasks
        assert task2 in all_tasks

    def test_get_pending_tasks(self):
        """Test getting pending tasks only."""
        tm = TaskManager()
        pending_task = tm.add_task("Pending Task")
        completed_task = tm.add_task("Completed Task")
        tm.mark_task_completed(completed_task.id)

        pending_tasks = tm.get_pending_tasks()

        assert len(pending_tasks) == 1
        assert pending_task in pending_tasks
        assert completed_task not in pending_tasks

    def test_get_completed_tasks(self):
        """Test getting completed tasks only."""
        tm = TaskManager()
        pending_task = tm.add_task("Pending Task")
        completed_task = tm.add_task("Completed Task")
        tm.mark_task_completed(completed_task.id)

        completed_tasks = tm.get_completed_tasks()

        assert len(completed_tasks) == 1
        assert completed_task in completed_tasks
        assert pending_task not in completed_tasks

    def test_update_task_success(self):
        """Test updating a task successfully."""
        tm = TaskManager()
        task = tm.add_task("Old Title", "Old Description")

        success = tm.update_task(task.id, "New Title", "New Description")

        assert success is True
        assert tm.tasks[task.id].title == "New Title"
        assert tm.tasks[task.id].description == "New Description"

    def test_update_task_with_partial_updates(self):
        """Test updating only title or only description."""
        tm = TaskManager()
        task = tm.add_task("Old Title", "Old Description")

        # Update only title
        tm.update_task(task.id, title="New Title")
        assert tm.tasks[task.id].title == "New Title"
        assert tm.tasks[task.id].description == "Old Description"

        # Update only description
        tm.update_task(task.id, description="New Description")
        assert tm.tasks[task.id].title == "New Title"
        assert tm.tasks[task.id].description == "New Description"

    def test_update_task_fails_for_nonexistent_id(self):
        """Test that updating a non-existent task returns False."""
        tm = TaskManager()

        success = tm.update_task(999, "New Title")

        assert success is False

    def test_update_task_fails_with_empty_title(self):
        """Test that updating with empty title raises ValueError."""
        tm = TaskManager()
        task = tm.add_task("Old Title")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            tm.update_task(task.id, "")

    def test_update_task_fails_with_long_title(self):
        """Test that updating with long title raises ValueError."""
        tm = TaskManager()
        task = tm.add_task("Old Title")
        long_title = "x" * 101

        with pytest.raises(ValueError, match="Title cannot exceed 100 characters"):
            tm.update_task(task.id, long_title)

    def test_update_task_fails_with_long_description(self):
        """Test that updating with long description raises ValueError."""
        tm = TaskManager()
        task = tm.add_task("Old Title")
        long_description = "x" * 501

        with pytest.raises(ValueError, match="Description cannot exceed 500 characters"):
            tm.update_task(task.id, description=long_description)

    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        tm = TaskManager()
        task = tm.add_task("Test Task")

        success = tm.delete_task(task.id)

        assert success is True
        assert len(tm.tasks) == 0
        assert task.id not in tm.tasks

    def test_delete_task_fails_for_nonexistent_id(self):
        """Test that deleting a non-existent task returns False."""
        tm = TaskManager()

        success = tm.delete_task(999)

        assert success is False

    def test_mark_task_completed_success(self):
        """Test marking a task as completed."""
        tm = TaskManager()
        task = tm.add_task("Test Task")  # Initially status is False by default

        success = tm.mark_task_completed(task.id)

        assert success is True
        assert tm.tasks[task.id].status is True

    def test_mark_task_completed_fails_for_nonexistent_id(self):
        """Test that marking a non-existent task as completed returns False."""
        tm = TaskManager()

        success = tm.mark_task_completed(999)

        assert success is False

    def test_mark_task_incomplete_success(self):
        """Test marking a task as incomplete."""
        tm = TaskManager()
        task = tm.add_task("Test Task")  # Initially status is False by default
        # First mark as completed
        tm.mark_task_completed(task.id)

        success = tm.mark_task_incomplete(task.id)

        assert success is True
        assert tm.tasks[task.id].status is False

    def test_mark_task_incomplete_fails_for_nonexistent_id(self):
        """Test that marking a non-existent task as incomplete returns False."""
        tm = TaskManager()

        success = tm.mark_task_incomplete(999)

        assert success is False

    def test_get_task_count(self):
        """Test getting the total task count."""
        tm = TaskManager()
        assert tm.get_task_count() == 0

        tm.add_task("Task 1")
        assert tm.get_task_count() == 1

        tm.add_task("Task 2")
        assert tm.get_task_count() == 2

    def test_get_pending_count(self):
        """Test getting the pending task count."""
        tm = TaskManager()
        task1 = tm.add_task("Task 1")
        task2 = tm.add_task("Task 2")
        tm.mark_task_completed(task2.id)

        assert tm.get_pending_count() == 1

    def test_get_completed_count(self):
        """Test getting the completed task count."""
        tm = TaskManager()
        task1 = tm.add_task("Task 1")
        task2 = tm.add_task("Task 2")
        tm.mark_task_completed(task2.id)

        assert tm.get_completed_count() == 1