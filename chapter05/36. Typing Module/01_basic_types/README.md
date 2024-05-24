# Demonstrating the Use of `Any`, `Union`, and `Optional` in Python 🐍

This script demonstrates how to use the `Any`, `Union`, and `Optional` types from the `typing` module in Python. The script includes functions to describe values, process input, and display messages based on different types of inputs.

## Script Overview 📘

The script defines three functions:
- `describe_value`: Describes the type and value of the input.
- `process_input`: Processes the input based on its type and returns a corresponding message.
- `display_message`: Displays a message if provided, otherwise indicates no message to display.

The `main()` function tests these functions with different types of inputs.

### :computer: Script Code

```python
from typing import Any, Union, Optional

def describe_value(value: Any) -> str:
    """
    Returns a string describing the type and value of the input.

    Parameters:
    value (Any): The value to describe.

    Returns:
    str: A description of the value's type and value.
    """
    return f"The value is of type {type(value).__name__} with value {value}"

def process_input(input_value: Union[int, str, None]) -> str:
    """
    Processes the input based on its type and returns a corresponding message.

    Parameters:
    input_value (Union[int, str, None]): The input value to process.

    Returns:
    str: A message describing the processing of the input value.
    """
    if input_value is None:
        return "Received a None value"
    elif isinstance(input_value, int):
        return f"Processing an integer: {input_value}"
    elif isinstance(input_value, str):
        return f"Processing a string: {input_value}"

def display_message(message: Optional[str]) -> None:
    """
    Displays a message if provided, otherwise indicates no message to display.

    Parameters:
    message (Optional[str]): The message to display, or None.
    """
    if message is None:
        print("No message to display.")
    else:
        print(f"Message: {message}")

def main() -> None:
    """
    Main function to test the describe_value, process_input, and display_message functions.
    """
    # Testing describe_value function
    print(describe_value(100))                  # Expected output: The value is of type int with value 100
    print(describe_value("Hello"))              # Expected output: The value is of type str with value Hello
    print(describe_value([1, 2, 3]))            # Expected output: The value is of type list with value [1, 2, 3]

    # Testing process_input function
    print(process_input(42))                    # Expected output: Processing an integer: 42
    print(process_input("Hello"))               # Expected output: Processing a string: Hello
    print(process_input(None))                  # Expected output: Received a None value

    # Testing display_message function
    display_message("Welcome!")                 # Expected output: Message: Welcome!
    display_message(None)                       # Expected output: No message to display.

if __name__ == "__main__":
    main()
```

### Key Features 🌟
- **Type Descriptions**: The `describe_value` function provides a description of the input value's type and value.
- **Type Handling**: The `process_input` function handles different types of input values and returns appropriate messages.
- **Conditional Display**: The `display_message` function displays a message if provided and indicates no message otherwise.
- **Type Hinting**: Demonstrates the use of the `Any`, `Union`, and `Optional` types from the `typing` module.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see the functions in action with different types of inputs.

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