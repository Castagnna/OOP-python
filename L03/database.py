'''
public, private, protected
_ protected
__ private
'''

class DataBase:
    def __init__(self):
        self.__data = {}

    @property
    def data(self):
        return self.__data

    def insert_client(self, id, name):
        if 'clients' not in self.__data:
            self.__data['clients'] = {id: name}
        else:
            self.__data['clients'].update({id: name})

    def list_clients(self):
        for id, name in self.__data['clients'].items():
            print(id, name)

    def delete_client(self, id):
        del self.__data['clients'][id]
