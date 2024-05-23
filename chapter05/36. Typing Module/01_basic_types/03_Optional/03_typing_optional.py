from typing import Optional
# Optional: A shorthand for Union[T, None], representing a value that can be of type T or None.

def greet(name: Optional[str]) -> None:
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello, guest!")

# Examples of using Optional
greet("Alice")  # Hello, Alice!
greet(None)     # Hello, guest!
