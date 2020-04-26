from database import DataBase

db = DataBase()
db.insert_client(1, 'Rose')
db.insert_client(2, 'Paul')
db.insert_client(3, 'John')
db.insert_client(4, 'John')
db.insert_client(5, 'John')
#print(db.__data)

db.delete_client(1)
db.list_clients()

# db.__data = 'something else'
db.list_clients()

print(db._DataBase__data)
print(db.data)