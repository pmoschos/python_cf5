# Inventory Management System in Python

This script demonstrates an inventory management system in Python, which includes custom exception handling for out-of-stock items and basic inventory operations like adding and removing items.

## Script Overview 📘

The project includes two main files: `store.py` and `app.py`. The `store.py` file defines the classes and functionality for the inventory system, including a custom exception for out-of-stock items. The `app.py` file demonstrates the usage of these classes and handles various inventory operations.

### :computer: Script Code

#### store.py
```python
class OutOfStockError(Exception):
    """
    Custom exception to be raised when an item is out of stock.
    """
    def __init__(self, item_name):
        super().__init__(f"{item_name} is out of stock")

class Item:
    """
    Represents an item in the inventory.
    
    Attributes:
        name (str): The name of the item.
        quantity (int): The quantity of the item in stock.
    """
    def __init__(self, name, quantity):
        """
        Initializes the item with a name and quantity.
        
        Parameters:
            name (str): The name of the item.
            quantity (int): The quantity of the item.
        """
        self.name = name
        self.quantity = quantity

    def __str__(self):
        """
        Returns a string representation of the item.
        """
        return f"{self.name}, {self.quantity}"
    
    def __eq__(self, other):
        """
        Checks equality based on the item name.
        
        Parameters:
            other (Item): The other item to compare.
        
        Returns:
            bool: True if the item names are the same, False otherwise.
        """
        if not isinstance(other, Item):
            return False
        return self.name == other.name
    
    def __hash__(self):
        """
        Returns a hash value for the item based on its name.
        
        Returns:
            int: The hash value of the item name.
        """
        return hash(self.name)

class Inventory:
    """
    Represents an inventory of items.
    
    Attributes:
        items (list): A list of items in the inventory.
    """
    def __init__(self):
        """
        Initializes the inventory with an empty list of items.
        """
        self.items = []
    
    def add_item(self, item):
        """
        Adds an item to the inventory. If the item already exists, its quantity is updated.
        
        Parameters:
            item (Item): The item to add.
        """
        for existing_item in self.items:
            if existing_item == item:
                existing_item.quantity += item.quantity
                return
        self.items.append(item)
    
    def remove_item(self, item_name_to_remove):
        """
        Removes an item from the inventory. If the item is not found or out of stock, raises an error.
        
        Parameters:
            item_name_to_remove (str): The name of the item to remove.
        
        Returns:
            Item: The item with updated quantity after removal.
        
        Raises:
            ValueError: If the item is not found in the inventory.
            OutOfStockError: If the item is out of stock.
        """
        # Check if the item exists in the inventory
        if Item(item_name_to_remove, None) not in self.items:
            raise ValueError(f"{item_name_to_remove} is not in the inventory")
        
        # Find the item and update its quantity
        for item in self.items:
            if item == Item(item_name_to_remove, None):
                if item.quantity > 0:
                    item.quantity -= 1
                    return Item(item.name, item.quantity)
                else:
                    raise OutOfStockError(item.name)

    def print_items(self):
        """
        Prints all items in the inventory.
        """
        for item in self.items:
            print(item)
```

#### app.py
```python
from store import * # Inventory, Item, OutOfStockError

def main():
    """
    Main function to demonstrate the functionality of the inventory system.
    """
    # Create an inventory
    inventory = Inventory()
    
    # Add items to inventory
    inventory.add_item(Item("Apple", 10))
    inventory.add_item(Item("Banana", 5))
    inventory.add_item(Item("Apple", 5))  # Increase quantity of existing item
    
    # Print current inventory
    print("Current inventory:")
    inventory.print_items()
    
    # Remove an item from inventory
    print("\nRemoving an Apple...")
    inventory.remove_item("Apple")
    inventory.print_items()
    
    # Try to remove an item not in inventory
    try:
        inventory.remove_item("Orange")
    except ValueError as e:
        print(e)
    
    # Try to remove more items than available
    try:
        for _ in range(20):
            inventory.remove_item("Banana")
    except OutOfStockError as e:
        print(e)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Custom Exceptions**: Learn how to create and use custom exceptions in Python.
- **Inventory Management**: Understand how to manage inventory by adding and removing items.
- **Error Handling**: See how to handle errors gracefully when items are not found or out of stock.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the scripts as `store.py` and `app.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing these files.
5. Run the script with: `python app.py`.

## Usage Example 📋
Execute the script to see how the inventory management system works in Python. The script will demonstrate adding items to the inventory, removing items, and handling errors when items are out of stock or not found.

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
