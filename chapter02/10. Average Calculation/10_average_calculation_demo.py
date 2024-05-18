def get_average(num1: float, num2: float, num3: float) -> str:
    """
    Calculate the average of three numbers and format it to two decimal places.

    Args:
    num1 (float): The first number.
    num2 (float): The second number.
    num3 (float): The third number.

    Returns:
    str: The average of the three numbers formatted to two decimal places.
    """
    return "{:.2f}".format((num1 + num2 + num3) / 3)

def main() -> None:
    """
    Main function to execute the program.
    """
    first_number = 10
    second_number = 20
    third_number = 15

    # Calculate the average of the provided numbers
    average = get_average(first_number, second_number, third_number)
    print("The average is:", average)

if __name__ == "__main__":
    main()
