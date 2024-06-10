# 0x01. Python - Async

## Project Overview
This project focuses on asynchronous programming in Python, specifically using the `asyncio` library. You'll learn to implement asynchronous coroutines, execute them concurrently, and manage tasks efficiently.

## Learning Objectives
By the end of this project, you should be able to:
- Understand and use `async` and `await` syntax.
- Execute an async program using `asyncio`.
- Run concurrent coroutines.
- Create `asyncio` tasks.
- Utilize the `random` module in asynchronous contexts.

## Requirements
- A `README.md` file at the root of the project folder is mandatory.
- Allowed editors: `vi`, `vim`, `emacs`.
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
- All files should end with a new line.
- All files must be executable.
- File length will be tested using `wc`.
- The first line of all files should be `#!/usr/bin/env python3`.
- Code should follow the `pycodestyle` style (version 2.5.x).
- All functions and coroutines must be type-annotated.
- All modules should have documentation.
- All functions should have documentation explaining their purpose.

## Tasks

### Task 0: The Basics of Async
Write an asynchronous coroutine `wait_random` that takes an integer argument `max_delay` (default value: 10) and waits for a random delay between 0 and `max_delay` (inclusive), then returns the delay.

**File**: `0-basic_async_syntax.py`

### Task 1: Execute Multiple Coroutines Concurrently with Async
Write an async routine `wait_n` that takes two integer arguments `n` and `max_delay`. It spawns `wait_random` `n` times with the specified `max_delay` and returns a list of all the delays in ascending order without using `sort()`.

**File**: `1-concurrent_coroutines.py`

### Task 2: Measure the Runtime
Write a function `measure_time` that measures the total execution time for `wait_n(n, max_delay)` and returns the total time divided by `n`.

**File**: `2-measure_runtime.py`

### Task 3: Tasks
Write a function `task_wait_random` that takes an integer `max_delay` and returns an `asyncio.Task`.

**File**: `3-tasks.py`

### Task 4: Tasks with Multiple Coroutines
Modify `wait_n` to create a new function `task_wait_n` that uses `task_wait_random`.

**File**: `4-tasks.py`

## Repository Structure
- **GitHub repository**: `alx-backend-python`
- **Directory**: `0x01-python_async_function`
- **Files**: 
  - `0-basic_async_syntax.py`
  - `1-concurrent_coroutines.py`
  - `2-measure_runtime.py`
  - `3-tasks.py`
  - `4-tasks.py`

Ensure all files are properly documented, executable, and follow the project requirements.

