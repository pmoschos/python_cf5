# Point Class in Python

This script demonstrates the implementation of a `Point` class in Python. The class includes methods for adding points, checking equality, and accessing/modifying private attributes via properties.

## Script Overview 📘

The script defines a `Point` class with private attributes for the x and y coordinates. It includes methods for addition, equality checking, and string representation. The class also uses properties to provide controlled access to the private attributes. The `main()` function demonstrates the usage of the `Point` class and additional helper functions.

### :computer: Script Code

```python
class Point:
    def __init__(self, x, y):
        """
        Initialize a point with coordinates (x, y).
        
        Parameters:
        x (int or float): The x-coordinate of the point.
        y (int or float): The y-coordinate of the point.
        """
        self.__x = x
        self.__y = y
    
    def __str__(self):
        """
        Return a string representation of the point.
        
        Returns:
        str: The string representation of the point.
        """
        return f"({self.__x}, {self.__y})"
    
    def __add__(self, other):
        """
        Add a point or a number to the current point.
        
        Parameters:
        other (Point, int, or float): The other point or number to add.
        
        Returns:
        Point: The result of the addition.
        
        Raises:
        TypeError: If the other operand is not a Point or a number.
        """
        if isinstance(other, Point):
            return Point(self.__x + other.__x, self.__y + other.__y)
        elif isinstance(other, (int, float)):
            return Point(self.__x + other, self.__y + other)
        else:
            raise TypeError(f"Unsupported operand types for +: 'Point' and {type(other).__name__}")
    
    def __radd__(self, other):
        """
        Add the current point to a number (for right-side addition).
        
        Parameters:
        other (int or float): The number to add.
        
        Returns:
        Point: The result of the addition.
        """
        return self.__add__(other)
    
    def __eq__(self, other):
        """
        Check if two points are equal.
        
        Parameters:
        other (Point): The other point to compare.
        
        Returns:
        bool: True if the points are equal, False otherwise.
        """
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        else:
            return False
    
    @property
    def x(self):
        """
        Get the x-coordinate of the point.
        
        Returns:
        int or float: The x-coordinate of the point.
        """
        return self.__x
    
    @x.setter
    def x(self, value):
        """
        Set the x-coordinate of the point.
        
        Parameters:
        value (int or float): The new x-coordinate of the point.
        """
        self.__x = value
    
    @property
    def y(self):
        """
        Get the y-coordinate of the point.
        
        Returns:
        int or float: The y-coordinate of the point.
        """
        return self.__y
    
    @y.setter
    def y(self, value):
        """
        Set the y-coordinate of the point.
        
        Parameters:
        value (int or float): The new y-coordinate of the point.
        """
        self.__y = value

def do_add(a, b):
    """
    Add two objects using the + operator.
    
    Parameters:
    a, b: The objects to add.
    
    Returns:
    The result of the addition.
    """
    return a + b

def main():
    """
    Main function to demonstrate the usage of the Point class and do_add function.
    """
    p1 = Point(1, 2)
    p2 = Point(3, 4)

    print("p1 + p2 =", p1 + p2)  # (4, 6)
    print("p1 + 10 =", p1 + 10)  # (11, 12)
    print("sum([p1, p2]) =", sum([p1, p2]))  # (4, 6)
    print("p1 == Point(1, 2) =", p1 == Point(1, 2))  # True
    print("p1 == 'Hello' =", p1 == "Hello")  # False

    print("do_add(Point(10, 20), Point(5, 5)) =", do_add(Point(10, 20), Point(5, 5)))  # (15, 25)

    # Accessing private fields via properties
    print("p1 x-coordinate:", p1.x)  # 1
    print("p1 y-coordinate:", p1.y)  # 2

    # Modifying private fields via setters
    p1.x = 100
    p1.y = 200
    print("Modified p1:", p1)  # (100, 200)

if __name__ == "__main__":
    main()
```

## Key Features 🌟
- **Encapsulation**: Learn how to use private attributes to encapsulate data.
- **Operator Overloading**: Understand how to overload operators for custom behavior in class instances.
- **Property Management**: See how to manage access to private attributes using properties.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `29_point_class.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `29_point_class.py`.
5. Run the script with: `python 29_point_class.py`.

## Usage Example 📋
Execute the script to see how the Point class works. The script will demonstrate creating points, adding points and numbers, checking equality, and accessing/modifying private attributes via properties.

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
