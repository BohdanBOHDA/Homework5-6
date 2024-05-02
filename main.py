# Дз про успадкування класів

# Завдання 1

class Animal:
    eyes = 2
    ears = 2
    legs = 4
    nose = 1


class Cat(Animal):
    isMeowing = True
    isBarking = False


class Dog(Animal):
    isMeowing = False
    isBarking = True


print(Cat.isBarking, Cat.isMeowing, Cat.nose, Cat.eyes, Cat.ears, Cat.legs)
print(Dog.isBarking, Dog.isMeowing, Dog.nose, Dog.eyes, Dog.ears, Dog.legs)

# Завдання 2


class Person:
    name = "Bohdan"

    def age(self):
        print("I'm 11 years old")


class Driver(Person):
    driver_license_number = 80394


driver_1 = Driver()

print(Driver.name, Driver.driver_license_number, driver_1.age())

# Завдання 3


class Vehicle:
    speed = 40

    def move(self):
        print("I am moving!")


class Car(Vehicle):
    isSmall = True


class Plane(Vehicle):
    isFlying = True


class Tram(Vehicle):
    isElectric = True


vehicle_1 = Vehicle()
print(vehicle_1.move())
print(Car.speed, Car.isSmall)
print(Plane.speed, Plane.isFlying)
print(Tram.speed, Tram.isElectric)

# Завдання 4


class Device:

    def turn_on(self):
        print("I am turning on")

    def turn_off(self):
        print("I am turning off")


class Smartphone(Device):
    isSmall = True


class Computer(Device):
    isFast = True


class Tablet(Device):
    isNot_keyboard = True


tablet_1 = Tablet()
print(tablet_1.turn_on())
print(tablet_1.turn_off())
print(Tablet.isNot_keyboard)
print(Smartphone.isSmall)
print(Computer.isFast)

# Завдання 5


class Programminglanguage:
    name = "Julia"

    def print_hello(self):
        print("Hello!")


class Python(Programminglanguage):
    isNormal = True


class Html(Programminglanguage):
    isEasy = True


class Javascript(Programminglanguage):
    isInteresting = True


python_1 = Python()
print(python_1.print_hello())
print(Python.name, Python.isNormal)
print(Html.name, Html.isEasy)
print(Javascript.name, Javascript.isInteresting)
