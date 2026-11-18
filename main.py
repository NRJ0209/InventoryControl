from InventoryControl import add_product
from InventoryControl import register_sale
from InventoryControl import restock_product
from InventoryControl import find_low_stock
from InventoryControl import calculate_total_value


def main():

    inventory = {}

    # 1. Test add_product()
    print("=== ADD PRODUCT ===")

    print(add_product(inventory, "Laptop", 900.0, 5))
    print(add_product(inventory, "Mouse", 25.0, 10))
    print(add_product(inventory, "Keyboard", 50.0, 2))

    # Duplicate product
    print(add_product(inventory, "Laptop", 800.0, 3))

    # Invalid product
    print(add_product(inventory, "", 20.0, 5))

    print(inventory)


    # 2. Test register_sale()
    print("\n=== REGISTER SALE ===")

    print(register_sale(inventory, "Laptop", 2))
    print(register_sale(inventory, "Mouse", 15))
    print(register_sale(inventory, "Phone", 1))

    print(inventory)


    # 3. Test restock_product()
    print("\n=== RESTOCK PRODUCT ===")

    print(restock_product(inventory, "Laptop", 3))
    print(restock_product(inventory, "Mouse", 0))
    print(restock_product(inventory, "Phone", 5))

    print(inventory)


    # 4. Test find_low_stock()
    print("\n=== FIND LOW STOCK ===")

    print(find_low_stock(inventory, 5))
    print(find_low_stock(inventory, 10))
    print(find_low_stock(inventory, 0))


    # 5. Test calculate_total_value()
    print("\n=== CALCULATE TOTAL VALUE ===")

    print(calculate_total_value(inventory))


    # 6. Test empty inventory
    print("\n=== EMPTY INVENTORY ===")

    empty_inventory = {}

    print(calculate_total_value(empty_inventory))
    print(find_low_stock(empty_inventory, 5))


main()

