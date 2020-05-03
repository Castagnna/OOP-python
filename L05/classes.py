class Car:
    def __init__(self):
        self.products =[]

    def insert_product(self, product):
        self.products.append(product)

    def product_list(self):
        for p in self.products:
            print(p.name, p.value)

    def total_sum(self):
        total = 0
        for p in self.products:
            total += p.value
        return total


class Product:
    def __init__(self, name, value):
        self.name = name
        self.value = value