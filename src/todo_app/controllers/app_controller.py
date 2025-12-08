"""
App Controller module for the Interactive CLI Todo Application.

This module defines the AppController class which handles input processing
and application flow coordination.
"""
import curses
from ..models.task_manager import TaskManager
from ..views.cli_view import CliView
from ..views.constants import MESSAGES, MENU_OPTIONS


class AppController:
    """
    Handles input processing and application flow coordination.

    This class manages the application state, processes keyboard input,
    and coordinates between the model (TaskManager) and view (CliView).
    """
    def __init__(self, task_manager: TaskManager, cli_view: CliView):
        """
        Initialize the application controller with task manager and CLI view.

        Args:
            task_manager (TaskManager): The task manager to operate on
            cli_view (CliView): The CLI view for UI rendering
        """
        self.task_manager = task_manager
        self.cli_view = cli_view
        self.running = True

    def run(self):
        """Main application loop."""
        self.cli_view.setup_curses()
        try:
            while self.running:
                self.display_current_view()
                self.handle_input()
        finally:
            self.cli_view.cleanup()

    def display_current_view(self):
        """Display the current view based on application state."""
        self.cli_view.clear_screen()
        self.cli_view.display_header()

        if self.cli_view.current_view == "main_menu":
            self.display_main_menu()
        elif self.cli_view.current_view == "view_all_tasks":
            self.display_tasks(self.task_manager.get_all_tasks())
        elif self.cli_view.current_view == "view_pending_tasks":
            self.display_tasks(self.task_manager.get_pending_tasks())
        elif self.cli_view.current_view == "view_completed_tasks":
            self.display_tasks(self.task_manager.get_completed_tasks())

        self.cli_view.display_totals()
        self.cli_view.refresh()

    def display_main_menu(self):
        """Display the main menu."""
        self.cli_view.display_menu()

    def display_tasks(self, tasks):
        """Display a list of tasks."""
        if not tasks:
            height, width = self.cli_view.screen.getmaxyx()
            msg_y = height // 2
            msg_x = max(0, (width - len(MESSAGES["NO_TASKS"])) // 2)
            self.cli_view.screen.addstr(msg_y, msg_x, MESSAGES["NO_TASKS"])
        else:
            self.cli_view.display_tasks(tasks)

    def handle_input(self):
        """Handle keyboard input from the user."""
        if not self.cli_view.screen:
            return

        key = self.cli_view.screen.getch()

        # Handle navigation keys
        if key == curses.KEY_UP:
            self.handle_up_arrow()
        elif key == curses.KEY_DOWN:
            self.handle_down_arrow()
        elif key == 10 or key == curses.KEY_ENTER:  # Enter key
            self.handle_enter()
        elif key == 27:  # ESC key
            self.handle_escape()
        elif key == ord('q'):  # 'q' to quit
            self.running = False

    def handle_up_arrow(self):
        """Handle UP arrow key navigation."""
        if self.cli_view.current_view == "main_menu":
            self.cli_view.current_selection = max(0, self.cli_view.current_selection - 1)

    def handle_down_arrow(self):
        """Handle DOWN arrow key navigation."""
        if self.cli_view.current_view == "main_menu":
            max_selection = len(MENU_OPTIONS) - 1
            current_selection = self.cli_view.current_selection + 1
            self.cli_view.current_selection = min(max_selection, current_selection)

    def handle_enter(self):
        """Handle ENTER key selection."""
        if self.cli_view.current_view == "main_menu":
            self.handle_menu_selection()
        elif self.cli_view.current_view.startswith("view_"):
            # If viewing tasks, go back to main menu
            self.cli_view.current_view = "main_menu"

    def handle_escape(self):
        """Handle ESC key navigation."""
        # If in a sub-menu or task view, return to main menu
        if self.cli_view.current_view != "main_menu":
            self.cli_view.current_view = "main_menu"
        else:
            # If already in main menu, quit the application
            self.running = False

    def handle_menu_selection(self):
        """Handle menu item selection."""
        selected_option = MENU_OPTIONS[self.cli_view.current_selection]

        if selected_option == "Add Task":
            self.add_task()
        elif selected_option == "View All Tasks":
            self.cli_view.current_view = "view_all_tasks"
        elif selected_option == "View Pending Tasks":
            self.cli_view.current_view = "view_pending_tasks"
        elif selected_option == "View Completed Tasks":
            self.cli_view.current_view = "view_completed_tasks"
        elif selected_option == "Update Task":
            self.update_task()
        elif selected_option == "Delete Task":
            self.delete_task()
        elif selected_option == "Mark Complete":
            self.mark_task_complete()
        elif selected_option == "Mark Incomplete":
            self.mark_task_incomplete()
        elif selected_option == "Exit":
            self.running = False

    def add_task(self):
        """Handle adding a new task."""
        try:
            title = self.cli_view.get_user_input(MESSAGES["PROMPT_TITLE"])
            if not title:
                error_msg = MESSAGES["INVALID_INPUT"] + "Title is required"
                self.cli_view.display_message(error_msg, "error")
                return

            description = self.cli_view.get_user_input(MESSAGES["PROMPT_DESCRIPTION"])

            self.task_manager.add_task(title, description)
            self.cli_view.display_message(MESSAGES["TASK_ADDED"], "success")
        except ValueError as e:
            self.cli_view.display_message(MESSAGES["INVALID_INPUT"] + str(e), "error")

    def update_task(self):
        """Handle updating an existing task."""
        try:
            task_id_str = self.cli_view.get_user_input(MESSAGES["PROMPT_TASK_ID"])
            if not task_id_str:
                self.cli_view.display_message(MESSAGES["CANCELLED"], "info")
                return

            task_id = int(task_id_str)
            task = self.task_manager.get_task(task_id)
            if not task:
                self.cli_view.display_message(MESSAGES["TASK_NOT_FOUND"], "error")
                return

            # Get new title (or keep current if empty input)
            new_title = self.cli_view.get_user_input(MESSAGES["PROMPT_NEW_TITLE"])
            if not new_title:
                new_title = task.title

            # Get new description (or keep current if empty input)
            new_description = self.cli_view.get_user_input(MESSAGES["PROMPT_NEW_DESCRIPTION"])
            if not new_description:
                new_description = task.description

            success = self.task_manager.update_task(task_id, new_title, new_description)
            if success:
                self.cli_view.display_message(MESSAGES["TASK_UPDATED"], "success")
            else:
                self.cli_view.display_message(MESSAGES["TASK_NOT_FOUND"], "error")
        except ValueError:
            self.cli_view.display_message(MESSAGES["INVALID_INPUT"] + "Invalid task ID", "error")

    def delete_task(self):
        """Handle deleting a task."""
        try:
            task_id_str = self.cli_view.get_user_input(MESSAGES["PROMPT_TASK_ID"])
            if not task_id_str:
                self.cli_view.display_message(MESSAGES["CANCELLED"], "info")
                return

            task_id = int(task_id_str)
            task = self.task_manager.get_task(task_id)
            if not task:
                self.cli_view.display_message(MESSAGES["TASK_NOT_FOUND"], "error")
                return

            confirmed = self.cli_view.get_confirmation(MESSAGES["CONFIRM_DELETE"])
            if confirmed:
                success = self.task_manager.delete_task(task_id)
                if success:
                    self.cli_view.display_message(MESSAGES["TASK_DELETED"], "success")
                else:
                    self.cli_view.display_message(MESSAGES["TASK_NOT_FOUND"], "error")
            else:
                self.cli_view.display_message(MESSAGES["CANCELLED"], "info")
        except ValueError:
            self.cli_view.display_message(MESSAGES["INVALID_INPUT"] + "Invalid task ID", "error")

    def mark_task_complete(self):
        """Handle marking a task as complete."""
        try:
            task_id_str = self.cli_view.get_user_input(MESSAGES["PROMPT_TASK_ID"])
            if not task_id_str:
                self.cli_view.display_message(MESSAGES["CANCELLED"], "info")
                return

            task_id = int(task_id_str)
            success = self.task_manager.mark_task_completed(task_id)
            if success:
                self.cli_view.display_message(MESSAGES["TASK_COMPLETED"], "success")
            else:
                self.cli_view.display_message(MESSAGES["TASK_NOT_FOUND"], "error")
        except ValueError:
            self.cli_view.display_message(MESSAGES["INVALID_INPUT"] + "Invalid task ID", "error")

    def mark_task_incomplete(self):
        """Handle marking a task as incomplete."""
        try:
            task_id_str = self.cli_view.get_user_input(MESSAGES["PROMPT_TASK_ID"])
            if not task_id_str:
                self.cli_view.display_message(MESSAGES["CANCELLED"], "info")
                return

            task_id = int(task_id_str)
            success = self.task_manager.mark_task_incomplete(task_id)
            if success:
                self.cli_view.display_message(MESSAGES["TASK_INCOMPLETE"], "success")
            else:
                self.cli_view.display_message(MESSAGES["TASK_NOT_FOUND"], "error")
        except ValueError:
            self.cli_view.display_message(MESSAGES["INVALID_INPUT"] + "Invalid task ID", "error")
