# 0x03. Unittests and Integration Tests

## Description
This project focuses on unit testing and integration testing for backend development. The goal is to write tests to ensure that specific functions return expected results for various inputs and that the interactions between different parts of the code work as expected.

## Unit Testing
Unit testing involves testing individual functions to ensure they return expected results for different sets of inputs. It tests both standard inputs and edge cases. Unit tests should mock most calls to external functions, especially those making network or database calls.

### Key Concept
The main question a unit test should answer is: *If everything defined outside this function works as expected, does this function work as expected?*

## Integration Testing
Integration tests aim to test code paths end-to-end, ensuring that all parts of the code interact correctly. Typically, only low-level functions that make external calls (HTTP requests, file I/O, database I/O, etc.) are mocked.

### Key Concept
Integration tests verify the interactions between various parts of your code.

## Running Tests
To execute your tests, use the following command:
```sh
$ python -m unittest path/to/test_file.py

