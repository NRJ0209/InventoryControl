from InventoryControl import add_product
from InventoryControl import register_sale
if __name__ == "__main__":
    inventory = {}

    print(add_product(inventory, "apple", 0.5, 10))
    print(add_product(inventory, "apple", 0.5, 10))
    print(add_product(inventory, "banana", -0.3, 5))
    print(add_product(inventory, "pear", 0.7, 0))
    print(add_product(inventory, "", 1.0, 1))
    print(register_sale(inventory, "apple", 5))

    print(inventory)
