
class Car:

    def __init__(self, color, mileage):

        self.color = color
        self.mileage = mileage

    def description(self):

        print(f'The {self.color} car has {self.mileage} miles')

Car('blue', 20000).description()
Car('red', 30000).description()