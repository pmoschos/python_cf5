# Sales Data Analysis in Python

This script demonstrates various techniques to create and manipulate a sales dictionary in Python. It includes filtering sales data, calculating taxes, and computing total sales using different methods.

## Script Overview 📘

The script defines a sales dictionary using quarters and their corresponding prices. It filters the sales data, calculates taxes for each quarter, and computes the total sales for the year using `reduce` and `sum`.

### :computer: Script Code

```python
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
```

## Key Features 🌟
- **Dictionary Creation**: Learn how to create a dictionary by zipping two lists.
- **Filtering**: Understand how to filter dictionary items based on their values.
- **Tax Calculation**: See how to calculate taxes for each item in the dictionary.
- **Total Sales Calculation**: Learn two methods to compute the total sales for the year using `reduce` and `sum`.

## Technical Requirements 🔧
- **Python Version**: Python 3.x recommended
- **External Libraries**: None, only the built-in Python functionalities

## Installation and Setup 🚀
No installation is required, as the script can be run directly from any Python-enabled environment:

1. Ensure Python 3.x is installed on your machine.
2. Save the script as `27_sales_analysis.py`.
3. Open a terminal or command prompt.
4. Navigate to the directory containing `27_sales_analysis.py`.
5. Run the script with: `python 27_sales_analysis.py`.

## Usage Example 📋
Execute the script to see how various Python techniques are used to analyze sales data. The script will output the sales dictionary, filtered sales, calculated taxes, and total sales for the year.

📢 Stay Updated
Be sure to ⭐ this repository to keep up with updates and new learning materials!

## 📄 License
🔐 This project is protected under the MIT License.

## Contact 📧
Panagiotis Moschos - pan.moschos86@gmail.com

🔗 Note: This is a Python script and requires a Python interpreter to run.

<h1 align="center">Happy Coding 👨‍💻</h1>
<p align="center">
  Made with ❤️ by Panagiotis Moschos (https://github.com/pmoschos)
</p>
