import datetime as dt

class Inventory:
    def __init__(self):
# creating an empty dictionary of products
        self.products = {}


    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
        else:
            raise ValueError("Product ID already exists.")

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product ID not found.")

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.products:
            self.products[product_id].quantity = new_quantity
        else:
           raise ValueError("Product ID not found.")

    def check_stock_level(self, product_id):
        if product_id in self.products:
            return self.products[product_id].quantity
        else:
            raise ValueError("Product ID not found.")
