#Assignment 3

#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
#Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.
#Sample Order Data:

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    # More orders...
]

def process_orders(orders):
    for order in orders:
        customer, product, quantity = order
        order_info = f"{customer} ordered {quantity} {product}{'s' if quantity > 1 else ''}"
        print(order_info)

process_orders(orders)