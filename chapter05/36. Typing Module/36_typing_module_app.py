from typing import List, Dict, Tuple, Callable, TypeVar, Generic, Union, Optional, Any

# Basic types
def process(value: Any) -> None:
    """
    Processes and prints the given value.

    Parameters:
    value (Any): The value to be processed.
    """
    print(f"Processing value: {value}")

# Union and Optional
def fetch_data(key: Union[int, str], default: Optional[str] = None) -> Optional[str]:
    """
    Fetches data based on the provided key.

    Parameters:
    key (Union[int, str]): The key to fetch data for.
    default (Optional[str]): The default value to return if no data is found.

    Returns:
    Optional[str]: The fetched data or the default value.
    """
    if isinstance(key, int):
        return f"Data for int key: {key}"
    elif isinstance(key, str):
        return f"Data for str key: {key}"
    return default

# Generic Collections
def handle_list(items: List[int]) -> None:
    """
    Handles a list of integers.

    Parameters:
    items (List[int]): The list of integers to handle.
    """
    print(f"Handling list of integers: {items}")

def handle_dict(mapping: Dict[str, int]) -> None:
    """
    Handles a dictionary with string keys and integer values.

    Parameters:
    mapping (Dict[str, int]): The dictionary to handle.
    """
    print(f"Handling dictionary: {mapping}")

# Tuple
def return_tuple() -> Tuple[int, str, float]:
    """
    Returns a tuple containing an integer, a string, and a float.

    Returns:
    Tuple[int, str, float]: A tuple with an integer, a string, and a float.
    """
    return (1, "hello", 3.14)

# Callable
def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    """
    Applies a function to two integers.

    Parameters:
    func (Callable[[int, int], int]): The function to apply.
    x (int): The first integer argument.
    y (int): The second integer argument.

    Returns:
    int: The result of applying the function to the arguments.
    """
    return func(x, y)

# Generics and TypeVar
T = TypeVar('T')

def get_first_element(elements: List[T]) -> T:
    """
    Returns the first element of a list.

    Parameters:
    elements (List[T]): The list of elements.

    Returns:
    T: The first element of the list.
    """
    return elements[0]

# Generic class
class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        """
        Returns the value stored in the container.

        Returns:
        T: The value stored in the container.
        """
        return self.value

def main():
    """
    Main function to demonstrate the usage of various type hints and generic programming in Python.
    """
    # Basic types
    process("Hello, World!")
    process(123)
    process([1, 2, 3])

    # Union and Optional
    print(fetch_data(42))
    print(fetch_data("key"))
    print(fetch_data(42, default="Default value"))
    print(fetch_data("key", default="Default value"))

    # Generic Collections
    handle_list([1, 2, 3, 4, 5])
    handle_dict({"one": 1, "two": 2, "three": 3})

    # Tuple
    t = return_tuple()
    print(f"Returned tuple: {t}")

    # Callable
    def add(x: int, y: int) -> int:
        return x + y

    result = apply_function(add, 10, 20)
    print(f"Result of apply_function: {result}")

    # Generics and TypeVar
    first_element = get_first_element([10, 20, 30])
    print(f"First element: {first_element}")

    # Generic class
    int_container = Container(123)
    str_container = Container("Hello")
    print(f"Integer container value: {int_container.get_value()}")
    print(f"String container value: {str_container.get_value()}")

if __name__ == "__main__":
    main()
