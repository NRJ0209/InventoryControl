def add_product(inventory: dict, name: str,
                price: float, quantity: int) -> bool:
    """Add a new product with a non-negative price and initial stock.

    Return True if added, or False for invalid values or a duplicate name.
    Modify the inventory only when the operation succeeds.
    """

    # Check for invalid values or duplicate names
    if name == "" or price < 0 or quantity < 0 or name in inventory:
        return False

    # Only save the product if all checks passed
    inventory[name] = {"price": price, "quantity": quantity}
    return True


def register_sale(inventory: dict, name: str, quantity: int) -> bool:
    """Sell a positive integer quantity of an existing product.

    Return True and reduce stock if enough units are available.
    Otherwise, return False without changing the inventory.
    """
    if name in inventory:
        if quantity <= inventory[name]:
            inventory[name] -= quantity
            return True
    return False

def restock_product(inventory: dict, name: str, quantity: int) -> bool:
    """Add a positive integer quantity to an existing product's stock.

    Return True if updated, or False if the product is missing
    or the quantity is not positive.
    """
    # Reject the operation if the product does not exist or the quantity is zero or negative
    if name not in inventory or quantity <= 0:
        return False

    # Add the received units to the product's current stock
    inventory[name]["quantity"] += quantity
    return True


def find_low_stock(inventory: dict, minimum: int) -> list[str]:
    """Return product names with stock strictly below the minimum.

    The minimum must be a non-negative integer.
    Return an empty list if no products match.
    Raise ValueError if the minimum is negative.
    """
    #validate the input first: a negative minimum makes no sense
    if minimum < 0:
        raise ValueError("Minimum must be non-negative")
    #will hold the names of the products that are below the minimum
    low_stock = []
    #go through every product name in inventory
    for name, data in inventory.items():
        if data["quantity"] < minimum:
            low_stock.append(name)
    #if no product matched this is an empty list
    return low_stock


def calculate_total_value(inventory: dict) -> float:
    """Return the total stock value in euros, rounded to two decimals.

    Multiply each unit price by its available quantity and sum the values.
    Return 0.0 for an empty inventory.
    """
    if inventory == {}:
        return 0.0
    total = 0.0
    for name, data in inventory.items():
        total += data["price"] * data["quantity"]
    return total
