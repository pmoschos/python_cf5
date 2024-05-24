from typing import Any

def process_value(value: Any) -> None:
    """
    Processes and prints the given value.

    Parameters:
    value (Any): The value to be processed, can be of any type.
    """
    print(f"Processing value: {value}")

def main() -> None:
    """
    Main function to demonstrate the usage of the process_value function with different types of arguments.
    """
    # Examples of using Any
    process_value(10)                # An integer
    process_value("Hello")           # A string
    process_value([1, 2, 3])         # A list
    process_value({"key": "value"})  # A dictionary

if __name__ == "__main__":
    main()

