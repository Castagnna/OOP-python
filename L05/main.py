# classes aggregation

from classes import Car, Product

cart = Car()

p1 = Product('t-shirt', 50)
p2 = Product('cup', 10)
p3 = Product('book', 20)

cart.insert_product(p1)
cart.insert_product(p2)
cart.insert_product(p3)

cart.product_list()

print(cart.total_sum())