from typing import TypeAlias, List

# TypeAlias: Allows defining a type alias for better readability
Vector: TypeAlias = List[float]

def add_vectors(v1: Vector, v2: Vector) -> Vector:
    """
    Adds two vectors component-wise.

    Parameters:
    v1 (Vector): The first vector.
    v2 (Vector): The second vector.

    Returns:
    Vector: The component-wise sum of v1 and v2.
    """
    return [x + y for x, y in zip(v1, v2)]

def scale_vector(v: Vector, scalar: float) -> Vector:
    """
    Scales a vector by a scalar.

    Parameters:
    v (Vector): The vector to be scaled.
    scalar (float): The scalar to multiply each component by.

    Returns:
    Vector: The scaled vector.
    """
    return [x * scalar for x in v]

def main() -> None:
    """
    Main function to demonstrate the use of vector operations.
    """
    v1: Vector = [1.0, 2.0, 3.0]
    v2: Vector = [4.0, 5.0, 6.0]
    
    print("Vector addition:")
    result_add = add_vectors(v1, v2)
    print(f"{v1} + {v2} = {result_add}")
    
    scalar = 2.0
    print("\nVector scaling:")
    result_scale = scale_vector(v1, scalar)
    print(f"{v1} * {scalar} = {result_scale}")

if __name__ == "__main__":
    main()

