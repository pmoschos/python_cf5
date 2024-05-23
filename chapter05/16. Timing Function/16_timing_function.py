import time

def get_time(n):
    """
    Calculate the sum of the first n natural numbers and measure the time taken to perform the calculation.

    Parameters:
    n (int): The number of natural numbers to sum.

    Returns:
    int: The sum of the first n natural numbers.
    """
    start_time = time.time()  # Record the start time
    # Perform the calculation: sum of the first n natural numbers
    result = sum(range(n))  # 0 + 1 + 2 + 3 + ... + (n - 1)
    end_time = time.time()  # Record the end time
    # Print the time taken to run the function
    print(f"My function took {end_time - start_time: .5f} seconds to run")
    
    return result

def main():
    """
    Main function to demonstrate the get_time function.
    """
    # Call the get_time function with n = 1,000,000 and print the result
    print(get_time(1000000))

if __name__ == "__main__":
    main()
