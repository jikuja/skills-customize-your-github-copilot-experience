# 📘 Assignment: Python Error Handling

## 🎯 Objective

Learn to write robust Python programs by using `try/except/finally` blocks, raising custom exceptions, and gracefully recovering from runtime errors.

## 📝 Tasks

### 🛠️	Catch and Handle Exceptions

#### Description
Practice catching common runtime errors so your program can respond gracefully instead of crashing.

#### Requirements
Completed program should:

- Write a function `safe_divide(a, b)` that returns the result of `a / b`
- Catch a `ZeroDivisionError` and return `None` instead of crashing
- Write a function `parse_integer(value)` that converts a string to an integer
- Catch a `ValueError` and return `None` when the conversion fails

Example:
```python
safe_divide(10, 2)   # → 5.0
safe_divide(10, 0)   # → None
parse_integer("42")  # → 42
parse_integer("abc") # → None
```

### 🛠️	Use Finally and Multiple Except Clauses

#### Description
Extend your error handling to cover multiple exception types and use `finally` to run cleanup code regardless of whether an error occurred.

#### Requirements
Completed program should:

- Write a function `read_first_line(filename)` that opens a file and returns its first line
- Handle `FileNotFoundError` by returning `"File not found"`
- Handle `PermissionError` by returning `"Access denied"`
- Use a `finally` block to ensure the file is always closed if it was opened

### 🛠️	Raise Custom Exceptions

#### Description
Define your own exception classes to communicate specific error conditions clearly to the caller.

#### Requirements
Completed program should:

- Define a custom exception class `InvalidAgeError` that inherits from `ValueError`
- Write a function `validate_age(age)` that raises `InvalidAgeError` if `age` is less than 0 or greater than 120
- Demonstrate catching `InvalidAgeError` separately from other `ValueError` exceptions
- Include a descriptive message in the raised exception
