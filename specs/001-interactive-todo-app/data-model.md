# Data Model: Interactive CLI Todo Application

## Task Entity

### Attributes
- **id**: `int` - Unique identifier for each task (auto-incrementing integer)
- **title**: `str` - Short title/description of the task (required, max 100 chars)
- **description**: `str` - Detailed description of the task (optional, max 500 chars)
- **status**: `bool` - Boolean indicating completion status (default: False)
- **created_at**: `datetime` - Timestamp of when task was created (auto-generated)

### Dataclass Definition
```python
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:
    id: int
    title: str
    description: str = ""
    status: bool = False
    created_at: datetime = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()

    def mark_completed(self):
        self.status = True

    def mark_incomplete(self):
        self.status = False

    def update_title(self, new_title: str):
        if len(new_title.strip()) == 0:
            raise ValueError("Title cannot be empty")
        if len(new_title) > 100:
            raise ValueError("Title cannot exceed 100 characters")
        self.title = new_title.strip()

    def update_description(self, new_description: str):
        if len(new_description) > 500:
            raise ValueError("Description cannot exceed 500 characters")
        self.description = new_description
```

## TaskManager Entity

### Attributes
- **tasks**: `Dict[int, Task]` - Dictionary mapping task IDs to Task objects
- **next_id**: `int` - Next available ID for new tasks (auto-incrementing)

### Methods
- `add_task(title: str, description: str = "") -> Task`: Creates and adds a new task
- `get_task(task_id: int) -> Optional[Task]`: Retrieves a task by ID
- `get_all_tasks() -> List[Task]`: Returns all tasks
- `get_pending_tasks() -> List[Task]`: Returns only incomplete tasks
- `get_completed_tasks() -> List[Task]`: Returns only completed tasks
- `update_task(task_id: int, title: str = None, description: str = None) -> bool`: Updates a task's properties
- `delete_task(task_id: int) -> bool`: Removes a task by ID
- `mark_task_completed(task_id: int) -> bool`: Marks a task as completed
- `mark_task_incomplete(task_id: int) -> bool`: Marks a task as incomplete
- `get_task_count() -> int`: Returns total number of tasks
- `get_pending_count() -> int`: Returns number of pending tasks
- `get_completed_count() -> int`: Returns number of completed tasks

## State Management

### Application State
The application maintains state in-memory only:
- Tasks exist only during the current session
- No persistence to file or database
- All data is lost when the application exits

## Validation Rules

### Task Creation
- Title is required and must be 1-100 characters
- Description is optional and can be up to 500 characters
- ID is auto-generated and must be unique
- Status defaults to False (incomplete)

### Task Updates
- Title cannot be empty
- Title cannot exceed 100 characters
- Description cannot exceed 500 characters
- ID cannot be modified
- Only existing tasks can be updated

### Task Operations
- Operations (update, delete, mark complete) require valid task ID
- Non-existent task IDs result in appropriate error handling