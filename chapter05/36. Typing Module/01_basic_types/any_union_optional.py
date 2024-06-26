from typing import Any, Union, Optional

def describe_value(value: Any) -> str:
    """
    Returns a string describing the type and value of the input.

    Parameters:
    value (Any): The value to describe.

    Returns:
    str: A description of the value's type and value.
    """
    return f"The value is of type {type(value).__name__} with value {value}"

def process_input(input_value: Union[int, str, None]) -> str:
    """
    Processes the input based on its type and returns a corresponding message.

    Parameters:
    input_value (Union[int, str, None]): The input value to process.

    Returns:
    str: A message describing the processing of the input value.
    """
    if input_value is None:
        return "Received a None value"
    elif isinstance(input_value, int):
        return f"Processing an integer: {input_value}"
    elif isinstance(input_value, str):
        return f"Processing a string: {input_value}"

def display_message(message: Optional[str]) -> None:
    """
    Displays a message if provided, otherwise indicates no message to display.

    Parameters:
    message (Optional[str]): The message to display, or None.
    """
    if message is None:
        print("No message to display.")
    else:
        print(f"Message: {message}")

def main() -> None:
    """
    Main function to test the describe_value, process_input, and display_message functions.
    """
    # Testing describe_value function
    print(describe_value(100))                  # Expected output: The value is of type int with value 100
    print(describe_value("Hello"))              # Expected output: The value is of type str with value Hello
    print(describe_value([1, 2, 3]))            # Expected output: The value is of type list with value [1, 2, 3]

    # Testing process_input function
    print(process_input(42))                    # Expected output: Processing an integer: 42
    print(process_input("Hello"))               # Expected output: Processing a string: Hello
    print(process_input(None))                  # Expected output: Received a None value

    # Testing display_message function
    display_message("Welcome!")                 # Expected output: Message: Welcome!
    display_message(None)                       # Expected output: No message to display.

if __name__ == "__main__":
    main()

