"""
Unit tests for the Task dataclass in the Interactive CLI Todo Application.
"""
import pytest
from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from todo_app.models.task import Task


class TestTask:
    """Test class for Task dataclass functionality."""

    def test_task_creation_with_required_fields(self):
        """Test creating a Task with required fields only."""
        task = Task(id=1, title="Test Task")

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == ""
        assert task.status is False
        assert isinstance(task.created_at, datetime)

    def test_task_creation_with_all_fields(self):
        """Test creating a Task with all fields provided."""
        created_time = datetime.now()
        task = Task(id=1, title="Test Task", description="Test Description", status=True, created_at=created_time)

        assert task.id == 1
        assert task.title == "Test Task"
        assert task.description == "Test Description"
        assert task.status is True
        assert task.created_at == created_time

    def test_task_creation_sets_default_created_at(self):
        """Test that created_at is set automatically if not provided."""
        task = Task(id=1, title="Test Task")

        assert task.created_at is not None
        assert isinstance(task.created_at, datetime)

    def test_task_creation_fails_with_empty_title(self):
        """Test that creating a Task with empty title raises ValueError."""
        with pytest.raises(ValueError, match="Title cannot be empty"):
            Task(id=1, title="")

    def test_task_creation_fails_with_title_exceeding_max_length(self):
        """Test that creating a Task with title exceeding 100 chars raises ValueError."""
        long_title = "x" * 101
        with pytest.raises(ValueError, match="Title cannot exceed 100 characters"):
            Task(id=1, title=long_title)

    def test_task_creation_fails_with_description_exceeding_max_length(self):
        """Test that creating a Task with description exceeding 500 chars raises ValueError."""
        long_description = "x" * 501
        with pytest.raises(ValueError, match="Description cannot exceed 500 characters"):
            Task(id=1, title="Test", description=long_description)

    def test_mark_completed_method(self):
        """Test the mark_completed method."""
        task = Task(id=1, title="Test Task", status=False)

        task.mark_completed()

        assert task.status is True

    def test_mark_incomplete_method(self):
        """Test the mark_incomplete method."""
        task = Task(id=1, title="Test Task", status=True)

        task.mark_incomplete()

        assert task.status is False

    def test_update_title_success(self):
        """Test updating the title of a task successfully."""
        task = Task(id=1, title="Old Title")

        task.update_title("New Title")

        assert task.title == "New Title"

    def test_update_title_fails_with_empty_string(self):
        """Test that updating title with empty string raises ValueError."""
        task = Task(id=1, title="Old Title")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            task.update_title("")

    def test_update_title_fails_with_whitespace_only(self):
        """Test that updating title with whitespace only raises ValueError."""
        task = Task(id=1, title="Old Title")

        with pytest.raises(ValueError, match="Title cannot be empty"):
            task.update_title("   ")

    def test_update_title_fails_with_long_title(self):
        """Test that updating title with a long string raises ValueError."""
        task = Task(id=1, title="Old Title")
        long_title = "x" * 101

        with pytest.raises(ValueError, match="Title cannot exceed 100 characters"):
            task.update_title(long_title)

    def test_update_description_success(self):
        """Test updating the description of a task successfully."""
        task = Task(id=1, title="Test Title", description="Old Description")

        task.update_description("New Description")

        assert task.description == "New Description"

    def test_update_description_fails_with_long_description(self):
        """Test that updating description with a long string raises ValueError."""
        task = Task(id=1, title="Test Title")
        long_description = "x" * 501

        with pytest.raises(ValueError, match="Description cannot exceed 500 characters"):
            task.update_description(long_description)