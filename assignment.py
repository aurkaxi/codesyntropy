item_names = ["Laptop", "Headphones", "Keyboard", "Mouse"]
item_quantities = [10, 20, 15, 30]
item_prices = [1000, 500, 450, 300]

cart_items = []
cart_quantities = []


def view_inventory():
    print("Inventory:")
    for i in range(len(item_names)):
        print(str(i + 1) + ".", "Name:", item_names[i])
        print("Qty:", item_quantities[i], "; Price:", item_prices[i])
        print()
    print("========================\n")


def add_item():
    print("Add Item:")

    name = input("Enter item name: ")
    while name in item_names:
        print("Item already exists. Try again.\n")
        name = input("Enter item name: ")

    quantity = input("Enter item quantity: ")
    while not quantity.isdigit():
        print("Invalid quantity. Try again.\n")
        quantity = input("Enter item quantity: ")
    quantity = int(quantity)

    price = input("Enter item price: ")
    while not price.isdigit():
        print("Invalid price. Try again.\n")
        price = input("Enter item price: ")
    price = int(price)

    item_names.append(name)
    item_quantities.append(quantity)
    item_prices.append(price)

    print("\nItem added successfully. Here is the updated inventory:\n")
    view_inventory()


def remove_item():
    print("Remove Item:")

    name = input("Enter item name: ")
    while name not in item_names:
        print("Item not found. Try again.\n")
        name = input("Enter item name: ")

    index = item_names.index(name)
    item_names.pop(index)
    item_quantities.pop(index)
    item_prices.pop(index)

    if name in cart_items:
        index = cart_items.index(name)
        cart_items.pop(index)
        cart_quantities.pop(index)

    print("\nItem removed successfully. Here is the updated inventory:\n")
    view_inventory()


def update_item():
    print("Update Item:")

    name = input("Enter item name: ")
    while name not in item_names:
        print("Item not found. Try again.\n")
        name = input("Enter item name: ")
    index = item_names.index(name)

    quantity = input("Enter item quantity: ")
    while not quantity.isdigit():
        print("Invalid quantity. Try again.\n")
        quantity = input("Enter item quantity: ")
    quantity = int(quantity)

    item_quantities[index] = quantity

    if name in cart_items:
        index = cart_items.index(name)
        if cart_quantities[index] > quantity:
            cart_quantities[index] = quantity

    print("\nItem updated successfully. Here is the updated inventory:\n")
    view_inventory()


def add_to_cart():
    print("Add to Cart:")

    index = input("Enter item index: ")
    while not index.isdigit() or int(index) > len(item_names):
        print("Invalid index. Try again.\n")
        index = input("Enter item index: ")
    index = int(index)

    quantity = input("Enter item quantity: ")
    while (not quantity.isdigit()) or (int(quantity) > item_quantities[index - 1]):
        print("Invalid quantity. Try again.\n")
        quantity = input("Enter item quantity: ")
    quantity = int(quantity)

    cart_items.append(item_names[index - 1])
    cart_quantities.append(quantity)

    print("\nItem added to cart successfully. Here is the updated cart:")
    view_cart()
    print("========================\n")


def calculate_total():
    total = 0
    for i in range(len(cart_items)):
        index = item_names.index(cart_items[i])
        total += item_prices[index] * cart_quantities[i]
    return total


def view_cart():
    print("Cart:")
    for i in range(len(cart_items)):
        print(str(i + 1) + ".", "Name:", cart_items[i])
        print("Qty:", cart_quantities[i])
        print()

    print("Total:", calculate_total())
    print("========================\n")


def checkout():
    if len(cart_items) == 0:
        print("Cart is empty. Try again.\n")
        return

    view_cart()
    print("Checkout:")
    print("Total:", calculate_total())
    confirm = input("Confirm checkout? (y/n): ")
    while confirm.lower() not in ["y", "n"]:
        if confirm.lower() == "y":
            for i in range(len(cart_items)):
                index = item_names.index(cart_items[i])
                item_quantities[index] -= cart_quantities[i]
            cart_items.clear()
            cart_quantities.clear()
            print("Checkout successful. Cart is now empty.")
        elif confirm.lower() == "n":
            print("Checkout cancelled.")
    print("========================\n")


while True:
    print(
        "1. View Inventroy\n2. Add Item\n3. Remove Item\n4. Update Item\n5. Add to Cart \n6. View Cart\n7. Checkout\n8. Exit"
    )
    choice = int(input("Enter your choice: "))
    print("========================\n")

    if choice == 1:
        view_inventory()
    elif choice == 2:
        add_item()
    elif choice == 3:
        remove_item()
    elif choice == 4:
        update_item()
    elif choice == 5:
        add_to_cart()
    elif choice == 6:
        view_cart()
    elif choice == 7:
        checkout()
    elif choice == 8:
        break
    else:
        print("Invalid choice. Try again.\n")

print("Thank you for using the inventory management system.")
