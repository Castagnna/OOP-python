# Getter and Setters
from product import Product


p1 = Product('t-shirt', 100)
p1.discount(20)
print(p1.name, p1.price)

p2 = Product('cup', 'RS15')
p2.discount(10)
print(p2.name, p2.price)