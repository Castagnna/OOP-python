# Getter and Setters
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def discount(self, percent):
        self.price = self.price * (1 - percent/100)

    # Getter
    @property
    def price(self):
        return self._price

    # Setter
    @price.setter
    def price(self, value):
        if isinstance(value, str):
            value = float(value.replace('RS', ''))
        self._price = value

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, value):
        self._name = value.upper()
