"""
Unit tests for the constants module in the Interactive CLI Todo Application.
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
from todo_app.views.constants import (
    Colors, DISPLAY, COLORS, ASCII_HEADER, MENU_OPTIONS,
    STATUS_INDICATORS, MESSAGES
)


class TestConstants:
    """Test class for constants module."""

    def test_colors_enum_values(self):
        """Test that Colors enum has correct values."""
        assert Colors.HEADER == 1
        assert Colors.MENU == 2
        assert Colors.TASK == 3
        assert Colors.SUCCESS == 4
        assert Colors.ERROR == 5
        assert Colors.HIGHLIGHT == 6
        assert Colors.COMPLETED == 7

    def test_display_constants(self):
        """Test that DISPLAY dictionary has required keys and values."""
        assert 'MIN_WIDTH' in DISPLAY
        assert 'MIN_HEIGHT' in DISPLAY
        assert 'MAX_TITLE_LENGTH' in DISPLAY
        assert 'MAX_DESC_LENGTH' in DISPLAY
        assert 'MENU_WIDTH' in DISPLAY
        assert 'TASK_PREVIEW_LENGTH' in DISPLAY

        assert DISPLAY['MIN_WIDTH'] == 80
        assert DISPLAY['MIN_HEIGHT'] == 24
        assert DISPLAY['MAX_TITLE_LENGTH'] == 100
        assert DISPLAY['MAX_DESC_LENGTH'] == 500

    def test_colors_constants(self):
        """Test that COLORS dictionary maps to correct enum values."""
        assert COLORS['HEADER'] == Colors.HEADER
        assert COLORS['MENU'] == Colors.MENU
        assert COLORS['TASK'] == Colors.TASK
        assert COLORS['SUCCESS'] == Colors.SUCCESS
        assert COLORS['ERROR'] == Colors.ERROR
        assert COLORS['HIGHLIGHT'] == Colors.HIGHLIGHT
        assert COLORS['COMPLETED'] == Colors.COMPLETED

    def test_ascii_header_structure(self):
        """Test that ASCII_HEADER has the expected structure."""
        assert isinstance(ASCII_HEADER, list)
        assert len(ASCII_HEADER) == 6  # Based on the defined header
        assert all(isinstance(line, str) for line in ASCII_HEADER)

        # Check that the header contains expected content
        header_content = ''.join(ASCII_HEADER)
        assert 'INTERACTIVE TODO APP' in header_content

    def test_menu_options(self):
        """Test that MENU_OPTIONS contains expected menu items."""
        expected_options = [
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

        assert MENU_OPTIONS == expected_options
        assert len(MENU_OPTIONS) == 9

    def test_status_indicators(self):
        """Test that STATUS_INDICATORS has correct values."""
        assert STATUS_INDICATORS[True] == "[completed] ✓"
        assert STATUS_INDICATORS[False] == "[incomplete]"

    def test_messages_constants(self):
        """Test that MESSAGES dictionary has required keys."""
        required_keys = [
            'NO_TASKS',
            'TASK_ADDED',
            'TASK_UPDATED',
            'TASK_DELETED',
            'TASK_COMPLETED',
            'TASK_INCOMPLETE',
            'INVALID_INPUT',
            'TASK_NOT_FOUND',
            'CONFIRM_DELETE',
            'CANCELLED',
            'PROMPT_TITLE',
            'PROMPT_DESCRIPTION',
            'PROMPT_TASK_ID',
            'PROMPT_NEW_TITLE',
            'PROMPT_NEW_DESCRIPTION'
        ]

        for key in required_keys:
            assert key in MESSAGES
            assert isinstance(MESSAGES[key], str)