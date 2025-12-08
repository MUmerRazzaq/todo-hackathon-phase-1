"""
Main entry point for the Interactive CLI Todo Application.

This module provides the main function to run the application.
"""
import signal
import sys
from typing import NoReturn
from .models.task_manager import TaskManager
from .views.cli_view import CliView
from .controllers.app_controller import AppController


def signal_handler(signum, frame) -> NoReturn:
    """
    Handle system signals for graceful shutdown.

    Args:
        signum: Signal number
        frame: Current stack frame
    """
    # We don't need to use the parameters, just need them for the signal handler
    # signature
    print("\nReceived interrupt signal. Exiting gracefully...")
    sys.exit(0)


def main():
    """
    Main function to run the Interactive CLI Todo Application.

    Initializes the task manager, CLI view, and application controller,
    then starts the application loop. Includes proper exception handling
    and signal handling for graceful shutdown.
    """
    # Register signal handler for graceful shutdown
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)

    # Initialize the components
    task_manager = TaskManager()
    cli_view = CliView(task_manager)
    app_controller = AppController(task_manager, cli_view)

    try:
        # Run the application
        app_controller.run()
    except KeyboardInterrupt:
        print("\nApplication interrupted by user. Exiting gracefully...")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
    finally:
        # Ensure cleanup happens even if an exception occurs
        print("Shutting down application... Goodbye!")


if __name__ == "__main__":
    main()
