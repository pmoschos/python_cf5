# Duck Typing in Python

This script demonstrates the use of polymorphism and abstract classes in Python. It defines a base class `Vehicle` with an abstract method `drive()`, and various subclasses that implement this method. It also shows how to handle classes that do not extend the base class but still provide the required method.

## Script Overview 📘

The script defines a `Vehicle` class with an abstract method `drive()`, which must be implemented by any subclass. It includes subclasses `Car` and `Bicycle` that correctly implement `drive()`, and a `Hoverboard` class that does not extend `Vehicle` but has a `drive()` method. The script also demonstrates how to handle a subclass `Boat` that does not implement the required method.

### :computer: Script Code

```python
class Vehicle:
    def drive(self):
        raise NotImplementedError("Subclasses should implement this!")

class Car(Vehicle):
    def drive(self):
        print("Driving a car")

class Bicycle(Vehicle):
    def drive(self):
        print("Riding a bicycle")

# A class that does not extend Vehicle but has a drive method
class Hoverboard:
    def drive(self):
        print("Hovering on a hoverboard")

# A class that extends Vehicle but does not implement the drive method
class Boat(Vehicle):
    def sail(self):
        print("Sailing a boat")

# Polymorphic method
def drive_vehicle(vehicle):
    try:
        vehicle.drive()
    except NotImplementedError:
        print(f"{vehicle.__class__.__name__} can't drive.")

def main():
    # Instances of each class
    my_car = Car()
    my_bicycle = Bicycle()
    my_hoverboard = Hoverboard()
    my_boat = Boat()

    # Calling the drive_vehicle function with different objects
    drive_vehicle(my_car)        # Output: Driving a car
    drive_vehicle(my_bicycle)    # Output: Riding a bicycle
    drive_vehicle(my_hoverboard) # Output: Hovering on a hoverboard

    try:
        drive_vehicle(my_boat)       # Output: Boat can't drive.
    except NotImplementedError as e:
        print(e)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Abstract Classes**: Learn how to define and use abstract base classes in Python.
- **Polymorphism**: Understand how polymorphism allows objects of different types to be treated uniformly.
- **Error Handling**: See how to handle cases where a required method is not implemented.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `31_duck_typing.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `31_duck_typing.py`.
5. Run the script with: `python 31_duck_typing.py`.

## Usage Example 📋
Execute the script to see how polymorphism and abstract classes work in Python. The script will demonstrate driving different vehicles, including handling cases where the `drive()` method is not implemented.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</
