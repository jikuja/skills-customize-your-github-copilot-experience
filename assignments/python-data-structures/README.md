# 📘 Assignment: Python Data Structures

## 🎯 Objective

Explore Python's built-in data structures — lists, dictionaries, sets, and tuples — by writing functions that store, organize, and retrieve data in different ways.

## 📝 Tasks

### 🛠️	Work with Lists

#### Description
Write functions that create and manipulate a list of student names, practicing common list operations.

#### Requirements
Completed program should:

- Create a list of at least five student names
- Write a function `add_student(students, name)` that appends a name and returns the updated list
- Write a function `remove_student(students, name)` that removes a name if it exists and returns the updated list
- Write a function `find_student(students, name)` that returns `True` if the name is in the list, `False` otherwise

### 🛠️	Work with Dictionaries and Sets

#### Description
Use a dictionary to store student grades and a set to track unique subjects, practicing key-based access and set operations.

#### Requirements
Completed program should:

- Create a dictionary mapping at least three student names to their numeric grade (0–100)
- Write a function `get_grade(grades, name)` that returns the grade for a student, or `None` if not found
- Write a function `passing_students(grades)` that returns a list of names with a grade of 60 or above
- Create a set of subject names and demonstrate adding, removing, and checking membership

### 🛠️	Work with Tuples

#### Description
Use tuples to represent fixed records such as coordinates or student info, and practice unpacking and iteration.

#### Requirements
Completed program should:

- Create a list of tuples where each tuple holds a student's `(name, grade, subject)`
- Write a function `top_student(records)` that returns the name of the student with the highest grade
- Demonstrate tuple unpacking by printing each student's name, grade, and subject in a formatted string
