class Product:
    def __init__(self, product_id, name, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock_quantity = stock_quantity

    def __str__(self):
        return f"{self.name} - ${self.price} (Stock: {self.stock_quantity})"


class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        if product.product_id not in self.items:
            self.items[product.product_id] = {'product': product, 'quantity': 0}

        if quantity > 0 and quantity <= product.stock_quantity:
            self.items[product.product_id]['quantity'] += quantity
            product.stock_quantity -= quantity
            print(f"{quantity} {product.name}(s) added to the cart.")
        else:
            print(f"Invalid quantity or insufficient stock for {product.name}.")

    def remove_product(self, product, quantity=1):
        if product.product_id in self.items and quantity > 0:
            if quantity <= self.items[product.product_id]['quantity']:
                self.items[product.product_id]['quantity'] -= quantity
                product.stock_quantity += quantity
                print(f"{quantity} {product.name}(s) removed from the cart.")
                if self.items[product.product_id]['quantity'] == 0:
                    del self.items[product.product_id]
            else:
                print(f"Invalid quantity. There are only {self.items[product.product_id]['quantity']} {product.name}(s) in the cart.")
        else:
            print(f"{product.name} not found in the cart.")

    def view_cart(self):
        if not self.items:
            print("Shopping cart is empty.")
        else:
            total_price = 0
            print("Shopping Cart:")
            for item in self.items.values():
                product = item['product']
                quantity = item['quantity']
                item_price = quantity * product.price
                total_price += item_price
                print(f"{product.name} - Quantity: {quantity}, Price: ${item_price}")
            print(f"Total Price: ${total_price}")

    def checkout(self):
        print("Checkout:")
        self.view_cart()
        print("Thank you for shopping with us!")

        self.items = {}


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.order_history = []

    def login(self, entered_password):
        return self.password == entered_password

    def view_order_history(self):
        print(f"Order History for {self.username}:")
        for order in self.order_history:
            order.view_cart()

if __name__ == "__main__":
    laptop = Product(1, "Laptop", 1000, 10)
    phone = Product(2, "Smartphone", 500, 20)
    headphones = Product(3, "Headphones", 50, 30)

    user1 = User("john_doe", "password123")


    if user1.login("password123"):

        cart = ShoppingCart()


        cart.add_product(laptop, 2)
        cart.add_product(phone, 1)
        cart.add_product(headphones, 3)

        cart.view_cart()

        cart.remove_product(laptop, 1)

        user1.order_history.append(cart)

        user1.view_order_history()
    else:
        print("Login failed. Incorrect password.")