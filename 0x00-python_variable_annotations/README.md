# 0x00. Python - Variable Annotations

## Learning Objectives

### General

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

Type annotations in Python 3
How you can use type annotations to specify function signatures and variable types
Duck typing
How to validate your code with mypy

## Requirements
### General
Allowed editors: vi, vim, emacs
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
All your files should end with a new line
The first line of all your files should be exactly #!/usr/bin/env python3
A README.md file, at the root of the folder of the project, is mandatory
Your code should use the pycodestyle style (version 2.5.)
All your files must be executable
The length of your files will be tested using wc
All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## tasks

1. Basic Annotations - Add
2. Basic Annotations - Concat
3. Basic Annotations - Floor
4. Basic Annotations - To String
5. Define Variables
6. Complex Types - List of Floats
7. Complex Types - Mixed List
8. Complex Types - String and Int/Float to Tuple
9. Complex Types - Functions
10. Duck Typing - Iterable Object

## Basic Annotations - Add

**File:** `0-add.py`

Write a type-annotated function `add` that takes two floats `a` and `b` as arguments and returns their sum as a float.

```python
def add(a: float, b: float) -> float:
    return a + b

