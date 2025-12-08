# Interactive CLI Todo Application Constitution

## Core Principles

### UI
Clear minimal UI easy to navigate for non technical user.

### Reliability
The application must function correctly under normal usage patterns without crashing or losing tasks.

### Usability
Keyboard navigation: UP/DOWN/ENTER/ESC.

### Maintainability
Code must be modular, adhering to Python best practices, and easy for another developer to understand and extend.

### Completeness
All five specified core features (Add, Delete, Update, View, Mark Complete) must be fully implemented.

### Code Standards
All major functions and methods must use Python type hints and include docstrings following Google or NumPy style, while adhering to PEP 8 standards checked with Flake8.

## Key Standards

Code Style: Adherence to PEP 8 standards (checked with a linter like Flake8).
Type Hinting: All major functions and methods must use Python type hints.
Documentation: All public functions, classes, and methods must include docstrings (following a standard like Google or NumPy style).
Testing: Basic unit tests must be written for the core business logic (e.g., task manipulation) to demonstrate functional correctness.

## Constraints

Technology Stack: Must use UV for dependency management and be compatible with Python 3.13+.
Storage: Tasks must be stored in-memory only (no file I/O or database connection).
Dependencies: Minimum external dependencies required; aim for a clean standard library implementation.
Project Structure: Must follow a standard Python project layout (e.g., a source directory like `src/`, a `tests/` directory, and a root `pyproject.toml` file).

## Success Criteria

All 5 core features (Add, Delete, Update, View, Mark Complete) are functionally correct.
The application can be installed and run via UV without errors.
Linter checks (e.g., Flake8) pass with zero warnings for style violations.
Core logic unit tests pass with 100% coverage for the task-handling module.

## Governance

All development must follow the specified principles and constraints. Changes to this constitution require explicit approval and documentation of the rationale. Code reviews must verify compliance with all principles before merging.

**Version**: 1.0.0 | **Ratified**: 2025-12-08 | **Last Amended**: 2025-12-08
