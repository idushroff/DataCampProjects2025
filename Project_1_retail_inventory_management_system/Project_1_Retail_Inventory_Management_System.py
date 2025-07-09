""" Building a Retail Inventory Management System. """


"""
In this project, you will develop a comprehensive inventory 
management system for a retail business by applying 
your knowledge in object-oriented programming (OOP) in Python. 
Imagine you are working for an e-commerce company called SHOPSMART,
a rapidly growing online retailer that sells a wide range of products, 
including electronics, clothing, and home goods. As the company expands, 
efficiently managing inventory becomes crucial to ensure smooth operations 
and customer satisfaction. 

Object-oriented programming (OOP) is a programming paradigm that organizes software design
around data or objects rather than functions and logic. OOP allows for modular, reusable, and
maintainable code, which is particularly beneficial for complex systems like inventory
management systems. 
"""


""" 
Create Product and Order classes based on the
implementation requirements outlined in the Workbook.

These classes will handle the successful management of a
retail inventory system, including the creation, updating,
and deletion of products, and the placement of orders.
"""

"""
You will define two classes `Product` and `Order`, using the implementation requirements detailed below:

# `Product`

- Constructor parameter(s): `self`, `product_id`, `name`, `category`, `quantity`, `price`, and `supplier`.
- Class-level variable(s): `inventory`.

## `Product` class method(s)

### `add_product()`
- Parameter(s): `cls`, `name`, `category`, `quantity`, `price`, and `supplier`.
- Behavior: 
    - Define the `product_id` assuming it's auto-generated incrementally, without any duplicate `product_id` values.
    - Define a `new_product` variable that will call the constructor of the Product class.
    - Return the message `"Product added successfully"` to know that the product was added successfully.

### `update_product()`
- Parameter(s): `cls`, `product_id`, `quantity`, `price`, and `supplier`.
    - `quantity`, `price`, and `supplier` should have default values of `None`. 
- Behavior: 
    - Check if the `product_id` already exists in the `inventory`.
    - If `product_id` exists, check for the given parameters in the method if they have a value and update accordingly the product.
    - Return either one of these messages: `"Product information updated successfully"` or `"Product not found"`.

### `delete_product()`
- Parameter(s): `cls`, `product_id`.
- Behavior: 
    - Check in the inventory list if the given `product_id` was passed as a parameter.
    - If `product_id` exists then remove the product from the list.
    - Return either one of these messages: `"Product deleted successfully"` or `"Product not found"`.
"""


class Product:
    inventory = []  # Class-level variable to store all products
    product_counter = 1  # Start the product_id from 1 and increment with each new product

    def __init__(self, product_id, name, category, quantity, price, supplier):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.quantity = quantity
        self.price = price
        self.supplier = supplier

    @classmethod
    def add_product(cls, name, category, quantity, price, supplier):
        # Auto-generate product_id based on current counter
        product_id = cls.product_counter
        cls.product_counter += 1  # Increment the counter for the next product

        # Create the new product instance
        new_product = Product(product_id, name, category, quantity, price, supplier)

        # Add the product to the inventory
        cls.inventory.append(new_product)
        return "Product added successfully"

    @classmethod
    def update_product(cls, product_id, quantity=None, price=None, supplier=None):
        # Check if the product exists in inventory
        for product in cls.inventory:
            if product.product_id == product_id:
                if quantity is not None:
                    product.quantity = quantity
                if price is not None:
                    product.price = price
                if supplier is not None:
                    product.supplier = supplier
                return "Product information updated successfully"

        # If product not found
        return "Product not found"

    @classmethod
    def delete_product(cls, product_id):
        # Find and remove product by id
        for product in cls.inventory:
            if product.product_id == product_id:
                cls.inventory.remove(product)
                return "Product deleted successfully"

        # If product not found
        return "Product not found"


# Test the functionality
# Add products
print(Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A"))
print(Product.add_product("Smartphone", "Electronics", 100, 500, "Supplier B"))

# Update a product
print(Product.update_product(1, quantity=45, price=950))

# Delete a product
print(Product.delete_product(2))

"""
# `Order`

- Constructor parameter(s): `self`, `order_id`, `products`, and `customer_info`.
    - `customer_info` should have a default value of `None`. 

## `Order` method(s)

### `place_order()`
- Parameter(s): `self`, `product_id`, `quantity`, and `customer_info`.
    - `customer_info` should have a default value of `None`.
- Behavior: 
    - Append to the `products` list a tuple containing `product_id` and `quantity`.
    - Assume that each order can only take **one** product. 
    - Return the message: `"Order placed successfully. Order ID: {self.order_id}"`.
"""


class Order:

    def __init__(self, order_id, products, customer_info=None):
        self.order_id = order_id
        self.products = products  # List of product tuples (product_id, quantity)
        self.customer_info = customer_info

    def place_order(self, product_id, quantity, customer_info=None):
        # Check if the product is available in the inventory (assuming there's a Product class)
        product = None
        for prod in Product.inventory:
            if prod.product_id == product_id:
                product = prod
                break

        if product is None:
            return f"Product with ID {product_id} not found in inventory."

        # Check if there's enough quantity available
        if product.quantity < quantity:
            return f"Not enough stock for product ID {product_id}. Available quantity: {product.quantity}"

        # Reduce the quantity of the product in the inventory
        product.quantity -= quantity

        # Append the product to the order's product list
        self.products.append((product_id, quantity))

        # If customer_info is provided, update the order's customer_info
        if customer_info is not None:
            self.customer_info = customer_info

        # Return success message with order ID
        return f"Order placed successfully. Order ID: {self.order_id}"


# Example usage

# Assuming Product class is already populated in the inventory
p1 = Product(1, "Laptop", "Electronics", 50, 1000, "Supplier A")
Product.inventory.append(p1)

order = Order(order_id=1, products=[], customer_info=None)

# Attempt to place an order
print(order.place_order(1, 2))  # Ordering 2 laptops
print(order.place_order(1, 100))  # Trying to order more than the available stock


"""
As an example, your code must be able to create products like this:

`p1 = Product.add_product("Laptop", "Electronics", 50, 1000, "Supplier A")`

Update them like this:

`update_p1 = Product.update_product(1, quantity=45, price=950)`

Delete them like this:

`delete_p1 = Product.delete_product(1)`

And, create and place orders like this:

`order = Order(order_id=1, products=[])`

`order_placement = order.place_order(1, 2, customer_info="John Doe")`
"""

"""
############### RESOURCES ###############
Class anatomy: the __init__ constructor
https://campus.datacamp.com/courses/introduction-to-object-oriented-programming-in-python/oop-fundamentals-1?ex=9

Class vs. instance attributes
https://campus.datacamp.com/courses/introduction-to-object-oriented-programming-in-python/inheritance-and-polymorphism-2?ex=1

Class methods
https://campus.datacamp.com/courses/introduction-to-object-oriented-programming-in-python/inheritance-and-polymorphism-2?ex=5

"""



