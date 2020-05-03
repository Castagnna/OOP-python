# Association - use another object
# Aggregation - have
# >>> Class composition - owner
# Inheritance - is another object


from classes import Client

c1 = Client('john', 32)
c1.insert_addrees('fpolis', 'SC')
c1.list_address()
del c1
print()

c2 = Client('Paul', 17)
c2.insert_addrees('poa', 'RS')
c2.insert_addrees('rio', 'RJ')
c2.list_address()

c3 = Client('Maria', 15)
c3.insert_addrees('curitiba', 'PR')
c3.list_address()

print('#'*20)