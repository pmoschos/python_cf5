from typing import Any, Union, Optional

def describe_value(value: Any) -> str:
    return f"The value is of type {type(value).__name__} with value {value}"

def process_input(input_value: Union[int, str, None]) -> str:
    if input_value is None:
        return "Received a None value"
    elif isinstance(input_value, int):
        return f"Processing an integer: {input_value}"
    elif isinstance(input_value, str):
        return f"Processing a string: {input_value}"

def display_message(message: Optional[str]) -> None:
    if message is None:
        print("No message to display.")
    else:
        print(f"Message: {message}")

# Testing the functions
print(describe_value(100))                  # The value is of type int with value 100
print(describe_value("Hello"))              # The value is of type str with value Hello
print(describe_value([1, 2, 3]))            # The value is of type list with value [1, 2, 3]

print(process_input(42))                    # Processing an integer: 42
print(process_input("Hello"))               # Processing a string: Hello
print(process_input(None))                  # Received a None value

display_message("Welcome!")                 # Message: Welcome!
display_message(None)                       # No message to display.
