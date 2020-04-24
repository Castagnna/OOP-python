from L01.people import People

p1 = People('John', 19)
p2 = People('Maria', 13)

print(p1.current_year)
print(p2.current_year)
print(People.current_year)
print(p1.bith_year())

p1.stop_eat()
p1.eat('apple')
p1.eat('apple')
p1.stop_eat()
p1.stop_speak()
p1.speak('this car is fast')
p1.eat('banana')
p1.stop_speak()
p1.eat('banana')
p2.speak('dolls')

