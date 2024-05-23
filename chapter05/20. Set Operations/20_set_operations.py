def main():
    """
    Main function to demonstrate set operations in Python.
    """
    # Define two sets
    bag1 = {"A1", "A2", "A3", "A4", "BA1"}
    bag2 = {"A1", "A2", "B3", "B4", "BB2"}

    # Find common elements (intersection) of bag1 and bag2
    common_elements = bag1 & bag2
    # Alternatively, using the intersection method
    common_elements = bag1.intersection(bag2)
    print("Common elements of bag1 and bag2:", common_elements)

    # Find all elements (union) of bag1 and bag2
    all_the_elements = bag1 | bag2
    # Alternatively, using the union method
    all_the_elements = bag1.union(bag2)
    print("All elements of bag1 and bag2:", all_the_elements)

    # Find elements in bag1 but not in bag2 (difference)
    diff1 = bag1 - bag2
    # Alternatively, using the difference method
    diff1 = bag1.difference(bag2)
    print("Elements in bag1 but not in bag2:", diff1)

    # Find elements that are in either bag1 or bag2 but not both (symmetric difference)
    diff2 = bag1 ^ bag2
    # Alternatively, using the symmetric_difference method
    diff2 = bag1.symmetric_difference(bag2)
    print("Elements in either bag1 or bag2 but not both:", diff2)

if __name__ == "__main__":
    main()
