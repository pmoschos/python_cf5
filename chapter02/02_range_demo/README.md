# Understanding the `range()` Function in Python

Welcome to the Python `range()` Function Demonstration! This script showcases various methods for utilizing the `range()` function in loops, including different start, stop, and step parameters. It's an ideal resource for anyone new to Python or those teaching programming concepts related to iteration and range generation.

## Script Overview 📘

The script demonstrates how to use the `range()` function for generating sequences of numbers, performing loops with break and continue statements, utilizing nested loops, and understanding variable scope within loops.

### :computer: Script Code

```python
# The range function returns an object of class range.
# range(10)
# It generates a sequence of numbers starting from 0 by default and increments by 1
a = range(10)
print(f"a : {a}")  # Output: a : range(0, 10)
print(f"type(a): {type(a)}")  # Output: type(a): <class 'range'>

# Basic loop from 0 to 9
print("Loop from 0 to 9:")
for i in range(10):
    print(i, end=' ')
print("\n")

# Loop with a start, stop, and step
print("Loop from 1 to 9 with step of 3:")
for i in range(1, 10, 3):
    print(i, end=' ')
print("\n")

# Loop with a break statement
print("Loop from 0 to 9, breaking at 5:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
print("\n")

# Loop with a continue statement
print("Loop from 0 to 9, skipping 5:")
for i in range(10):
    if i == 5:
        continue
    print(i, end=' ')
print("\n")

# Loop with a break statement and else block
print("Loop from 0 to 9, breaking at 5, with else block:")
for i in range(10):
    if i == 5:
        break
    print(i, end=' ')
else:
    print("Loop ended normally")
print("\n")

# Loop with an else block executing after normal completion
print("Loop from 0 to 9, with else block (no break):")
for i in range(10):
    print(i, end=' ')
else:
    print("\nLoop ended normally")
print()

# Nested loops example
print("Nested loops example (multiplication table):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i * j}", end=' | ')
    print()
print()

# Using range with negative step
print("Loop from 10 to 1, decrementing by 2:")
for i in range(10, 0, -2):
    print(i, end=' ')
print("\n")

# Demonstrating that a for loop does not have its own scope in Python
# Iterate over a range of numbers and print each number
for num in range(10):
    print(num, end=' ')
print("\n-----")

# The variable num is still accessible here, outside the for loop
print("After the loop, num is still accessible")
print(f"num = {num}")
```

## Key Features 🌟

- **Basic Looping**: Understand how to use the `range()` function to create simple loops.
- **Advanced Looping**: Learn about using start, stop, and step parameters in the `range()` function.
- **Loop Control**: Discover how to use break and continue statements within loops.
- **Nested Loops**: Explore nested loops through a practical example.
- **Scope Demonstration**: Understand the scope of variables within loops.

## Technical Requirements 🔧

- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀

No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `02_range_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `02_range_demo.py`.
5. Run the script with: `python 02_range_demo.py`.

## Usage Example 📋

Execute the script to see how various `range()` function operations are performed in the console. This will help you understand the practical applications of `range()` in Python programming.

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