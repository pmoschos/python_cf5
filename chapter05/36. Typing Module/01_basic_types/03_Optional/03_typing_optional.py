from typing import Optional

def greet(name: Optional[str]) -> None:
    """
    Prints a greeting message.

    If the provided name is not None, it prints "Hello, {name}!".
    Otherwise, it prints "Hello, guest!".

    Parameters:
    name (Optional[str]): The name of the person to greet, or None for a generic greeting.
    """
    if name is not None:
        print(f"Hello, {name}!")
    else:
        print("Hello, guest!")

def main() -> None:
    """
    The main function to demonstrate the use of the greet function with different inputs.
    """
    # Example usages of the greet function
    greet("Alice")  # Expected output: Hello, Alice!
    greet(None)     # Expected output: Hello, guest!

if __name__ == "__main__":
    main()

