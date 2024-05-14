def calculate_simple_interest(principal, rate):
    """
    Calculate simple interest on a given amount.

    Parameters:
    - principal (float): The principal amount.
    - rate (float): The annual interest rate (expressed as a decimal).

    Returns:
    - float: The interest calculated.
    """
    interest = principal * rate
    return interest

def main():
    # Amount of the principal loan/deposit
    amount = 215_000.0  # underscore for readability (Python 3.6+ feature)
    
    # Annual interest rate (as a decimal)
    rate = 0.25

    # Calculate interest using the function
    interest = calculate_simple_interest(amount, rate)

    # Print the total interest, formatted to two decimal places
    print(f"Total interest: ${interest:,.2f}")

if __name__ == "__main__":
    main()
