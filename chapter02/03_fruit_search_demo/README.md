# Python Fruit Search Demonstration

Welcome to the Python Fruit Search Demonstration! This script showcases various methods for checking the presence of items in a list, particularly focusing on searching for specific fruits. It's an ideal resource for both beginners learning Python and educators teaching basic programming concepts related to list operations and conditional structures.

## Script Overview 📘

The script first uses a traditional for-loop combined with a conditional statement to search for fruits in a predefined list. If the fruit is found, the loop breaks, and a message is printed. If not, after the loop concludes, another message indicates the fruit's absence. This demonstrates the use of the `else` clause on loops, which is a lesser-known but powerful feature.

### :computer: Script Code

```python
# List of fruits
fruits = ["Banana", "Orange", "Mango", "Grapes"]

# The fruit we want to check for
fruit_to_check = "Apple"

# Search for the fruit in the list
for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list.")
        break  # Exit the loop if the fruit is found
else:
    # This block is executed only if the loop is not broken (fruit not found)
    print(f"{fruit_to_check} is not in the list.")

# Additional example with another fruit
fruit_to_check = "Mango"

# Search for the fruit in the list
for fruit in fruits:
    if fruit == fruit_to_check:
        print(f"{fruit_to_check} is in the list.")
        break  # Exit the loop if the fruit is found
else:
    # This block is executed only if the loop is not broken (fruit not found)
    print(f"{fruit_to_check} is not in the list.")

# Pythonic and powerful method using 'in' keyword
print()
print("Why do Python devs never get lost? Because they always know where 'in' is!")
print("he he...") 

# Check if the fruit is in the list using a more Pythonic approach
fruit_to_check = "Grapes"
print(f"{fruit_to_check} is {'in' if fruit_to_check in fruits else 'not in'} the list.")
```

## Key Features 🌟
- **List Search**: Learn how to search for items in a list using traditional loops and conditions.
- **Use of `else` with Loops**: Understand how the `else` clause works with loops to handle cases when an item is not found.
- **Pythonic Techniques**: Discover the elegant and efficient way to check for item existence using the `in` keyword.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `03_fruit_search_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `03_fruit_search_demo.py`.
5. Run the script with: `python 03_fruit_search_demo.py`.

## Usage Example 📋
Execute the script to see how it checks the presence of various fruits in the list. This will help you understand basic list operations and the practical application of loop constructs in Python programming.

## 📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new examples!

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

