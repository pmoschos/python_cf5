# Python List CRUD Functions Demonstration

Welcome to the Python List CRUD Functions Demonstration! This script showcases various methods for manipulating lists in Python, including creating, reading, updating, and deleting elements. It's an ideal resource for anyone new to Python or those teaching programming concepts related to list operations.

## Script Overview 📘

The script demonstrates how to populate a list, iterate over it to read values and indices, and highlights the scope behavior of variables used in loops.

### :computer: Script Code

```python
# Populate a list
ages = [19, 23, 34, 45]
print("Initial list of ages:", ages)

# Read: Iterating over a list and accessing both the index and the value
print("\nIterating with index and value:")
for index, value in enumerate(ages):
    # Using enumerate() to get both index and value while iterating
    print(f"Index {index}: {value}")

# Iterating with enhanced for loop
print("\nIterating with enhanced for loop:")
for age in ages:
    # Simple iteration over the list values
    print(age, end=' ')
print()

# for loop does not have its own scope in Python
# The variable 'age' used in the for loop is still accessible here
print(f"age = {age}")
```

## Key Features 🌟

- **List Creation**: Learn how to initialize and populate lists in Python.
- **List Reading**: Understand different methods for iterating over lists and accessing both index and value.
- **Variable Scope in Loops**: Discover the behavior of variables used within for loops in Python and their scope.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `01_list_populate_traverse.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `01_list_populate_traverse.py`.
5. Run the script with: `python 01_list_populate_traverse.py`.

## Usage Example 📋

Execute the script to see how various list operations are performed in the console. This will help you understand the practical applications of list manipulation in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
