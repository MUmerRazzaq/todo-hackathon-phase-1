# Interactive CLI Todo Application

## Feature Description

An interactive command-line interface (CLI) application that allows users to manage their tasks through a menu-driven interface with real-time updates. The application will strictly separate the User Interface (CLI/View/Controller) logic from the Core Business Logic (Task Manager/Model) following MVC architecture principles.

## User Scenarios & Testing

### Primary User Flow
1. User launches the CLI application and sees a dual-panel interface with ASCII art header
2. User navigates through menu options using UP/DOWN arrows and ENTER to select
3. User performs CRUD+C operations (Add, View, Update, Delete, Mark Complete) on tasks
4. Task list updates in real-time after each operation
5. User can exit the application cleanly

### Acceptance Scenarios
- **AS A** user wanting organized task management via CLI, **I WANT** a menu-driven interface with real-time task updates, **SO THAT** I can efficiently manage my tasks without typing commands.
- **AS A** user, **I WANT** clear visual feedback with color coding and status indicators, **SO THAT** I can quickly understand the state of my tasks.
- **AS A** user, **I WANT** unique task IDs to prevent data corruption, **SO THAT** I can safely perform operations without accidentally affecting wrong tasks.

### Edge Cases
- Invalid task IDs entered by user
- Empty task lists
- Terminal size smaller than minimum requirements (80x24)
- Attempting to update/delete non-existent tasks

## Functional Requirements

### 1. UI/UX & Display Requirements
- **REQ-UI-001**: Application must display a colorful ASCII art header/logo that remains visible at all times
- **REQ-UI-002**: Interface must use a dual-panel layout with menu-driven selection on left and real-time task list on right
- **REQ-UI-003**: Dual-panel layout must render correctly at minimum terminal size of 80 columns wide by 24 rows high
- **REQ-UI-004**: Task format must display: `[ID] Title, Description snippet, [Status]`
- **REQ-UI-005**: Task list must update immediately after every successful action (Add, Delete, Update, Complete)
- **REQ-UI-006**: Status indicators must differentiate visually between `[incomplete]` and `[completed] ✓`
- **REQ-UI-007**: Application must use color coding: Green for success, Red for failure/errors, Yellow/Blue for navigation prompts/neutral status
- **REQ-UI-008**: Use `>` to indicate currently highlighted item (menu or task)
- **REQ-UI-009**: Display real-time totals: "Pending: X", "Completed: Y"

### 2. Functional & Navigation Requirements
- **REQ-FUNC-001**: All 5 core features must be fully functional: Add, View, Update, Delete, Mark Complete
- **REQ-FUNC-002**: All user actions (except input forms) must be initiated through menu selection, not command-line input
- **REQ-FUNC-003**: Primary task list panel must only display tasks with [incomplete] status
- **REQ-FUNC-004**: Keyboard navigation: UP/DOWN arrows navigate menus/lists, ENTER selects items, ESC returns to previous screen or main menu
- **REQ-FUNC-005**: Exception: ESC while in input field must cancel input and revert screen state
- **REQ-FUNC-006**: Data persistence is in-memory only, stored in a single, well-defined object by Model layer
- **REQ-FUNC-007**: Application must generate and manage unique Task IDs to prevent data corruption
- **REQ-FUNC-008**: All command arguments and data entry fields must have robust validation with helpful error messages

### 3. Code Quality Requirements
- **REQ-QUAL-001**: Strict adherence to Model-View-Controller (MVC) separation
- **REQ-QUAL-002**: Mandatory type hints for all public functions/methods
- **REQ-QUAL-003**: Comprehensive docstrings for all public functions/methods
- **REQ-QUAL-004**: Exhaustive error handling for invalid or missing inputs
- **REQ-QUAL-005**: All display text, colors, and magic numbers must be defined in a constants file

## Success Criteria

- **CRITERIA-001**: All 5 CRUD+C features (Add, Delete, Update, View, Mark Complete) are accessible and function correctly
- **CRITERIA-002**: Application generates unique Task IDs and prevents data corruption during operations
- **CRITERIA-003**: Input validation provides helpful, actionable error messages (e.g., "Error: ID '105' does not exist.")
- **CRITERIA-004**: Dual-panel layout renders correctly at minimum terminal size (80x24)
- **CRITERIA-005**: Real-time updates occur immediately after successful actions
- **CRITERIA-006**: All UI elements follow specified color coding and visual feedback standards
- **CRITERIA-007**: Keyboard navigation works as specified (UP/DOWN/ENTER/ESC)
- **CRITERIA-008**: MVC separation is strictly maintained with clear boundaries between UI and business logic

## Key Entities

### Task Entity
- **ID**: Unique identifier for each task (auto-generated)
- **Title**: Short title/description of the task
- **Description**: Detailed description of the task (optional)
- **Status**: Boolean indicating completion status (incomplete/completed)
- **Created**: Timestamp of when task was created (optional)

### System Components
- **Model Layer**: Task Manager responsible for business logic and data management
- **View Layer**: UI renderer responsible for displaying interface elements
- **Controller Layer**: Input handler responsible for processing user interactions
- **Constants Module**: Configuration values for colors, display text, and magic numbers

## Dependencies & Assumptions

### Dependencies
- Terminal/Console library for UI rendering (curses for Python - part of standard library)
- Standard input/output handling for user interactions

### Assumptions
- Users are comfortable with keyboard navigation
- Terminal supports color display
- Application runs in a standard terminal environment
- In-memory persistence is sufficient for session-based usage
- curses library will be used for terminal UI (part of Python standard library)
- Maximum 3 external dependencies will be used as per constraints

## Constraints & Out-of-Scope

### In Scope
- Interactive menu-driven CLI interface
- CRUD+C operations for task management
- Real-time display updates
- MVC architectural separation
- Input validation and error handling
- Color-coded visual feedback
- Keyboard navigation support

### Out of Scope
- Persistent storage (data lost on exit)
- GUI or web interface
- Priority/Tagging systems
- Search/Filter functionality
- User authentication
- Network synchronization
- Cross-platform compatibility beyond standard terminals