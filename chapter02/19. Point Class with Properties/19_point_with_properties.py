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
