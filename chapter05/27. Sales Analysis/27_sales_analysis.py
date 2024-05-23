from functools import reduce

def main():
    """
    Main function to demonstrate creating a sales dictionary, filtering sales,
    calculating taxes, and computing total sales using various Python techniques.
    """
    # Define quarters and corresponding prices
    quarters = ['A', 'B', 'C', 'D']
    prices = [1000, 2000, 1800, 1500]

    # Create sales dictionary by zipping quarters and prices
    sales = dict(zip(quarters, prices))
    print("Sales dictionary:", sales)

    print("-------------------")
    # Iterate through the sales dictionary and print each key-value pair
    for key, value in sales.items():
        print(f"{key} : {value}")

    # Filter sales dictionary to include only items with values >= 1500
    filtered_sales = dict(filter(lambda quarter_tuple: quarter_tuple[1] >= 1500, sales.items()))
    print("Filtered sales (>= 1500):", filtered_sales)

    # Calculate taxes for each quarter at a rate of 20%
    quarters_tax = {key: value * 0.2 for key, value in sales.items()}
    print("Quarters tax (20%):", quarters_tax)

    # Calculate total sales for the year using reduce
    total_year_sales = reduce(lambda x, y: x + y, sales.values())
    print("Total year sales (using reduce):", total_year_sales)

    # Alternative way to calculate total sales using sum
    total_year_sales_sum = sum(sales.values())
    print("Total year sales (using sum):", total_year_sales_sum)

if __name__ == "__main__":
    main()
