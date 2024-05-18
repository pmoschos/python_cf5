import math

class Point:
    """
    A class representing a point in 2D space.

    Attributes:
        __x (float): The x-coordinate of the point.
        __y (float): The y-coordinate of the point.
    """

    def __init__(self, x: float = 0, y: float = 0):
        """Initialize a Point instance with x and y coordinates."""
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        """Get the x-coordinate."""
        return self.__x

    @x.setter
    def x(self, value: float):
        """Set the x-coordinate."""
        if not isinstance(value, (int, float)):
            raise TypeError("x must be a number")
        self.__x = value

    @property
    def y(self) -> float:
        """Get the y-coordinate."""
        return self.__y

    @y.setter
    def y(self, value: float):
        """Set the y-coordinate."""
        if not isinstance(value, (int, float)):
            raise TypeError("y must be a number")
        self.__y = value

    def __str__(self) -> str:
        """Return a string representation of the Point."""
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other: object) -> bool:
        """Check if two Points are equal."""
        if isinstance(other, Point):
            return self.__x == other.__x and self.__y == other.__y
        return False

    def __lt__(self, other: object) -> bool:
        """Check if this Point is less than another Point based on their coordinates."""
        if isinstance(other, Point):
            return (self.__x, self.__y) < (other.__x, other.__y)
        return NotImplemented

    def distance_to(self, other: 'Point') -> float:
        """Calculate the distance to another Point."""
        if isinstance(other, Point):
            return math.sqrt(math.pow(self.__x - other.__x, 2) + math.pow(self.__y - other.__y, 2))
        raise ValueError("The argument must be an instance of Point")

def main():
    # Create two Point objects
    p1 = Point(10, 20)
    p2 = Point(30, 40)
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    
    # Check equality
    print(f"Are points equal? {p1 == p2}")
    
    # Calculate distance between points
    print(f"Distance between points: {p1.distance_to(p2)}")
    
    # Demonstrating the use of properties
    p1.x = 15
    p1.y = 25
    print(f"Updated Point 1: {p1}")

    # Demonstrating __lt__ method
    p4 = Point(0, 0)
    print(f"Is Point 4 less than Point 1? {p4 < p1}")

if __name__ == "__main__":
    main()
