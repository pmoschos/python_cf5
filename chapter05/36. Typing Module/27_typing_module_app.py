from typing import List, Dict, Tuple, Callable, TypeVar, Generic, Union, Optional, Any

# Basic types
def process(value: Any) -> None:
    print(f"Processing value: {value}")

# Union and Optional
def fetch_data(key: Union[int, str], default: Optional[str] = None) -> Optional[str]:
    if isinstance(key, int):
        return f"Data for int key: {key}"
    elif isinstance(key, str):
        return f"Data for str key: {key}"
    return default

# Generic Collections
def handle_list(items: List[int]) -> None:
    print(f"Handling list of integers: {items}")

def handle_dict(mapping: Dict[str, int]) -> None:
    print(f"Handling dictionary: {mapping}")

# Tuple
def return_tuple() -> Tuple[int, str, float]:
    return (1, "hello", 3.14)

# Callable
def apply_function(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

# Generics and TypeVar
T = TypeVar('T')

def get_first_element(elements: List[T]) -> T:
    return elements[0]

# Generic class
class Container(Generic[T]):
    def __init__(self, value: T):
        self.value = value

    def get_value(self) -> T:
        return self.value

def main():
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
