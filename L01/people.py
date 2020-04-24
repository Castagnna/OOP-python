from datetime import datetime

class People:
    current_year = int(datetime.strftime(datetime.now(), '%Y'))

    def __init__(self, name, age, speaking=False, eating=False):
        self.name = name
        self.age = age
        self.speaking = speaking
        self.eating = eating

    def speak(self, word):
        if self.eating:
            print(f"{self.name} can't speak while eating")
            return
        if self.speaking:
            print(f'{self.name} is already speaking')
            return

        print(f'{self.name} is talking: {word}')
        self.speaking = True

    def stop_speak(self):
        if not self.speaking:
            print(f'{self.name} is already not speaking')
            return

        print(f'{self.name} stopped speak')
        self.speaking = False

    def eat(self, food):
        if self.eating:
            print(f'{self.name} is already eating.')
            return
        if self.speaking:
            print(f'{self.name} can not eating while talk.')
            return

        print(f'{self.name} is eating a(n) {food}.')
        self.eating = True

    def stop_eat(self):
        if not self.eating:
            print(f'{self.name} is not eating')
            return

        print(f'{self.name} stop eating')
        self.eating = False

    def bith_year(self):
        return self.current_year - self.age
