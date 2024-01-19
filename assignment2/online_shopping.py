from inventory import Product, add_product, load_inventory
from shopping_cart import AlreadyInCart, Item, add_to_cart, checkout, view_cart

cart_data: list[Item] = []
inventory_data: list[Product] = load_inventory()


class InvalidProductID(Exception):
    pass


def get_product(product_id: str, inventory_data: list[Product]) -> Product:
    for product in inventory_data:
        if product.product_id == product_id:
            return product
    raise InvalidProductID(f"Invalid product ID: {product_id}")


while True:
    print(
        "\n1. View Product Inventory\n2. View Cart\n3. Add Product to inventory\n4. Exit"
    )
    choice = input("Enter your choice: ")
    print()

    if choice == "1":
        if inventory_data == []:
            print("Inventory is empty. Notify Store Manager.\n")
            continue
        for product in inventory_data:
            print(product, "\n")

        to_cart = input(
            "Enter product ID(s), separated by space, to add to cart: "
        ).split()

        if to_cart == []:
            continue

        for product_id in to_cart:
            try:
                product = get_product(product_id, inventory_data)
            except InvalidProductID as e:
                print(e)
                continue

            while True:
                try:
                    quantity = int(input(f"Enter quantity for {product.name}: "))
                except ValueError:
                    print("Quantity must be an integer.")
                    continue

                if quantity > product.quantity:
                    print(f"We only have {product.quantity} {product.name} in stock.")
                    continue

                break

            try:
                cart_data = add_to_cart(product_id, quantity, cart_data)
            except AlreadyInCart as e:
                print(e)
                continue

            print(f"{product.name} added to cart successfully.\n")
    elif choice == "2":
        view_cart(cart_data, inventory_data)
        checkout(cart_data, inventory_data)
        cart_data = []
    elif choice == "3":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")

        while True:
            try:
                price = float(input("Enter product price: "))
            except ValueError:
                print("Price must be a number.")
                continue
            if price <= 0:
                print("Price must be greater than 0.")
                continue
            break
        while True:
            quantity = input("Enter product quantity: ")
            if not quantity.isnumeric():
                print("Quantity must be an integer.")
                continue

            quantity = int(quantity)
            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue

            break

        inventory_data = add_product(product_id, name, price, quantity, inventory_data)
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.\n")

print("Thank you for using our application.")
