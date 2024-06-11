# 0x02. Python - Async Comprehension

## Learning Objectives
By the end of this project, you should be able to explain the following concepts without any external assistance:
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

## Requirements

### General
- Use only allowed editors: `vi`, `vim`, `emacs`
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using `python3` (version 3.7)
- Each file must end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Code should conform to the `pycodestyle` style (version 2.5.x)
- The length of your files will be tested using `wc`
- All modules should have a documentation string (use `python3 -c 'print(__import__("my_module").__doc__)'`)
- All functions should have a documentation string (use `python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- Documentation should be a full sentence explaining the purpose of the module, class, or method (length will be verified)
- All functions and coroutines must be type-annotated

## Tasks

### 0. Async Generator
**File:** `0-async_generator.py`  
**Mandatory**

Write a coroutine called `async_generator` that takes no arguments. The coroutine should loop 10 times, each time asynchronously waiting 1 second, then yielding a random number between 0 and 10.

### 1. Async Comprehensions
**File:** `1-async_comprehension.py`  
**Mandatory**

Import `async_generator` from the previous task and write a coroutine called `async_comprehension` that takes no arguments. This coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

### 2. Run time for four parallel comprehensions
**File:** `2-measure_runtime.py`  
**Mandatory**

Import `async_comprehension` from the previous task and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. The function should measure the total runtime and return it. Note that the total runtime should be roughly 10 seconds.

## Repository
- **GitHub repository:** `alx-backend-python`
- **Directory:** `0x02-python_async_comprehension`

