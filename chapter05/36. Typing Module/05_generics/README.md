# Demonstrating the Use of Generics in Python 🐍

This script demonstrates how to use the `TypeVar` and `Generic` features from the `typing` module in Python to create a generic `Stack` class. This class can operate on a variety of types, providing a flexible and reusable stack implementation.

## Script Overview 📘

The script defines a generic `Stack` class that can store items of any type. It includes methods to push items onto the stack and pop items off the stack.

### :computer: Script Code

```python
from typing import TypeVar, Generic, List

# Allows defining functions and classes that can operate on a variety of types

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self.items: List[T] = []

    def push(self, item: T) -> None:
        """
        Pushes an item onto the stack.

        Parameters:
        item (T): The item to push onto the stack.
        """
        self.items.append(item)

    def pop(self) -> T:
        """
        Pops an item off the stack and returns it.

        Returns:
        T: The item popped off the stack.
        """
        return self.items.pop()
```

### Key Features 🌟
- **Generics**: Demonstrates the use of `TypeVar` and `Generic` to create a stack class that can operate on a variety of types.
- **Flexible Data Structure**: Provides a stack implementation that can store and manage items of any type.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Instantiate the `Stack` class with different types and use its `push` and `pop` methods to manage stack items of various types.

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