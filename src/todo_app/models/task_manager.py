"""
TaskManager class for the Interactive CLI Todo Application.

This module defines the TaskManager class which handles all business
logic for task operations including creation, retrieval, updating,
deletion, and status management.
"""
from typing import Dict, List, Optional
from .task import Task


class TaskManager:
    """
    Manages a collection of Task objects with methods for CRUD operations and status management.

    Attributes:
        tasks (Dict[int, Task]): Dictionary mapping task IDs to Task objects
        next_id (int): Next available ID for new tasks (auto-incrementing)
    """
    def __init__(self):
        """Initialize an empty task manager with ID counter starting at 1."""
        self.tasks: Dict[int, Task] = {}
        self.next_id = 1

    def add_task(self, title: str, description: str = "") -> Task:
        """
        Creates and adds a new task to the manager.

        Args:
            title (str): Title for the new task (required, max 100 chars)
            description (str): Description for the new task (optional, max 500 chars)

        Returns:
            Task: The newly created Task object

        Raises:
            ValueError: If title is empty or exceeds character limits
        """
        # Validate title before creating task
        if len(title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        if len(description) > 500:
            raise ValueError("Description cannot exceed 500 characters")

        task = Task(id=self.next_id, title=title.strip(), description=description)
        self.tasks[self.next_id] = task
        self.next_id += 1
        return task

    def get_task(self, task_id: int) -> Optional[Task]:
        """
        Retrieves a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve

        Returns:
            Optional[Task]: The Task object if found, None otherwise
        """
        return self.tasks.get(task_id)

    def get_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the manager.

        Returns:
            List[Task]: List of all Task objects
        """
        return list(self.tasks.values())

    def get_pending_tasks(self) -> List[Task]:
        """
        Returns only incomplete tasks.

        Returns:
            List[Task]: List of Task objects with status=False
        """
        return [task for task in self.tasks.values() if not task.status]

    def get_completed_tasks(self) -> List[Task]:
        """
        Returns only completed tasks.

        Returns:
            List[Task]: List of Task objects with status=True
        """
        return [task for task in self.tasks.values() if task.status]

    def update_task(self, task_id: int, title: str = None, description: str = None) -> bool:
        """
        Updates a task's properties.

        Args:
            task_id (int): ID of the task to update
            title (str, optional): New title for the task
            description (str, optional): New description for the task

        Returns:
            bool: True if update was successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        task = self.tasks[task_id]

        if title is not None:
            if len(title.strip()) == 0:
                raise ValueError("Title cannot be empty")
            if len(title) > 100:
                raise ValueError("Title cannot exceed 100 characters")
            task.update_title(title)

        if description is not None:
            if len(description) > 500:
                raise ValueError("Description cannot exceed 500 characters")
            task.update_description(description)

        return True

    def delete_task(self, task_id: int) -> bool:
        """
        Removes a task by its ID.

        Args:
            task_id (int): ID of the task to delete

        Returns:
            bool: True if deletion was successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        del self.tasks[task_id]
        return True

    def mark_task_completed(self, task_id: int) -> bool:
        """
        Marks a task as completed.

        Args:
            task_id (int): ID of the task to mark as completed

        Returns:
            bool: True if operation was successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        self.tasks[task_id].mark_completed()
        return True

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Marks a task as incomplete.

        Args:
            task_id (int): ID of the task to mark as incomplete

        Returns:
            bool: True if operation was successful, False if task not found
        """
        if task_id not in self.tasks:
            return False

        self.tasks[task_id].mark_incomplete()
        return True

    def get_task_count(self) -> int:
        """
        Returns total number of tasks.

        Returns:
            int: Total number of tasks in the manager
        """
        return len(self.tasks)

    def get_pending_count(self) -> int:
        """
        Returns number of pending tasks.

        Returns:
            int: Number of tasks with status=False
        """
        return len(self.get_pending_tasks())

    def get_completed_count(self) -> int:
        """
        Returns number of completed tasks.

        Returns:
            int: Number of tasks with status=True
        """
        return len(self.get_completed_tasks())
