# Python List Manipulation Functions Demonstration

Welcome to the Python List Manipulation Functions Demonstration! This script showcases various methods for managing lists in Python, including adding, updating, and deleting elements, as well as accessing list items. It's an ideal resource for anyone new to Python or those teaching programming concepts related to list operations.

## Script Overview 📘

The script begins by populating a list of fruits and then proceeds through a series of operations to modify the list in various ways. Each step demonstrates a different aspect of list manipulation, from appending items to removing them, illustrating the flexibility and power of lists in Python.

### :computer: Script Code

```python
# Populate
fruits = ["Apple", "Banana", "Cherry", "Apple"]
print("Initial list of fruits:", fruits)

# Add
fruits.append("Berry")  # Adding a single element
print("After appending 'Berry':", fruits)

fruits.extend(["Fig", "Grape"])  # Adding multiple elements
print("After extending with ['Fig', 'Grape']:", fruits)

fruits.insert(2, "Coconut")  # Inserting an element at a specific index
print("After inserting 'Coconut' at index 2:", fruits)

# Update
fruits[1] = "Blueberry"  # Updating an element at a specific index
print("\nAfter updating index 1 to 'Blueberry':", fruits)

fruits[2:4] = ["Melon", "Dragonfruit"]  # Updating a slice of the list
print("After updating slice from index 2 to 4:", fruits)

# Delete
removed_fruit = fruits.pop(3)  # Removing an element by index
print(f"\nAfter popping index 3 (removed {removed_fruit}):", fruits)

fruits.remove("Blueberry")  # Removing an element by value
print("After removing 'Blueberry':", fruits)

# Read: Using list slicing to access parts of the list
print("\nSliced list (first three elements):", fruits[:3])
print("Sliced list (last three elements):", fruits[-3:])

# Using index() to find the position of an element
position = fruits.index("Melon")
print(f"\nThe position of 'Melon' in the list is: {position}")
```

## Key Features 🌟
- **List Addition and Expansion**: Demonstrates how to add single and multiple items to a list.
- **List Updates and Slicing**: Shows how to update individual items and slices within the list.
- **Item Removal Techniques**: Explore methods to remove items by index or by value.
- **Reading List Items**: Learn how to access list items directly and through slicing.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `04_list_manipulation_demo.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `04_list_manipulation_demo.py`.
5. Run the script with: `python 04_list_manipulation_demo.py`.

## Usage Example 📋
Execute the script to see how various list operations are performed in the console. This will help you understand the practical applications of list manipulation in Python programming.

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

