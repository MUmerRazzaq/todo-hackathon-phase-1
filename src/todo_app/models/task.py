"""
Task dataclass for the Interactive CLI Todo Application.

This module defines the Task dataclass with validation methods
for managing individual todo items.
"""
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Task:
    """
    Represents a single todo task with title, description, status, and creation
    timestamp.

    Attributes:
        id (int): Unique identifier for the task
        title (str): Short title/description of the task (required, max 100 chars)
        description (str): Detailed description of the task (optional, max 500 chars)
        status (bool): Boolean indicating completion status (default: False)
        created_at (datetime): Timestamp of when task was created (auto-generated)
    """
    id: int
    title: str
    description: str = ""
    status: bool = False
    created_at: datetime = None

    def __post_init__(self):
        """Initialize the created_at field if not provided."""
        if self.created_at is None:
            self.created_at = datetime.now()

        # Validate title length after initialization
        if len(self.title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(self.title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        if len(self.description) > 500:
            raise ValueError("Description cannot exceed 500 characters")

    def mark_completed(self):
        """Mark the task as completed."""
        self.status = True

    def mark_incomplete(self):
        """Mark the task as incomplete."""
        self.status = False

    def update_title(self, new_title: str):
        """
        Update the task title with validation.

        Args:
            new_title (str): New title for the task

        Raises:
            ValueError: If title is empty or exceeds 100 characters
        """
        if len(new_title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(new_title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        self.title = new_title.strip()

    def update_description(self, new_description: str):
        """
        Update the task description with validation.

        Args:
            new_description (str): New description for the task

        Raises:
            ValueError: If description exceeds 500 characters
        """
        if len(new_description) > 500:
            raise ValueError("Description cannot exceed 500 characters")
        self.description = new_description
