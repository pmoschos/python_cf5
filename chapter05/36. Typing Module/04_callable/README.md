# Demonstrating the Use of `Callable` in Python 🐍

This script demonstrates how to use the `Callable` type from the `typing` module in Python to define functions that can accept other functions as arguments. The script includes examples of functions that add and multiply integers, and a higher-order function that executes these operations.

## Script Overview 📘

The script defines a higher-order function, `execute`, that takes a function and two integers as arguments. It also includes example functions, `add` and `multiply`, which are used to demonstrate the `execute` function.

### :computer: Script Code

```python
from typing import Callable

# Represents a function or method with a specific signature

# Function that executes a given function with two integer arguments
# The Callable type hint indicates that 'func' is a function that takes two integers as arguments and returns an integer
def execute(func: Callable[[int, int], int], x: int, y: int) -> int:
    """
    Executes a given function with two integer arguments.

    Parameters:
    func (Callable[[int, int], int]): A function that takes two integers as arguments and returns an integer.
    x (int): The first integer argument.
    y (int): The second integer argument.

    Returns:
    int: The result of the function call.
    """
    return func(x, y)

# Example usage:
# Define a function that adds two integers
def add(a: int, b: int) -> int:
    return a + b

# Define a function that multiplies two integers
def multiply(a: int, b: int) -> int:
    return a * b

# Execute the 'add' function with arguments 3 and 4
result_add = execute(add, 3, 4)
print(result_add)  # Output: 7

# Execute the 'multiply' function with arguments 3 and 4
result_multiply = execute(multiply, 3, 4)
print(result_multiply)  # Output: 12
```

### Key Features 🌟
- **Higher-Order Functions**: Demonstrates the use of higher-order functions by passing functions as arguments.
- **Type Hinting**: Uses the `Callable` type hint to specify the expected signature of functions passed as arguments.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see how the `execute` function can be used to perform different operations based on the function passed as an argument.

## 📢 Stay Updated

Be sure to ⭐ this repository to stay updated with new examples and enhancements!

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