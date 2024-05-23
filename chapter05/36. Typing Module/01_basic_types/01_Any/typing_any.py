from typing import Any
# Any: Represents any type.

def process_value(value: Any) -> None:
    print(f"Processing value: {value}")

# Examples of using Any
process_value(10)           # An integer
process_value("Hello")      # A string
process_value([1, 2, 3])    # A list
process_value({"key": "value"}) # A dictionary
