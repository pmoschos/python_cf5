def print_cities(*cities):
    """
    Print a list of cities separated by commas.

    Parameters:
    *cities (str): A variable number of city names to be printed.
    """
    if not cities:
        print("No cities provided.")
    else:
        print("Cities:", ", ".join(cities))

def main():
    # Demonstrate various calls to print_cities function
    print_cities("Athens", "Paris", "London")
    print_cities("London")
    print_cities("New York", "Tokyo", "Berlin", "Sydney")
    print_cities()

    # Print cities separated by commas using print_cities function
    print("--------------------------------")
    print_cities("Athens", "Paris", "London")

if __name__ == "__main__":
    main()
