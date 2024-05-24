# Demonstrating the Use of `Any` in Python 🐍

This script demonstrates how to use the `Any` type from the `typing` module in Python. The `process_value` function can accept arguments of any type and prints them.

## Script Overview 📘

The script defines a function, `process_value`, which processes and prints values of any type. The `main()` function demonstrates the usage of this function with different types of arguments.

### :computer: Script Code

```python
from typing import Any

def process_value(value: Any) -> None:
    """
    Processes and prints the given value.

    Parameters:
    value (Any): The value to be processed, can be of any type.
    """
    print(f"Processing value: {value}")

def main() -> None:
    """
    Main function to demonstrate the usage of the process_value function with different types of arguments.
    """
    # Examples of using Any
    process_value(10)                # An integer
    process_value("Hello")           # A string
    process_value([1, 2, 3])         # A list
    process_value({"key": "value"})  # A dictionary

if __name__ == "__main__":
    main()
```

### Key Features 🌟
- **Flexibility**: The `process_value` function can handle arguments of any type.
- **Type Hinting**: Demonstrates the use of the `Any` type from the `typing` module.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see the `process_value` function in action with various types of arguments.

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
