# Demonstrating the Use of `Optional` in Python 🐍

This script demonstrates how to use the `Optional` type from the `typing` module in Python. The `greet` function can accept a string or `None` and prints an appropriate greeting message.

## Script Overview 📘

The script defines a function, `greet`, which prints a greeting message based on whether a name is provided or not. The `main()` function demonstrates the usage of this function with different inputs.

### :computer: Script Code

```python
from typing import Optional

def greet(name: Optional[str]) -> None:
    """
    Prints a greeting message.

    If the provided name is not None, it prints "Hello, {name}!".
    Otherwise, it prints "Hello, guest!".

    Parameters:
    name (Optional[str]): The name of the person to greet, or None for a generic greeting.
    """
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello, guest!")

def main() -> None:
    """
    The main function to demonstrate the use of the greet function with different inputs.
    """
    # Example usages of the greet function
    greet("Alice")  # Expected output: Hello, Alice!
    greet(None)     # Expected output: Hello, guest!

if __name__ == "__main__":
    main()
```

### Key Features 🌟
- **Conditional Greetings**: The `greet` function provides a personalized greeting if a name is provided and a generic greeting if no name is given.
- **Type Hinting**: Demonstrates the use of the `Optional` type from the `typing` module.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see the `greet` function in action with different types of inputs.

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