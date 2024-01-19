"""This is a module to manage inventory"""


class Product:
    def __init__(self, product_id: str, name: str, price: float, quantity: int) -> None:
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"ID: {self.product_id}\nName: {self.name}\nPrice: {self.price}, In Stock: {self.quantity}"


def load_inventory() -> list[Product]:
    """This will load the inventory from a file

    ach product will have exactly 4 lines of information. First one is the product id, second is name, third one is the price and fourth one is the quantity. Two products will be separated by a blank line.

    We will skip the products with quantity 0.

    Returns:
        list[Product]: List of products
    """

    file = open("inventory.txt", "r")
    lines = file.readlines()
    file.close()

    products: list[Product] = []

    for i in range(0, len(lines), 5):
        id = lines[i].strip()
        name = lines[i + 1].strip()
        price = float(lines[i + 2].strip())
        quantity = int(lines[i + 3].strip())

        if quantity == 0:
            continue

        products.append(Product(id, name, price, quantity))

    return products


def save_inventory(inventory_data: list[Product]) -> None:
    """This will save the inventory data to a file

    We can take two approaches here. Either we can overwrite the whole file or check if the product already exists and update the quantity.
    Checking each product will consume more time and memory. Overwriting the file is much more concise in my opinion.

    Args:
        inventory_data (list[Product]): Inventory data

    """
    file = open("inventory.txt", "w")

    for product in inventory_data:
        file.write(
            f"{product.product_id}\n{product.name}\n{product.price}\n{product.quantity}\n\n"
        )
    file.close()

    return


def add_product(
    product_id: str,
    name: str,
    price: float,
    quantity: int,
    inventory_data: list[Product],
) -> list[Product]:
    """This will add a new product to the inventory

    Args:
        product_id (str): Product ID
        name (str): Product name
        price (float): Product price
        quantity (int): Product quantity in stock
        inventory_data (list[Product]): Inventory data

    Returns:
        list[Product]: Updated list[Product]
    """
    inventory_data.append(Product(product_id, name, price, quantity))

    save_inventory(inventory_data)
    return inventory_data


def update_stock(
    product_id: str, quantity_change: int, inventory_data: list[Product]
) -> list[Product]:
    """This will update the stock of a product

    Args:
        product_id (str): Product ID
        quantity_change (int): Quantity change
        inventory_data (list[Product]): Inventory data

    Returns:
        list[Product]: Updated Inventory data
    """
    for product in inventory_data:
        if product.product_id == product_id:
            product.quantity += quantity_change
            break
    return inventory_data
