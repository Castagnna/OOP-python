from classes import Writer, Pen, Machine

writer1 = Writer('john')
print(writer1.name)

pen1 = Pen('bic')
print(pen1.brand)

machine1 = Machine()
print(machine1)

writer1.tool = machine1
writer1.tool.write()

writer1.tool = pen1
writer1.tool.write()

del writer1
machine1.write()