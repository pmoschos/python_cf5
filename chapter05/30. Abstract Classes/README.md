# Abstract Base Classes in Python

This script demonstrates the use of Abstract Base Classes (ABC) in Python to define common interfaces for different implementations. It includes examples of a student DAO (Data Access Object) and an inventory management system.

## Script Overview 📘

The script defines abstract base classes for a student DAO and an inventory management system. It then implements these interfaces in concrete classes, demonstrating how to enforce method definitions in subclasses.

### :computer: Script Code

```python
from abc import ABC, abstractmethod

class AbstractStudentDAO(ABC):
    """Defines the Student DAO API"""

    @abstractmethod
    def insert(self, student):
        """Insert a new student"""
        raise NotImplementedError()
    
    @abstractmethod
    def update(self, student_id, student):
        """Update an existing student"""
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self, student_id):
        """Delete a student"""
        raise NotImplementedError()
    
    @abstractmethod
    def getOne(self, student_id):
        """Get a student by ID"""
        raise NotImplementedError()

class StudentImpl(AbstractStudentDAO):
    def __init__(self):
        self.students = {}

    def insert(self, student):
        student_id = student['id']
        self.students[student_id] = student
        print(f"Inserted student with ID: {student_id}")

    def update(self, student_id, student):
        if student_id in self.students:
            self.students[student_id] = student
            print(f"Updated student with ID: {student_id}")
        else:
            print(f"Student with ID: {student_id} not found")

    def delete(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
            print(f"Deleted student with ID: {student_id}")
        else:
            print(f"Student with ID: {student_id} not found")

    def getOne(self, student_id):
        return self.students.get(student_id, None)

class ABCInventory(ABC):

    @abstractmethod
    def add_item(self, item):
        """Add an item to the inventory"""
        pass

    @abstractmethod
    def remove_item(self, item_name_to_remove):
        """Remove an item from the inventory"""
        pass

class Inventory(ABCInventory):
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add an item to the inventory"""
        self.items.append(item)
        print(f"Added item: {item}")

    def remove_item(self, item_name_to_remove):
        """Remove an item from the inventory by name"""
        for item in self.items:
            if item.name == item_name_to_remove:
                self.items.remove(item)
                print(f"Removed item: {item_name_to_remove}")
                return
        print(f"Item not found: {item_name_to_remove}")

class Item:
    def __init__(self, name):
        self.name = name
        
    def __str__(self):
        return self.name

# Example usage
def main():
    # Student implementation example
    student_dao = StudentImpl()
    student_dao.insert({'id': 1, 'name': 'John Doe'})
    student_dao.update(1, {'id': 1, 'name': 'John Smith'})
    student = student_dao.getOne(1)
    print(f"Retrieved student: {student}")
    student_dao.delete(1)
    student = student_dao.getOne(1)
    print(f"Retrieved student after deletion: {student}")

    inventory = Inventory()
    item1 = Item("Laptop")
    item2 = Item("Phone")
    inventory.add_item(item1)
    # inventory.add_item(item2)
    inventory.remove_item("Laptop")
    inventory.remove_item("Tablet")  # This will print "Item not found: Tablet"

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Abstract Base Classes**: Learn how to define abstract base classes to enforce method definitions in subclasses.
- **DAO Pattern**: Understand how to implement the Data Access Object (DAO) pattern for managing data.
- **Inventory Management**: See an example of an inventory management system using abstract base classes and concrete implementations.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `30_abstract_classes.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `30_abstract_classes.py`.
5. Run the script with: `python 30_abstract_classes.py`.

## Usage Example 📋
Execute the script to see how abstract base classes and their concrete implementations work in Python. The script will demonstrate adding, updating, deleting, and retrieving students, as well as managing an inventory of items.

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
