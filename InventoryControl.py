def add_product(inventory: dict, name: str,
                price: float, quantity: int) -> bool:
    """Add a new product with a non-negative price and initial stock.

    Return True if added, or False for invalid values or a duplicate name.
    Modify the inventory only when the operation succeeds.
    """

def register_sale(inventory: dict, name: str, quantity: int) -> bool:
    """Sell a positive integer quantity of an existing product.

    Return True and reduce stock if enough units are available.
    Otherwise, return False without changing the inventory.
    """

def restock_product(inventory: dict, name: str, quantity: int) -> bool:
    """Add a positive integer quantity to an existing product's stock.

    Return True if updated, or False if the product is missing
    or the quantity is not positive.
    """

def find_low_stock(inventory: dict, minimum: int) -> list[str]:
    """Return product names with stock strictly below the minimum.

    The minimum must be a non-negative integer.
    Return an empty list if no products match.
    Raise ValueError if the minimum is negative.
    """

def calculate_total_value(inventory: dict) -> float:
    """Return the total stock value in euros, rounded to two decimals.

    Multiply each unit price by its available quantity and sum the values.
    Return 0.0 for an empty inventory.
    """