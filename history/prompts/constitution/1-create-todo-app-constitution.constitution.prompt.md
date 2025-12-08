---
id: 1
title: "Create Todo App Constitution"
stage: constitution
date_iso: "2025-12-08"
surface: "agent"
model: "claude-sonnet-4-5-20250929"
feature: "none"
branch: "master"
user: "user"
command: "/sp.constitution"
labels: ["constitution", "todo-app", "specification"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
  - ".specify/memory/constitution.md"
  - "history/prompts/constitution/1-create-todo-app-constitution.constitution.prompt.md"
tests_yaml: []
---

## Prompt Text

```
**Project:**Interactive CLI Todo Application with UI and in-memory storage

---

### Core Principles:
* **UI**: Clear minimal UI easy to navigate for non technical user.
* **Reliability:** The application must function correctly under normal usage patterns without crashing or losing tasks.
* **Usability:** Keyboard navigation: UP/DOWN/ENTER/ESC.
* **Maintainability:** Code must be modular, adhering to Python best practices, and easy for another developer to understand and extend.
* **Completeness:** All five specified core features (**Add, Delete, Update, View, Mark Complete**) must be fully implemented.

---

### Key Standards:

* **Code Style:** Adherence to **PEP 8** standards (checked with a linter like **Flake8**).
* **Type Hinting:** All major functions and methods must use **Python type hints**.
* **Documentation:** All public functions, classes, and methods must include **docstrings** (following a standard like **Google or NumPy** style).
* **Testing:** Basic unit tests must be written for the core business logic (e.g., task manipulation) to demonstrate functional correctness.

---

### Constraints:

* **Technology Stack:** Must use **UV** for dependency management and be compatible with **Python 3.13+**.
* **Storage:** Tasks must be stored **in-memory** only (no file I/O or database connection).
* **Dependencies:** Minimum external dependencies required; aim for a clean standard library implementation.
* **Project Structure:** Must follow a standard Python project layout (e.g., a source directory like `src/`, a `tests/` directory, and a root `pyproject.toml` file).

---

### Success Criteria:

* All 5 core features (**Add, Delete, Update, View, Mark Complete**) are functionally correct.
* The application can be installed and run via **UV** without errors.
* Linter checks (e.g., Flake8) pass with **zero warnings** for style violations.
* Core logic unit tests pass with **100% coverage** for the task-handling module.
```

## Response Text

Created the Interactive CLI Todo Application Constitution with the following sections:
- Core Principles: UI, Reliability, Usability, Maintainability, Completeness, Code Standards
- Key Standards: Code Style, Type Hinting, Documentation, Testing requirements
- Constraints: Technology Stack, Storage, Dependencies, Project Structure
- Success Criteria: Core features, UV compatibility, Linter checks, Test coverage
- Governance: Development and review requirements
- Version information: Version 1.0.0, Ratified and Amended on 2025-12-08

All placeholder tokens were replaced with concrete values from the user input, and the constitution document is now complete.

## Outcome

The project constitution has been successfully created with all specified principles and constraints properly documented. The constitution serves as the foundational governance document for the Interactive CLI Todo Application project.