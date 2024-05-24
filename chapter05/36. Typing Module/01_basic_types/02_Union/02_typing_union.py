from typing import Union

def handle_input(input_value: Union[int, str]) -> None:
    """
    Handles the input value based on its type and prints the appropriate message.

    Parameters:
    input_value (Union[int, str]): The input value to be handled, which can be an integer or a string.
    """
    if isinstance(input_value, int):
        print(f"Handling integer: {input_value}")
    elif isinstance(input_value, str):
        print(f"Handling string: {input_value}")

def main() -> None:
    """
    Main function to demonstrate the usage of the handle_input function with different types of arguments.
    """
    # Examples of using Union
    handle_input(42)        # Handling integer: 42
    handle_input("Hello")   # Handling string: Hello

if __name__ == "__main__":
    main()

