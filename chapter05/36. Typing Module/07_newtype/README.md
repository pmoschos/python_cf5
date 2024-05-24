# Demonstrating the Use of `NewType` in Python 🐍

This script demonstrates how to use the `NewType` feature from the `typing` module in Python to create distinct types based on existing types. The `UserId` type is created to represent user IDs as distinct from other integers.

## Script Overview 📘

The script defines a new type, `UserId`, based on the integer type, and a function `get_user` that accepts a `UserId` as its parameter.

### :computer: Script Code

```python
from typing import NewType

# Allows creating distinct types based on existing types

UserId = NewType('UserId', int)

def get_user(user_id: UserId) -> None:
    """
    Retrieves a user based on their user ID.

    Parameters:
    user_id (UserId): The ID of the user to retrieve, represented as a distinct type.
    """
    pass
```

### Key Features 🌟
- **Distinct Types**: Demonstrates the use of `NewType` to create distinct types based on existing types for better type safety and code clarity.
- **Type Safety**: The `UserId` type ensures that user IDs are treated as a specific and distinct type, reducing the risk of type-related errors.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Use the `UserId` type to create and handle user IDs distinctly from other integers, and ensure type safety in functions like `get_user`.

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