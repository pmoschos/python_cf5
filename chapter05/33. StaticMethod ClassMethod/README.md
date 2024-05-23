# Class Methods and Static Methods in Python

This script demonstrates the use of class methods and static methods in Python. It defines an `Employee` class with class-level and instance-level attributes, and methods that illustrate the proper and improper use of class methods and static methods.

## Script Overview 📘

The script defines an `Employee` class with class methods and static methods. It includes examples of accessing and modifying class-level data, as well as utility functions that do not depend on instance or class data. The `main()` function demonstrates creating instances of the `Employee` class, calculating bonuses, and handling incorrect method usage.

### :computer: Script Code

```python
class Employee:
    _total_employees = 0

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        Employee._total_employees += 1

    @classmethod
    def total_employees(cls):
        """
        Class method to get the total number of employees created.
        """
        return cls._total_employees

    @staticmethod
    def calculate_bonus(salary, bonus_percentage):
        """
        Static method to calculate the annual bonus based on salary and bonus percentage.
        """
        return salary * (bonus_percentage / 100)

    @classmethod
    def incorrect_class_method(cls):
        """
        Incorrectly tries to access instance-level attributes.
        """
        try:
            print(cls.first_name)  # This will cause an AttributeError
        except AttributeError as e:
            print(f"Error in class method: {e}")

    @staticmethod
    def incorrect_static_method():
        """
        Incorrectly tries to access class-level attributes.
        """
        try:
            print(Employee._total_employees)  # This will actually work since we access class-level attribute directly
        except AttributeError as e:
            print(f"Error in static method: {e}")

def main():
    # Creating employee instances
    emp1 = Employee("John", "Doe", 50000)
    emp2 = Employee("Jane", "Smith", 60000)

    # Getting the total number of employees created
    total_emps = Employee.total_employees()
    print(f"Total employees created: {total_emps}")  # Output: Total employees created: 2

    # Calculating annual bonus
    bonus = Employee.calculate_bonus(emp1.salary, 10)
    print(f"Annual bonus for {emp1.first_name} {emp1.last_name}: {bonus}")  # Output: Annual bonus for John Doe: 5000.0

    bonus = Employee.calculate_bonus(emp2.salary, 15)
    print(f"Annual bonus for {emp2.first_name} {emp2.last_name}: {bonus}")  # Output: Annual bonus for Jane Smith: 9000.0

    # Demonstrating incorrect usage
    print("\nDemonstrating incorrect usages:")

    # Incorrect class method usage
    Employee.incorrect_class_method()  # This will raise an AttributeError

    # Incorrect static method usage
    Employee.incorrect_static_method()  # This will not raise an error but is shown for demonstration

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Class Methods**: Learn how to define and use class methods to access and modify class-level data.
- **Static Methods**: Understand how to define and use static methods for utility functions that do not depend on instance or class data.
- **Error Handling**: See examples of incorrect method usage and how to handle errors.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `33_staticmethod_classmethod.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `33_staticmethod_classmethod.py`.
5. Run the script with: `python 33_staticmethod_classmethod.py`.

## Usage Example 📋
Execute the script to see how class methods and static methods work in Python. The script will demonstrate creating employee instances, calculating bonuses, and handling incorrect method usage.

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
