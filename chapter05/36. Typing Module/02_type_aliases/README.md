# Using Type Aliases in Python 🐍

This script demonstrates how to use the `TypeAlias` feature from the `typing` module in Python to create a type alias for better readability. The alias `Vector` is used to represent a list of floating-point numbers. The script includes functions to add vectors and scale a vector by a scalar.

## Script Overview 📘

The script defines a type alias `Vector` and two functions:
- `add_vectors`: Adds two vectors component-wise.
- `scale_vector`: Scales a vector by a scalar.

The `main()` function demonstrates the usage of these functions with example vectors.

### :computer: Script Code

```python
from typing import TypeAlias, List

# TypeAlias: Allows defining a type alias for better readability
Vector: TypeAlias = List[float]

def add_vectors(v1: Vector, v2: Vector) -> Vector:
    """
    Adds two vectors component-wise.

    Parameters:
    v1 (Vector): The first vector.
    v2 (Vector): The second vector.

    Returns:
    Vector: The component-wise sum of v1 and v2.
    """
    return [x + y for x, y in zip(v1, v2)]

def scale_vector(v: Vector, scalar: float) -> Vector:
    """
    Scales a vector by a scalar.

    Parameters:
    v (Vector): The vector to be scaled.
    scalar (float): The scalar to multiply each component by.

    Returns:
    Vector: The scaled vector.
    """
    return [x * scalar for x in v]

def main() -> None:
    """
    Main function to demonstrate the use of vector operations.
    """
    v1: Vector = [1.0, 2.0, 3.0]
    v2: Vector = [4.0, 5.0, 6.0]
    
    print("Vector addition:")
    result_add = add_vectors(v1, v2)
    print(f"{v1} + {v2} = {result_add}")
    
    scalar = 2.0
    print("\nVector scaling:")
    result_scale = scale_vector(v1, scalar)
    print(f"{v1} * {scalar} = {result_scale}")

if __name__ == "__main__":
    main()
```

### Key Features 🌟
- **Type Alias**: The `Vector` type alias improves code readability by clearly indicating that a list of floats represents a vector.
- **Vector Operations**: Functions to perform common vector operations, such as addition and scaling.
- **Type Hinting**: Demonstrates the use of type hinting for function parameters and return types.

### Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

### Usage Example 📋
Run the script directly in a Python environment to see the vector operations in action with different types of inputs.

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