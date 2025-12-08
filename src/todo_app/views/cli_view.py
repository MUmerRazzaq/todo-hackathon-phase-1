"""
CLI View module for the Interactive CLI Todo Application.

This module defines the CliView class which handles UI rendering and display
using the curses library.
"""
import curses
from typing import List, Optional
from ..models.task import Task
from ..models.task_manager import TaskManager
from .constants import ASCII_HEADER, COLORS, DISPLAY, MENU_OPTIONS


class CliView:
    """
    Handles UI rendering and display using the curses library.

    This class manages the terminal interface, including screen initialization,
    menu display, task rendering, and keyboard input handling.
    """
    def __init__(self, task_manager: TaskManager):
        """
        Initialize the CLI view with a task manager.

        Args:
            task_manager (TaskManager): The task manager to display tasks from
        """
        self.task_manager = task_manager
        self.screen = None
        self.current_selection = 0
        self.current_view = "main_menu"  # main_menu, view_tasks, add_task, etc.

    def setup_curses(self):
        """Initialize curses and set up the screen."""
        self.screen = curses.initscr()
        curses.start_color()
        curses.use_default_colors()
        curses.noecho()
        curses.cbreak()
        self.screen.keypad(True)

        # Initialize color pairs
        curses.init_pair(COLORS["HEADER"], curses.COLOR_CYAN, -1)
        curses.init_pair(COLORS["MENU"], curses.COLOR_YELLOW, -1)
        curses.init_pair(COLORS["TASK"], curses.COLOR_WHITE, -1)
        curses.init_pair(COLORS["SUCCESS"], curses.COLOR_GREEN, -1)
        curses.init_pair(COLORS["ERROR"], curses.COLOR_RED, -1)
        curses.init_pair(COLORS["HIGHLIGHT"], curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(COLORS["COMPLETED"], curses.COLOR_GREEN, -1)

    def cleanup(self):
        """Clean up curses settings and restore terminal."""
        if self.screen:
            self.screen.keypad(False)
        curses.nocbreak()
        curses.echo()
        curses.endwin()

    def clear_screen(self):
        """Clear the screen and refresh."""
        if self.screen:
            self.screen.clear()

    def display_header(self):
        """Display the ASCII art header at the top of the screen."""
        if not self.screen:
            return

        height, width = self.screen.getmaxyx()

        for i, line in enumerate(ASCII_HEADER):
            if i < DISPLAY["HEADER_HEIGHT"] and i < height:
                # Center the header if there's enough width
                x = max(0, (width - len(line)) // 2)
                self.screen.addstr(i, x, line, curses.color_pair(COLORS["HEADER"]))

    def display_menu(self):
        """Display the main menu with highlighting for the current selection."""
        if not self.screen:
            return

        height, width = self.screen.getmaxyx()
        start_y = DISPLAY["HEADER_HEIGHT"] + 1  # Start below the header

        for i, option in enumerate(MENU_OPTIONS):
            attr = curses.A_NORMAL
            if i == self.current_selection:
                attr = curses.color_pair(COLORS["HIGHLIGHT"])

            # Only display if we have enough screen space
            if start_y + i < height:
                text = f"> {option}" if i == self.current_selection else f"  {option}"
                self.screen.addstr(
                    start_y + i, 2, text,
                    curses.color_pair(COLORS["MENU"]) | attr
                )

    def display_tasks(self, tasks: List[Task], show_status: bool = True):
        """Display a list of tasks with their details."""
        if not self.screen:
            return

        height, width = self.screen.getmaxyx()
        start_y = DISPLAY["HEADER_HEIGHT"] + 1
        menu_width = DISPLAY["MENU_WIDTH"]
        task_area_start = menu_width + 2

        # Display column headers
        if start_y < height:
            attr = curses.color_pair(COLORS["TASK"]) | curses.A_BOLD
            self.screen.addstr(start_y, task_area_start, "ID", attr)
            self.screen.addstr(start_y, task_area_start + 5, "Title", attr)
            if show_status:
                self.screen.addstr(start_y, task_area_start + 30, "Status", attr)

        # Display tasks
        for i, task in enumerate(tasks):
            display_y = start_y + 2 + i
            if display_y >= height:
                break  # Don't display if we run out of screen space

            # Display task ID
            color_pair = curses.color_pair(COLORS["TASK"])
            self.screen.addstr(display_y, task_area_start, str(task.id), color_pair)

            # Display task title (with truncation if needed)
            title = task.title
            max_title_len = DISPLAY["TASK_PREVIEW_LENGTH"]
            if len(title) > max_title_len:
                title = title[:max_title_len - 3] + "..."

            color = COLORS["COMPLETED"] if task.status else COLORS["TASK"]
            self.screen.addstr(
                display_y, task_area_start + 5, title,
                curses.color_pair(color)
            )

            # Display status if requested
            if show_status:
                status_text = "[completed] ✓" if task.status else "[incomplete]"
                color = COLORS["COMPLETED"] if task.status else COLORS["TASK"]
                self.screen.addstr(
                    display_y, task_area_start + 30, status_text,
                    curses.color_pair(color)
                )

    def display_totals(self):
        """Display real-time totals (Pending: X, Completed: Y)."""
        if not self.screen:
            return

        height, width = self.screen.getmaxyx()
        pending_count = self.task_manager.get_pending_count()
        completed_count = self.task_manager.get_completed_count()
        total_count = self.task_manager.get_task_count()

        totals_text = f"Total: {total_count} | Pending: {pending_count} | " \
                      f"Completed: {completed_count}"

        # Display at the bottom of the screen
        self.screen.addstr(height - 2, 2, totals_text, curses.color_pair(COLORS["MENU"]))

    def display_message(self, message: str, message_type: str = "info"):
        """Display a message with appropriate styling."""
        if not self.screen:
            return

        height, width = self.screen.getmaxyx()
        color = COLORS["TASK"]

        if message_type == "success":
            color = COLORS["SUCCESS"]
        elif message_type == "error":
            color = COLORS["ERROR"]

        # Display message in the middle of the screen
        msg_y = height // 2
        msg_x = max(0, (width - len(message)) // 2)

        self.screen.addstr(msg_y, msg_x, message, curses.color_pair(color))
        self.screen.refresh()

        # Brief pause to show the message
        curses.napms(1500)

    def get_user_input(self, prompt: str) -> Optional[str]:
        """Get user input with a prompt."""
        if not self.screen:
            return None

        height, width = self.screen.getmaxyx()
        input_y = height - 4
        input_x = 2

        # Clear the input area
        self.screen.addstr(input_y, input_x, " " * (width - input_x - 1))
        self.screen.addstr(input_y + 1, input_x, " " * (width - input_x - 1))

        # Show the prompt
        self.screen.addstr(input_y, input_x, prompt, curses.color_pair(COLORS["MENU"]))
        self.screen.refresh()

        # Get user input
        curses.echo()
        try:
            user_input = self.screen.getstr(input_y + 1, input_x, 100).decode('utf-8')
        except Exception:
            user_input = ""
        finally:
            curses.noecho()

        return user_input.strip()

    def get_confirmation(self, prompt: str) -> bool:
        """Get yes/no confirmation from user."""
        if not self.screen:
            return False

        height, width = self.screen.getmaxyx()
        input_y = height - 4
        input_x = 2

        # Clear the input area
        self.screen.addstr(input_y, input_x, " " * (width - input_x - 1))
        self.screen.addstr(input_y + 1, input_x, " " * (width - input_x - 1))

        # Show the prompt
        self.screen.addstr(input_y, input_x, prompt, curses.color_pair(COLORS["MENU"]))
        self.screen.refresh()

        # Get user input
        curses.echo()
        try:
            user_input = self.screen.getstr(input_y + 1, input_x, 1).decode('utf-8').lower()
        except Exception:
            user_input = ""
        finally:
            curses.noecho()

        return user_input in ['y', 'yes']

    def refresh(self):
        """Refresh the screen to update the display."""
        if self.screen:
            self.screen.refresh()
