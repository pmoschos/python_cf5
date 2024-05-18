# Python City Listing Function Demonstration

Welcome to the Python City Listing Function Demonstration! This script showcases a function that prints a list of cities in a formatted string, separated by commas. It's an excellent resource for anyone learning Python or those teaching programming concepts related to handling variable numbers of arguments and string manipulation.

## Script Overview 📘

The script includes a function called `print_cities` which takes any number of city names as arguments and prints them in a formatted list. If no cities are provided, it outputs a default message. This demonstrates the flexibility of using variadic parameters in Python functions.

### :computer: Script Code

```python
def print_cities(*cities):
    """
    Print a list of cities separated by commas.

    Parameters:
    *cities (str): A variable number of city names to be printed.
    """
    if not cities:
        print("No cities provided.")
    else:
        print("Cities:", ", ".join(cities))

def main():
    # Demonstrate various calls to print_cities function
    print_cities("Athens", "Paris", "London")
    print_cities("London")
    print_cities("New York", "Tokyo", "Berlin", "Sydney")
    print_cities()

    # Print cities separated by commas using print_cities function
    print("--------------------------------")
    print_cities("Athens", "Paris", "London")

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Variadic Parameters**: Learn how to handle functions with a variable number of arguments, allowing for flexibility in how many items can be processed at a time.
- **String Manipulation**: Understand how to manipulate strings and use string methods like `join()` to format output elegantly.
- **Conditional Logic**: Discover how to implement conditional checks within functions to handle different input scenarios effectively.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `12_varargs_func_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `12_varargs_func_demo.py`.
5. Run the script with: `python 12_varargs_func_demo.py`.

## Usage Example 📋
Execute the script to see how the function manages and formats different sets of input city names. This will help you understand the practical applications of handling variable-length argument lists in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the [MIT License](https://mit-license.org/).

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 *Note: This is a Python script and requires a Python interpreter to run.*

---
<h1 align=center>Happy Coding 👨‍💻 </h1>

<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
