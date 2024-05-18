def print_cities(*cities, sep=", ", end="\n"):
    """
    Print a list of cities separated by a specified separator and ending with a specified end character.

    Parameters:
    *cities (str): A variable number of city names to be printed.
    sep (str): Separator between city names. Default is ", ".
    end (str): End character after the last city. Default is "\n".
    """
    if not cities:
        print("No cities provided.", end=end)
    else:
        print("Cities:", sep.join(cities), end=end)

def main():
    # Demonstrating various calls to print_cities function
    print_cities("Athens", "Paris", "London")
    print_cities("London")
    print_cities("New York", "Tokyo", "Berlin", "Sydney")
    print_cities()
    
    # Demonstrating custom separator and end character
    print_cities("Athens", "Paris", "London", sep=" | ", end=".")
    print("\n--------------------------")
    print("Athens", "Paris", "London", sep=" | ", end=".")

if __name__ == "__main__":
    main()

