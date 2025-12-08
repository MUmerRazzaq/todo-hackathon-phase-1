# Interactive CLI Todo Application

A feature-rich terminal-based todo application with a curses-based UI that provides a seamless and intuitive task management experience directly from your command line.

## 🌟 Features

- **Interactive Terminal UI**: Full-featured curses-based interface with keyboard navigation
- **Dual-Panel Layout**: Left menu for navigation, right panel for task display
- **CRUD Operations**: Create, Read, Update, Delete tasks
- **Task Status Management**: Mark tasks as complete/incomplete
- **Color-Coded Display**: Visual indicators for task status and UI elements
- **Real-time Statistics**: Dynamic counters for pending/completed tasks
- **ASCII Art Header**: Professional and branded UI experience
- **Input Validation**: Robust validation with helpful error messages
- **Graceful Shutdown**: Proper cleanup on exit

## 🛠️ Tech Stack

- **Python 3.13+**: Modern Python with type hints and dataclasses
- **Curses Library**: Native terminal UI rendering
- **UV Package Manager**: Fast dependency management
- **pytest**: Comprehensive testing framework

## 📋 Requirements

- Python 3.13 or higher
- Terminal with minimum 80x24 dimensions
- Unix-like environment (Linux/macOS) - Windows support via WSL

## 🚀 Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd interactive-todo-app
   ```

2. **Create and activate virtual environment**:
   ```bash
   uv venv
   source .venv/bin/activate
   ```

3. **Install the application**:
   ```bash
   uv pip install -e .
   ```

## 💻 Usage

Run the application with:
```bash
todo-app
```

### Keyboard Navigation
- **UP/DOWN Arrows**: Navigate menu options
- **ENTER**: Select menu option or confirm
- **ESC**: Return to previous screen or cancel input
- **'q' Key**: Quit the application

### Available Operations
- **Add Task**: Create new tasks with title and description
- **View All Tasks**: See complete task list
- **View Pending Tasks**: See incomplete tasks only
- **View Completed Tasks**: See completed tasks only
- **Update Task**: Modify existing task title or description
- **Delete Task**: Remove tasks with confirmation
- **Mark Complete**: Mark tasks as completed
- **Mark Incomplete**: Mark completed tasks as pending

## 📁 Project Structure

```
src/todo_app/
├── models/
│   ├── task.py          # Task dataclass with validation
│   └── task_manager.py  # Business logic for task operations
├── views/
│   ├── cli_view.py      # Curses-based UI with color coding
│   └── constants.py     # Color schemes, display configs, messages
├── controllers/
│   └── app_controller.py # Input handling and app flow
```

## 🧪 Testing

Run the test suite:
```bash
python -m pytest tests/ -v
```

The application includes 56 comprehensive tests covering:
- Unit tests for all models and components
- Integration tests for full application flow
- Navigation and UI interaction tests
- Error handling validation

## 🏗️ Architecture

The application follows a clean MVC (Model-View-Controller) architecture:

- **Models**: Handle data and business logic (`Task`, `TaskManager`)
- **Views**: Manage UI rendering and display (`CliView`)
- **Controllers**: Handle input processing and application flow (`AppController`)

## ⌨️ User Interface

### Main Menu
```
╔════════════════════════════════════════════════════════════════════════════╗
║                             INTERACTIVE TODO APP                           ║
║                                v0.1.0                                      ║
║                                                                            ║
║                Manage your tasks with ease in the terminal!                ║
╚════════════════════════════════════════════════════════════════════════════╝
  > Add Task
    View All Tasks
    View Pending Tasks
    View Completed Tasks
    Update Task
    Delete Task
    Mark Complete
    Mark Incomplete
    Exit
```

### Task Display
- Tasks displayed with ID, title, and status
- Color-coded status indicators (Green for completed, White for pending)
- Real-time totals display: "Total: X | Pending: Y | Completed: Z"

## 🔧 Configuration

All UI and application constants are defined in `constants.py`:
- Color schemes and pairs
- Display dimensions and limits
- Menu options and messages
- ASCII art header

## 🛡️ Error Handling

- Input validation with character limits (100 for title, 500 for description)
- Proper error messages for invalid operations
- Graceful handling of non-existent tasks
- Terminal compatibility checks

## 🚨 Graceful Shutdown

The application handles system signals (SIGINT, SIGTERM) for proper cleanup and displays a goodbye message upon exit.

## 📝 License

[Specify your license here]

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the full test suite
6. Submit a pull request

## 🐛 Issues

If you encounter any issues, please open an issue in the repository with:
- Detailed description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Environment information