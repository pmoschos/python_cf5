# Demonstrating the Use of `Union` in Python 🐍

This script demonstrates how to use the `Union` type from the `typing` module in Python. The `handle_input` function can accept arguments that are either integers or strings and prints them accordingly.

## Script Overview 📘

The script defines a function, `handle_input`, which processes and prints values based on their type (either integer or string). The `main()` function demonstrates the usage of this function with different types of arguments.

### :computer: Script Code

```python
from typing import Union

def handle_input(input_value: Union[int, str]) -> None:
    """
    Handles the input value based on its type and prints the appropriate message.

    Parameters:
    input_value (Union[int, str]): The input value to be handled, which can be an integer or a string.
    """
    if isinstance(input_value, int):
        print(f"Handling integer: {input_value}")
    elif isinstance(input_value, str):
        print(f"Handling string: {input_value}")

def main() -> None:
    """
    Main function to demonstrate the usage of the handle_input function with different types of arguments.
    """
    # Examples of using Union
    handle_input(42)        # Handling integer: 42
    handle_input("Hello")   # Handling string: Hello

if __name__ == "__main__":
    main()
```

### Key Features 🌟
- **Type Flexibility**: The `handle_input` function can handle arguments that are either integers or strings.
- **Type Hinting**: Demonstrates the use of the `Union` type from the `typing` module.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see the `handle_input` function in action with various types of arguments.

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