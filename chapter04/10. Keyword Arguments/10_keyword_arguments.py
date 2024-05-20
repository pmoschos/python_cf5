from typing import List, Tuple, Dict

def get_results(products: List[Tuple[str, int]], **kwargs) -> List[Tuple[str, int]]:
    """
    Filters a list of products based on given keyword arguments.
    Each keyword argument corresponds to a product attribute.

    Parameters:
    products (List[Tuple[str, int]]): A list of tuples where each tuple contains a brand and a price.
    **kwargs: Arbitrary keyword arguments, typically "brand" and "price".

    Returns:
    List[Tuple[str, int]]: A list of tuples that match the filtering criteria.
    
    Example:
    >>> products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    >>> get_results(products, brand="lenovo", price=100)
    [('lenovo', 100)]
    """
    # Improved filtering to allow matching on one or more provided criteria
    results = [
        # [<expression> for <item> in <iterable> if <condition>]
        (brand, price) for brand, price in products if kwargs.get('brand') == brand and kwargs.get('price') == price
    ]
    return results

def main():
    """
    Main function to demonstrate the use of get_results function.
    """
    products = [("lenovo", 100), ("lenovo", 40), ("imb", 100)]
    criteria = {"brand": "lenovo", "price": 100}

    # Demonstration of the function
    print(get_results(products, **criteria))

if __name__ == "__main__":
    main()
