from typing import TypeVar

# Used to create generic types.

T = TypeVar('T')

def identity(x: T) -> T:
    """
    Returns the input value unchanged.

    Parameters:
    x (T): The input value of any type.

    Returns:
    T: The same value as the input.
    """
    return x

