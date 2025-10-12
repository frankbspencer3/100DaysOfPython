class Car:
    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.miles = 0

    def drive(self, drive):
        self.miles += drive

    def info(self):
        return f"{self.make} {self.model} has {self.miles} miles."


Camaro = Car("Chevrolet", "Camaro")
Mustang = Car("Ford", "Mustang")

Camaro.drive(50)
print(Camaro.miles)

Mustang.drive(25)
Camaro.drive(24)

print(Mustang.miles)
print(Camaro.miles)
print(Camaro.wheels)

Car.wheels = 6

print(Camaro.wheels)
print(Mustang.wheels)

print(Camaro.info())