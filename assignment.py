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

    if name in item_names:
        print("Item already exists. Try again.\n")
        add_item()
        return
    
    quantity = int(input("Enter item quantity: "))
    price = int(input("Enter item price: "))

    item_names.append(name)
    item_quantities.append(quantity)
    item_prices.append(price)

    print("\nItem added successfully. Here is the updated inventory:\n")
    view_inventory()


def remove_item():
    print("Remove Item:")
    name = input("Enter item name: ")

    if name not in item_names:
        print("Item not found. Try again.\n")
        remove_item()
        return

    index = item_names.index(name)
    item_names.pop(index)
    item_quantities.pop(index)
    item_prices.pop(index)

    print("\nItem removed successfully. Here is the updated inventory:\n")
    view_inventory()


def update_item():
    print("Update Item:")
    name = input("Enter item name: ")

    if name not in item_names:
        print("Item not found. Try again.\n")
        update_item()
        return

    index = item_names.index(name)
    quantity = int(input("Enter item quantity: "))

    item_quantities[index] = quantity

    print("\nItem updated successfully. Here is the updated inventory:\n")
    view_inventory()


def add_to_cart():
    print("Add to Cart:")
    index = int(input("Enter item index: "))
    if index > len(item_names):
        print("Item not found. Try again.\n")
        add_to_cart()
        return

    quantity = int(input("Enter " + str(item_names[index - 1]) + " quantity: "))
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
    view_cart()
    print("Checkout:")
    print("Total:", calculate_total())
    confirm = input("Confirm checkout? (y/n): ")
    if confirm.lower() == "y":
        for i in range(len(cart_items)):
            index = item_names.index(cart_items[i])
            item_quantities[index] -= cart_quantities[i]
        cart_items.clear()
        cart_quantities.clear()
        print("Checkout successful. Cart is now empty.")
    else:
        print("Checkout cancelled.")
    print("========================\n")


choice = 0
while choice != 8:
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
    else:
        pass

print("Thank you for using the inventory management system.")
