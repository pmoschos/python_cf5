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

