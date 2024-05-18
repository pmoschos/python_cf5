# Python Class for Point Operations Demonstration

Welcome to the Python Class for Point Operations Demonstration! This script showcases the use of classes in Python to manage and manipulate data related to points in 2D space. It provides a robust example for anyone new to Python or those teaching programming concepts related to object-oriented programming.

## Script Overview 📘

The script introduces a `Point` class with comprehensive features including private attributes, class methods, property methods, and special methods for string representation and comparison. It demonstrates how to instantiate objects, access and modify their attributes, and utilize class-level data.

### :computer: Script Code

```python
class Point:
    # Class variable to keep track of the number of Point objects created
    __count = 0

    # Constructor to initialize a Point object with coordinates (x, y)
    def __init__(self, x = 0, y = 0):
        # Private attributes for encapsulation
        self.__x = x
        self.__y = y
        # Incrementing the count of Point objects
        Point.__count += 1
    
    # Class method to get the count of Point objects
    @classmethod
    def getCount(cls):
        return cls.__count

    # String Representation: Modified __str__ to include the class name.
    # Aimed at providing a readable string for the end user.
    def __str__(self):
        return f"({self.__x}, {self.__y})"
    
    # Detailed Representation (__repr__): Useful for debugging
    # Aimed at providing a detailed string for developers and debugging.
    def __repr__(self):
        return f"Point(x={self.__x}, y={self.__y})"
    
    # Equality comparison method for Point objects
    def __eq__(self, other):
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        return False
    
    # Getter property for the x-coordinate
    @property
    def x(self):
        return self.__x
    
    # Setter property for the x-coordinate
    @x.setter
    def x(self, x):
        self.__x = x

    # Getter property for the y-coordinate
    @property
    def y(self):
        return self.__y
    
    # Setter property for the y-coordinate
    @y.setter
    def y(self, y):
        self.__y = y


def main():
    # Creating a Point object with coordinates (10, 20)
    p = Point(10, 20)
    print(p.x, p.y)  # Accessing x and y coordinates
    p.x = 100  # Updating the x-coordinate
    p.y = 200  # Updating the y-coordinate
    print(p.x, p.y)  # Accessing updated coordinates

    # Creating more Point objects
    p2 = Point(14, 18)
    p3 = Point(100, 200)

    # Printing the count of Point objects
    print("Number of points:", Point.getCount())

    # Comparing Point objects for equality
    print("p == p2:", p == p2)
    print("p == p3:", p == p3)

    # Printing the detailed representation of Point objects
    print(repr(p))
    print(p2)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Class Definition and Object Manipulation**: Learn how to define classes, instantiate objects, and manage object state.
- **Attribute Encapsulation**: Understand the use of private attributes and properties in Python.
- **Method Types**: Explore class methods, instance methods, and static methods in a class context.
- **Special Methods**: Discover how to define and use special methods like `__str__`, `__repr__`, and `__eq__`.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: Uses the built-in `math` library for distance calculation.

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:
1. Ensure Python 3.x is installed on your machine.
2. Save the script as `19_point_with_properties.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `19_point_with_properties.py`.
5. Run the script with: `python 19_point_with_properties.py`.

## Usage Example 📋
Execute the script to see how Point objects are created, manipulated, and compared. This demonstrates the practical applications of class features in Python.

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
