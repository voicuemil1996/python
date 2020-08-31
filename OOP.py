#Ex.1
class Car:

    def __init__(self, color, mileage):

        self.color = color
        self.mileage = mileage

    def description(self):

        print(f'The {self.color} car has {self.mileage} miles')

Car('blue', 20000).description()
Car('red', 30000).description()


#Ex.2
class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"


class GoldenRetriever(Dog):

    def speak(self, sound = "Bark"):

        return super().speak(sound)