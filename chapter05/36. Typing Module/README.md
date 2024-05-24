# Demonstrating Advanced Type Hints in Python 🐍

This script demonstrates how to use various advanced type hints from the `typing` module in Python, including `Any`, `Union`, `Optional`, `List`, `Dict`, `Tuple`, `Callable`, `TypeVar`, and `Generic`. The script includes functions and classes that process different types of data using these type hints.

## Script Overview 📘

The script defines several functions and a generic class to showcase the usage of different type hints:

- **Basic Types**: `process` function that processes any type of value.
- **Union and Optional**: `fetch_data` function that fetches data based on a key that can be an integer or a string, with an optional default value.
- **Generic Collections**: `handle_list` and `handle_dict` functions that handle lists of integers and dictionaries with string keys and integer values.
- **Tuple**: `return_tuple` function that returns a tuple with an integer, a string, and a float.
- **Callable**: `apply_function` function that applies a given function to two integers.
- **Generics and TypeVar**: `get_first_element` function that returns the first element of a list, and `Container` class that stores and returns a value of any type.

### :computer: Script Code

```python
from typing import List, Dict, Tuple, Callable, TypeVar, Generic, Union, Optional, Any

# Basic types
def process(value: Any) -> None:
    print(f"Processing value: {value}")

# Union and Optional
def fetch_data(key: Union[int, str], default: Optional[str] = None) -> Optional[str]:
    if isinstance(key, int):
        return f"Data for int key: {key}"
    elif isinstance(key, str):
        return f"Data for str key: {key}"
    return default

# Generic Collections
def handle_list(items: List[int]) -> None:
    print(f"Handling list of integers: {items}")

def handle_dict(mapping: Dict[str, int]) -> None:
    print(f"Handling dictionary: {mapping}")

# Tuple
def return_tuple() -> Tuple[int, str, float]:
    return (1, "hello", 3.14)

# Callable
def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# Generics and TypeVar
T = TypeVar('T')

def get_first_element(elements: List[T]) -> T:
    return elements[0]

# Generic class
class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

def main():
    process("Hello, World!")
    process(123)
    process([1, 2, 3])

    print(fetch_data(42))
    print(fetch_data("key"))
    print(fetch_data(42, default="Default value"))
    print(fetch_data("key", default="Default value"))

    handle_list([1, 2, 3, 4, 5])
    handle_dict({"one": 1, "two": 2, "three": 3})

    t = return_tuple()
    print(f"Returned tuple: {t}")

    def add(x: int, y: int) -> int:
        return x + y

    result = apply_function(add, 10, 20)
    print(f"Result of apply_function: {result}")

    first_element = get_first_element([10, 20, 30])
    print(f"First element: {first_element}")

    int_container = Container(123)
    str_container = Container("Hello")
    print(f"Integer container value: {int_container.get_value()}")
    print(f"String container value: {str_container.get_value()}")

if __name__ == "__main__":
    main()
```

### Key Features 🌟
- **Advanced Type Hints**: Demonstrates the use of `Any`, `Union`, `Optional`, `List`, `Dict`, `Tuple`, `Callable`, `TypeVar`, and `Generic` to enhance type safety and code clarity.
- **Generic Programming**: Provides examples of generic functions and classes that can operate on a variety of types.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see how various type hints and generic programming features are used to handle different types of data.

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