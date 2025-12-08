# API Contracts: Interactive CLI Todo Application

## Task Management API

### Task Creation
```
Method: POST
Endpoint: N/A (in-memory operation)
Input:
  - title: string (required, 1-100 chars)
  - description: string (optional, 0-500 chars)
Output:
  - Task object with generated ID
  - Success boolean
Errors:
  - ValidationError: If title is invalid
```

### Task Retrieval
```
Method: GET
Endpoint: N/A (in-memory operation)
Input:
  - task_id: integer
Output:
  - Task object or null if not found
Errors:
  - None (returns null for invalid IDs)
```

### Task Update
```
Method: PUT
Endpoint: N/A (in-memory operation)
Input:
  - task_id: integer
  - title: string (optional, 1-100 chars)
  - description: string (optional, 0-500 chars)
Output:
  - Success boolean
Errors:
  - ValidationError: If inputs are invalid
  - NotFoundError: If task_id doesn't exist
```

### Task Deletion
```
Method: DELETE
Endpoint: N/A (in-memory operation)
Input:
  - task_id: integer
Output:
  - Success boolean
Errors:
  - NotFoundError: If task_id doesn't exist
```

### Task Completion Toggle
```
Method: PATCH
Endpoint: N/A (in-memory operation)
Input:
  - task_id: integer
  - status: boolean (True for completed, False for incomplete)
Output:
  - Success boolean
Errors:
  - NotFoundError: If task_id doesn't exist
```

## CLI Interface Contracts

### Input Validation
- All user inputs must be validated before processing
- Task IDs must be positive integers
- Task titles/descriptions must meet length requirements
- Invalid inputs must return helpful error messages

### Output Format
- All tasks displayed as: `[ID] Title, Description snippet, [Status]`
- Status displayed as: `[incomplete]` or `[completed] ✓`
- Real-time totals: "Pending: X", "Completed: Y"
- Error messages: "Error: [descriptive message]"

### User Interaction Contracts
- UP/DOWN arrows navigate through lists/menus
- ENTER selects highlighted items
- ESC returns to previous screen or main menu
- ESC during input cancels the operation