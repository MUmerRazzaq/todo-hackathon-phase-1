# Quickstart Guide: Interactive CLI Todo Application

## Prerequisites

- Python 3.13 or higher
- UV package manager
- Terminal with color support (minimum 80x24)

## Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Install Dependencies with UV
```bash
uv sync
```

Or if setting up a new project:
```bash
uv init
uv add <dependencies>
```

### 3. Run the Application
```bash
uv run src/todo_app/main.py
```

Or install and run as a package:
```bash
uv build
uv pip install .
todo-app
```

## Project Structure

```
src/
├── todo_app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── task.py
│   │   └── task_manager.py
│   ├── views/
│   │   ├── __init__.py
│   │   ├── cli_view.py
│   │   └── constants.py
│   ├── controllers/
│   │   ├── __init__.py
│   │   └── app_controller.py
│   └── main.py
tests/
├── unit/
├── integration/
└── conftest.py
pyproject.toml
```

## Development Commands

### Run Tests
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=src/todo_app

# Run specific test file
uv run pytest tests/unit/test_task_manager.py
```

### Linting
```bash
# Check code style
uv run flake8 src/ tests/

# Format code
uv run black src/ tests/
```

### Build & Distribution
```bash
# Build the package
uv build

# Run the application in development
uv run src/todo_app/main.py
```

## Architecture Overview

### Model Layer
- `task.py`: Defines the Task dataclass with validation
- `task_manager.py`: Business logic for task operations

### View Layer
- `cli_view.py`: curses-based UI rendering and display logic
- `constants.py`: Color codes, display text, and configuration

### Controller Layer
- `app_controller.py`: Input handling and application flow coordination

## Key Features

### 1. Task Management
- Add tasks with titles and descriptions
- View all pending tasks
- Update existing tasks
- Delete tasks
- Mark tasks as complete/incomplete

### 2. UI Features
- Dual-panel interface with menu and task list
- ASCII art header that remains visible
- Color-coded status indicators
- Real-time updates after each operation
- Keyboard navigation (UP/DOWN/ENTER/ESC)

### 3. Validation & Error Handling
- Input validation for all user entries
- Helpful error messages
- Prevention of invalid operations
- Graceful handling of edge cases

## Running Tests

The application follows a Test-Driven Development approach:

```bash
# Unit tests for business logic
uv run pytest tests/unit/ -v

# Integration tests for CLI components
uv run pytest tests/integration/ -v

# All tests with coverage
uv run pytest --cov=src/todo_app --cov-report=html
```

## Configuration

All display constants, colors, and magic numbers are defined in `constants.py`:

```python
# Example constants
COLORS = {
    "HEADER": 1,      # Color pair for header
    "MENU": 2,        # Color pair for menu
    "TASK": 3,        # Color pair for tasks
    "SUCCESS": 4,     # Color pair for success messages
    "ERROR": 5,       # Color pair for error messages
    "HIGHLIGHT": 6    # Color pair for highlighted items
}

DISPLAY = {
    "MIN_WIDTH": 80,
    "MIN_HEIGHT": 24,
    "MAX_TITLE_LENGTH": 100,
    "MAX_DESC_LENGTH": 500
}
```