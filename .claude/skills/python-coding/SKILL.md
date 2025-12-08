---
name: python-coding
description: >
  Python coding skill focused on writing high-quality, production-ready code.
  Use this skill when users request writing, refactoring, or reviewing Python code,
  especially when emphasizing: (1) code quality, (2) type safety, (3) error handling,
  (4) code organization, or (5) modern Python practices.
---

# Python Coding Guidelines

This skill provides comprehensive guidelines for writing high-quality, production-ready Python code.

## Core Principles

1.  **Code Quality First**: Prioritize readability, maintainability, and correctness over clever solutions.
2.  **Explicit Over Implicit**: Write clear, self-documenting code that doesn't require mental gymnastics.
3.  **Type Safety**: Always use type hints and leverage static type checking.
4.  **Defensive Programming**: Anticipate edge cases and handle errors gracefully.

## Code Standards

### Style and Formatting
-   Strictly follow **PEP 8** style guide.
-   Use 4 spaces for indentation (never tabs).
-   Limit lines to 79 characters (88 for Black formatter users).
-   Use descriptive variable names: `user_count` not `uc`.
-   Follow naming conventions:
    -   Functions/variables: `snake_case`
    -   Classes: `PascalCase`
    -   Constants: `UPPER_SNAKE_CASE`
    -   Private methods: `_leading_underscore`

### Type Hints and Documentation
-   **Always include type hints** for function parameters and return values.
-   Use modern type hint syntax (Python 3.9+): `list[str]` instead of `List[str]` when possible.
-   For complex types, import from `typing`: `Union`, `Optional`, `Callable`, `TypeVar`, etc.
-   Write comprehensive docstrings using **Google** or **NumPy** style:

```python
def process_user_data(
    user_id: int,
    filters: dict[str, Any] | None = None,
    validate: bool = True
) -> dict[str, Any]:
    """
    Process and validate user data with optional filtering.

    Args:
        user_id: Unique identifier for the user
        filters: Optional dictionary of filter criteria to apply
        validate: Whether to perform validation checks

    Returns:
        Processed user data dictionary containing validated fields

    Raises:
        ValueError: If user_id is invalid or data fails validation
        KeyError: If required fields are missing from the dataset

    Example:
        >>> process_user_data(123, {"status": "active"})
        {'id': 123, 'status': 'active', 'validated': True}
    """
    # Implementation here
    pass
```

### Error Handling

**Priority Order for Error Handling:**
1.  **Framework-provided error handling FIRST** (if working with a framework, use its built-in exceptions).
2.  **Standard library exceptions** for common cases.
3.  **Custom exceptions** only when framework/stdlib doesn't cover the use case.

**General Rules:**
-   Always prefer framework-provided error handling mechanisms when available.
-   Use specific exceptions, not bare `except:` clauses.
-   Catch specific exceptions you can handle, let others propagate.
-   Create custom exceptions **only** when framework/stdlib options don't exist.
-   Provide helpful error messages that guide debugging.
-   Use context managers (`with` statements) for resource management.
-   Log errors appropriately with proper logging levels.
-   Include relevant context in error messages (IDs, file paths, etc.).

**Standard Library Exception Examples:**
```python
import json
import logging
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

def load_config(filepath: Path) -> dict[str, Any]:
    """
    Load configuration file with comprehensive error handling.

    Args:
        filepath: Path to the configuration file

    Returns:
        Dictionary containing configuration data

    Raises:
        FileNotFoundError: If config file doesn't exist
        PermissionError: If file cannot be read due to permissions
        ValueError: If JSON is invalid or config is malformed
    """
    try:
        with filepath.open('r', encoding='utf-8') as f:
            config = json.load(f)

        # Validate required fields
        if 'version' not in config:
            raise ValueError("Config missing required 'version' field")

        return config

    except FileNotFoundError:
        logger.error(f"Configuration file not found: {filepath}")
        raise
    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in config file: {e}")
        raise ValueError(f"Invalid JSON in {filepath}: {e}") from e
    except PermissionError:
        logger.error(f"Permission denied reading config: {filepath}")
        raise
```

**Custom Exceptions (Use Sparingly):**
```python
class ConfigError(Exception):
    """Base exception for configuration-related errors."""
    pass

class ValidationError(Exception):
    """Raised when data validation fails."""

    def __init__(self, message: str, field: str | None = None):
        self.field = field
        super().__init__(message)

def validate_user_age(age: int, min_age: int = 18) -> None:
    """
    Validate user age meets minimum requirement.

    Args:
        age: User's age in years
        min_age: Minimum required age

    Raises:
        ValidationError: If age is below minimum or invalid
    """
    if age < 0:
        raise ValidationError("Age cannot be negative", field="age")

    if age < min_age:
        raise ValidationError(
            f"User must be at least {min_age} years old",
            field="age"
        )
```

### Code Organization
-   Break complex functions into smaller, single-responsibility functions.
-   Keep functions under 50 lines when possible.
-   Use early returns to reduce nesting.
-   Group related functionality into classes or modules.
-   Separate concerns: I/O, business logic, and data validation.

**Example of Good Function Decomposition:**
```python
def process_orders(orders: list[dict]) -> dict[str, Any]:
    """Process multiple orders and return summary statistics."""
    validated_orders = _validate_orders(orders)
    processed_orders = _apply_discounts(validated_orders)
    summary = _calculate_summary(processed_orders)
    return summary

def _validate_orders(orders: list[dict]) -> list[dict]:
    """Validate order data structure and contents."""
    return [order for order in orders if _is_valid_order(order)]

def _is_valid_order(order: dict) -> bool:
    """Check if single order has required fields."""
    required = {'order_id', 'customer_id', 'total'}
    return required.issubset(order.keys())
```

### Modern Python Practices
-   Use f-strings for string formatting: `f"User {name} has {count} items"`.
-   Leverage comprehensions for clarity: `[x**2 for x in range(10) if x % 2 == 0]`.
-   Use `pathlib.Path` instead of `os.path` for file operations.
-   Prefer `dataclasses` or `pydantic` models for structured data.
-   Use `Enum` for fixed sets of constants.
-   Utilize context managers and decorators when appropriate.

**Dataclass Example:**
```python
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class User:
    """Represents a user in the system."""
    user_id: int
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.now)
    is_active: bool = True
    roles: list[str] = field(default_factory=list)

    def __post_init__(self):
        """Validate data after initialization."""
        if not self.email or '@' not in self.email:
            raise ValueError(f"Invalid email: {self.email}")
```

**Enum Example:**
```python
from enum import Enum, auto

class OrderStatus(Enum):
    """Valid order status values."""
    PENDING = auto()
    PROCESSING = auto()
    SHIPPED = auto()
    DELIVERED = auto()
    CANCELLED = auto()

    def is_active(self) -> bool:
        """Check if order is in an active state."""
        return self in {self.PENDING, self.PROCESSING, self.SHIPPED}
```

## Edge Cases and Robustness

Always consider and handle:
-   Empty collections (lists, dicts, sets).
-   `None` values and optional parameters.
-   Zero, negative, and boundary values.
-   Large datasets (memory and performance implications).
-   Concurrent access (thread safety if applicable).
-   Invalid input types and malformed data.
-   File system errors (permissions, missing files).
-   Network errors (timeouts, connection failures).

Document assumptions and limitations explicitly in docstrings.

**Example:**
```python
def calculate_average(numbers: list[float]) -> float:
    """
    Calculate arithmetic mean of a list of numbers.

    Args:
        numbers: List of numeric values

    Returns:
        Average value

    Raises:
        ValueError: If list is empty
        TypeError: If list contains non-numeric values

    Note:
        This function loads all numbers into memory. For very large
        datasets (>1M items), consider using a streaming approach.
    """
    if not numbers:
        raise ValueError("Cannot calculate average of empty list")

    if not all(isinstance(n, (int, float)) for n in numbers):
        raise TypeError("All elements must be numeric")

    return sum(numbers) / len(numbers)
```

## Performance Considerations

-   Use appropriate data structures (set for membership, dict for lookups).
-   Avoid premature optimization, but be aware of O(n²) operations.
-   Use generators for large datasets.
-   Profile before optimizing (don't guess bottlenecks).
-   Document performance characteristics for complex operations.

**Generator Example:**
```python
import json
from pathlib import Path
from typing import Generator

def process_large_file(filepath: Path) -> Generator[dict, None, None]:
    """
    Process large file line-by-line without loading into memory.

    Yields:
        Parsed data dictionary for each line

    Note:
        Uses generator to handle files larger than available memory.
    """
    with filepath.open('r', encoding='utf-8') as f:
        for line in f:
            if line.strip():
                yield json.loads(line)
```

## Dependencies and Imports

-   Group imports: stdlib, third-party, local (separated by blank lines).
-   Use absolute imports over relative imports.
-   Only import what you need: `from typing import Optional` not `import typing`.
-   Document why specialized libraries are used.
-   Prefer stdlib solutions when performance differences are negligible.

**Proper Import Organization:**
```python
# Standard library imports
import json
import logging
from pathlib import Path
from typing import Any, Optional

# Third-party imports
import requests
from pydantic import BaseModel

# Local application imports
from myapp.models import User
from myapp.utils import validate_email
```

## Testing Mindset

When writing code:
-   Write testable, pure functions when possible.
-   Avoid global state and side effects.
-   Include example usage in docstrings.
-   Consider what unit tests would look like.
-   Add inline comments for complex algorithms explaining the "why".

**Example with Test Considerations:**
```python
def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calculate discounted price.

    Args:
        price: Original price (must be >= 0)
        discount_percent: Discount percentage (0-100)

    Returns:
        Final price after discount

    Raises:
        ValueError: If price is negative or discount is out of range

    Example:
        >>> calculate_discount(100.0, 20.0)
        80.0
        >>> calculate_discount(50.0, 0.0)
        50.0
    """
    if price < 0:
        raise ValueError("Price cannot be negative")

    if not 0 <= discount_percent <= 100:
        raise ValueError("Discount must be between 0 and 100")

    return price * (1 - discount_percent / 100)
```

## Code Review Checklist

Before delivering code, verify:
-   [ ] All functions have type hints.
-   [ ] All public functions have docstrings.
-   [ ] Edge cases are handled.
-   [ ] Error messages are helpful.
-   [ ] Code follows PEP 8.
-   [ ] No hardcoded values (use constants or config).
-   [ ] Resource cleanup is handled (files, connections).
-   [ ] Code is DRY (Don't Repeat Yourself).
-   [ ] Comments explain "why" not "what".
-   [ ] Security considerations addressed (input validation, no injection risks, etc.).

## Logging Best Practices

```python
import logging

# Configure logging at module level
logger = logging.getLogger(__name__)

def process_data(data: dict) -> dict:
    """Process data with appropriate logging."""
    logger.debug(f"Processing data with {len(data)} items")

    try:
        result = transform_data(data)
        logger.info(f"Successfully processed {len(result)} items")
        return result
    except Exception as e:
        logger.error(f"Failed to process data: {e}", exc_info=True)
        raise
```

## Security Considerations

-   **Input Validation**: Always validate and sanitize user input.
-   **Path Traversal**: Use `Path.resolve()` and validate paths stay within expected directories.
-   **SQL Injection**: Use parameterized queries, never string concatenation.
-   **Command Injection**: Avoid `shell=True` in subprocess calls.
-   **Sensitive Data**: Never log passwords, tokens, or PII.
-   **Dependencies**: Keep libraries updated, check for known vulnerabilities.

**Example:**
```python
from pathlib import Path

def read_user_file(filename: str, base_dir: Path) -> str:
    """
    Safely read user-specified file within base directory.

    Args:
        filename: User-provided filename
        base_dir: Base directory to restrict access to

    Returns:
        File contents

    Raises:
        ValueError: If file path escapes base directory
        FileNotFoundError: If file doesn't exist
    """
    # Resolve paths to prevent directory traversal
    file_path = (base_dir / filename).resolve()

    # Ensure resolved path is within base directory
    if not file_path.is_relative_to(base_dir.resolve()):
        raise ValueError("Access denied: path outside base directory")

    return file_path.read_text(encoding='utf-8')
```

## Response Format

When providing code:
1.  Briefly explain the approach and design decisions.
2.  Present the complete, working implementation.
3.  Highlight important edge cases or gotchas.
4.  Suggest improvements or alternatives if relevant.
5.  Provide usage examples when appropriate.
