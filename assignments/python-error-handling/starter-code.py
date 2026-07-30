
# Task 1: Catch and Handle Exceptions

def safe_divide(a, b):
    # TODO: return a / b, return None on ZeroDivisionError
    pass

def parse_integer(value):
    # TODO: return int(value), return None on ValueError
    pass


# Task 2: Use Finally and Multiple Except Clauses

def read_first_line(filename):
    # TODO: open file, return first line
    # Handle FileNotFoundError -> "File not found"
    # Handle PermissionError  -> "Access denied"
    # Use finally to ensure the file is closed
    pass


# Task 3: Raise Custom Exceptions

class InvalidAgeError(ValueError):
    pass  # TODO: optionally add custom __init__ with a message

def validate_age(age):
    # TODO: raise InvalidAgeError if age < 0 or age > 120
    pass
