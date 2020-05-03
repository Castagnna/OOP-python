class Client:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = []

    def insert_addrees(self, city, state):
        self.address.append(Address(city, state))

    def list_address(self):
        for a in self.address:
            print(a.city, a.state)

    def __del__(self):
        print(f'{self.name} erased')


class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state

    def __del__(self):
        print(f'{self.city}, {self.state} erased')