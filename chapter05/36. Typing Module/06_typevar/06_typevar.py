from typing import TypeVar
# Used to create generic types.

T = TypeVar('T')

def identity(x: T) -> T:
    return x
