import datetime as dt

class Transactions:
    
    def __init__(self):
        self.basket = {}
        self.total_amount = 0
        self.transaction_id = 1

    def add_to_basket(self, product_id, quantity):
        ### Add product to basket
        if product_id in self.products.keys():
            product = self.products[product_id]
            if product.quantity >= quantity:
                self.basket[product_id] = {'DOLLAR_VALUE': product.price * quantity, 'QUANTITY': quantity}
                # self.total_amount += product.price * quantity
                self.update_quantity(product_id, product.quantity - quantity)
            else:
                raise ValueError("Insufficient stock.")
        else:
            raise ValueError("Product ID not found.")

    def remove_from_basket(self, product_id, quantity):
        ### Remove product from basket
        if product_id in self.basket.keys():
            product = self.products[product_id]
            if self.basket[product_id]['QUANTITY'] >= quantity:
                new_quantity = self.basket[product_id]['QUANTITY'] - quantity
                self.basket[product_id] = {'DOLLAR_VALUE': product.price * new_quantity,'QUANTITY': new_quantity}
                # self.total_amount += product.price * quantity
                self.update_quantity(product_id, product.quantity - quantity)
            else:
                raise ValueError("Cannot remove that many items.")
        else:
            raise ValueError("Product ID not found.")   

    def generate_sale_and_receipt(self):

        sale_value = 0

        print(f"Transaction ID: {self.transaction_id}")
        print(f"Time of Transaction: {dt.datetime.now().strftime('%Y-%m-%d %H:%M')}")
        print("Items sold:")
        for product_id, product_details in self.basket.items():
            
            sale_value += product_details['DOLLAR_VALUE']
            
            print(f"    {self.products[product_id].name}: {product_details['QUANTITY']} - ${product_details['DOLLAR_VALUE']:.2f}")
        print("="*25)
        print(f"Total amount: ${sale_value:.2f}")

        self.basket = {}
