# Python Average Calculation Function Demonstration

Welcome to the Python Average Calculation Function Demonstration! This script showcases how to calculate the average of three numbers and format the result. It's an ideal resource for anyone new to Python or those teaching programming concepts related to basic mathematical operations and string formatting.

## Script Overview 📘

The script includes a function called `get_average` which calculates the average of three given numbers and returns the result formatted to two decimal places. This demonstrates the use of arithmetic operations, function definition, parameter passing, and output formatting in Python.

### :computer: Script Code

```python
def get_average(num1: float, num2: float, num3: float) -> str:
    """
    Calculate the average of three numbers and format it to two decimal places.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    num3 (float): The third number.

    Returns:
    str: The average of the three numbers formatted to two decimal places.
    """
    return "{:.2f}".format((num1 + num2 + num3) / 3)

def main() -> None:
    """
    Main function to execute the program.
    """
    first_number = 10
    second_number = 20
    third_number = 15

    # Calculate the average of the provided numbers
    average = get_average(first_number, second_number, third_number)
    print("The average is:", average)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Function Definition and Defaults**: Learn how to define functions with default parameters.
- **Arithmetic Operations**: Understand how to perform arithmetic calculations and use them in practical applications.
- **String Formatting**: Discover how to format strings in Python to control how text and numbers are displayed.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `10_average_calculation_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `10_average_calculation_demo.py`.
5. Run the script with: `python 10_average_calculation_demo.py`.

## Usage Example 📋
Execute the script to see how the function calculates the average of three numbers and displays it formatted to two decimal places. This will help you understand the practical applications of basic math functions in Python programming.

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
