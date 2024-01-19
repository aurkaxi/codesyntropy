from inventory import Product, save_inventory, update_stock
from payment import process_payment


class Item:
    def __init__(self, product_id: str, quantity: int) -> None:
        self.product_id = product_id
        self.quantity = quantity


class AlreadyInCart(Exception):
    pass


def add_to_cart(product_id: str, quantity: int, cart_data: list[Item]) -> list[Item]:
    """This will add a product to the cart

    Args:
        product_id (str): Product ID
        quantity (int): Quantity
        cart_data (list[Item]): Cart data

    Returns:
        list[Item]: Updated cart data
    """
    for item in cart_data:
        if item.product_id == product_id:
            raise AlreadyInCart(f"{product_id} is already in cart. Skipped.\n")
    cart_data.append(Item(product_id, quantity))
    return cart_data


def view_cart(cart_data: list[Item], inventory_data: list[Product]) -> None:
    """This will display the cart

    Args:
        cart_data (list[Item]): _description_
        inventory_data (list[Product]): _description_
    """
    for item in cart_data:
        for product in inventory_data:
            if item.product_id == product.product_id:
                print(
                    f"Name: {product.name}\nQty: {item.quantity}\nCost: {product.price * item.quantity}\n"
                )
                break
    return


def checkout(cart_data: list[Item], inventory_data: list[Product]) -> None:
    if len(cart_data) == 0:
        print("Cart is empty.n")
        return

    total_cost = 0
    for item in cart_data:
        for product in inventory_data:
            if item.product_id == product.product_id:
                total_cost += product.price * item.quantity
                break
    print(f"Total cost: {total_cost}")
    if input("Do you want to check out? (y/*): ") == "y":
        for item in cart_data:
            update_stock(item.product_id, -item.quantity, inventory_data)
        process_payment(total_cost)
        save_inventory(inventory_data)
        print("Payment processed successfully.\n")
    else:
        print("Payment cancelled.\n")
