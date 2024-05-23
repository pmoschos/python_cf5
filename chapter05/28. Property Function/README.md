# Encapsulation and Property Management in Python

This script demonstrates the use of encapsulation and property management in Python using the `property()` function. It includes defining getter, setter, and deleter methods for a class attribute and dynamically adding new attributes to a class instance.

## Script Overview 📘

The script defines a `Person` class with a private attribute `_name` and manages access to this attribute using getter, setter, and deleter methods via the `property()` function. The `main()` function demonstrates how to use these properties and dynamically add new attributes to an instance of the class.

### :computer: Script Code

```python
class Person:
    def __init__(self, name):
        self._name = name  # Private attribute

    def get_name(self):
        print("Getting name")
        return self._name

    def set_name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        print("Setting name")
        self._name = value

    def del_name(self):
        print("Deleting name")
        del self._name

    # Create property using property() function
    # fget: A function for getting the attribute value.
    # fset: A function for setting the attribute value.
    # fdel: A function for deleting the attribute value.
    # doc:  A string that contains the documentation for the attribute.
    name = property(get_name, set_name, del_name, "This is the 'name' property")

def main():
    # Usage
    p = Person("John")
    print(p.name)       # Getting name -> John
    p.name = "Jane"     # Setting name
    print(p.name)       # Getting name -> Jane
    del p.name          # Deleting name

    # Add new property to person p
    p.friends = []
    p.friends.append("Bob")
    p.friends.append("Alice")

    print(f"\nPrinting friends:")
    for friend in p.friends:
        print(f" - {friend}")
    print()

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Encapsulation**: Learn how to use private attributes and manage access using getter, setter, and deleter methods.
- **Property Management**: Understand how to create properties in Python using the `property()` function.
- **Dynamic Attributes**: See how to dynamically add new attributes to an instance of a class.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `28_property_function.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `28_property_function.py`.
5. Run the script with: `python 28_property_function.py`.

## Usage Example 📋
Execute the script to see how encapsulation and property management work in Python. The script will demonstrate getting, setting, and deleting a property, as well as dynamically adding new attributes to a class instance.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
