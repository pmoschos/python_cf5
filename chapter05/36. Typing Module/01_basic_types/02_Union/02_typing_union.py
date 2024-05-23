from typing import Union
#Union: Represents a value that can be one of several specified types.

def handle_input(input_value: Union[int, str]) -> None:
    if isinstance(input_value, int):
        print(f"Handling integer: {input_value}")
    elif isinstance(input_value, str):
        print(f"Handling string: {input_value}")

# Examples of using Union
handle_input(42)        # Handling integer: 42
handle_input("Hello")   # Handling string: Hello
