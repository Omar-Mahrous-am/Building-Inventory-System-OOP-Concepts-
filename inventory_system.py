# ShopSmart Inventory Management System

class Product:

    # Class-level variables
    inventory = []
    id_counter = 1

    # Constructor
    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        product_id = cls.id_counter
        cls.id_counter += 1
        new_product = cls(product_id, name, category, quantity, price, supplier)
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"
        return "Product not found"


class Order:

    # Constructor
    def __init__(self, order_id, products, customer_info=None):
        self.order_id = order_id
        self.products = products
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info):
        self.products.append((product_id, quantity))
        self.customer_info = customer_info
        return f"Order placed successfully. Order ID: {self.order_id}"


# Example usage
if __name__ == "__main__":
    p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")
    print(p1)

    update_p1 = Product.update_product(1, quantity=45, price=950)
    print(update_p1)

    delete_p1 = Product.delete_product(1)
    print(delete_p1)

    order = Order(order_id=1, products=[])
    order_placement = order.place_order(1, 2, customer_info="John Doe")
    print(order_placement)
