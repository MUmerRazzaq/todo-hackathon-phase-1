"""
Constants module for the Interactive CLI Todo Application.

This module defines color codes, display text, and configuration
constants used throughout the application.
"""
from enum import IntEnum


class Colors(IntEnum):
    """Color pair identifiers for curses color pairs."""
    HEADER = 1
    MENU = 2
    TASK = 3
    SUCCESS = 4
    ERROR = 5
    HIGHLIGHT = 6
    COMPLETED = 7


# Display configuration
DISPLAY = {
    "MIN_WIDTH": 80,
    "MIN_HEIGHT": 24,
    "MAX_TITLE_LENGTH": 100,
    "MAX_DESC_LENGTH": 500,
    "MENU_WIDTH": 25,  # Width of the left menu panel
    "TASK_PREVIEW_LENGTH": 50,  # Length of task description preview
    "HEADER_HEIGHT": 6,  # Height of ASCII art header
}

# Color definitions
COLORS = {
    "HEADER": Colors.HEADER,
    "MENU": Colors.MENU,
    "TASK": Colors.TASK,
    "SUCCESS": Colors.SUCCESS,
    "ERROR": Colors.ERROR,
    "HIGHLIGHT": Colors.HIGHLIGHT,
    "COMPLETED": Colors.COMPLETED,
}

# ASCII Art Header
ASCII_HEADER = [
    "╔════════════════════════════════════════════════════════════════════════════╗",
    "║                             INTERACTIVE TODO APP                           ║",
    "║                                v0.1.0                                      ║",
    "║                                                                            ║",
    "║                Manage your tasks with ease in the terminal!                ║",
    "╚════════════════════════════════════════════════════════════════════════════╝"
]

# Menu options
MENU_OPTIONS = [
    "Add Task",
    "View All Tasks",
    "View Pending Tasks",
    "View Completed Tasks",
    "Update Task",
    "Delete Task",
    "Mark Complete",
    "Mark Incomplete",
    "Exit"
]

# Status indicators
STATUS_INDICATORS = {
    True: "[completed] ✓",
    False: "[incomplete]",
}

# Display messages
MESSAGES = {
    "NO_TASKS": "No tasks found.",
    "TASK_ADDED": "Task added successfully!",
    "TASK_UPDATED": "Task updated successfully!",
    "TASK_DELETED": "Task deleted successfully!",
    "TASK_COMPLETED": "Task marked as completed!",
    "TASK_INCOMPLETE": "Task marked as incomplete!",
    "INVALID_INPUT": "Invalid input: ",
    "TASK_NOT_FOUND": "Task not found!",
    "CONFIRM_DELETE": "Are you sure you want to delete this task? (y/N): ",
    "CANCELLED": "Operation cancelled.",
    "PROMPT_TITLE": "Enter task title: ",
    "PROMPT_DESCRIPTION": "Enter task description (optional): ",
    "PROMPT_TASK_ID": "Enter task ID: ",
    "PROMPT_NEW_TITLE": "Enter new title (or press Enter to keep current): ",
    "PROMPT_NEW_DESCRIPTION": "Enter new description (or press Enter to keep current): ",
}
