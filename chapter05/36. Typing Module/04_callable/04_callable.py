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


