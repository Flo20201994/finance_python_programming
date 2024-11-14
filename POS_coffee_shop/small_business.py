import datetime as dt

class SmallBusiness(Inventory, Transactions,):
    def __init__(self, ):        
        Inventory.__init__(self)
        Transactions.__init__(self)
        
magic_dirt_coffee_house = SmallBusiness()

magic_dirt_coffee_house.add_product(Product(1, 'Latte', 5, 50))
magic_dirt_coffee_house.add_product(Product(2, 'Americano', 4.50, 50))
magic_dirt_coffee_house.add_product(Product(3, 'Espresso', 3, 50))
magic_dirt_coffee_house.add_product(Product(4, 'Drip Coffee', 3, 50 ))


magic_dirt_coffee_house.products


magic_dirt_coffee_house.check_stock_level(1)

magic_dirt_coffee_house.remove_product(2)

magic_dirt_coffee_house.check_stock_level(2)



magic_dirt_coffee_house.add_to_basket(1,4)
magic_dirt_coffee_house.add_to_basket(2,4)

magic_dirt_coffee_house.generate_sale_and_receipt()

magic_dirt_coffee_house.basket
