class Dog:

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        self.age = 0

    def bark(self):
        bark = f"{self.name} says woof!"
        return bark

    def rename(self, new_name):
        self.name = new_name
        return new_name

    def birthday(self):
        self.age += 1
        return self.age

Dog1 = Dog("kiba", "doberman")
# Dog1.name = "kiba"
# Dog1.breed = "Doberman"

print(Dog1.bark())

Dog2 = Dog("sally", "pitbull")
# Dog2.name = "sally"
# Dog2.breed = "pitbull"
print(Dog2.bark())
Dog1.rename("orange")

print(Dog1.bark())
print(Dog2.bark())
print(Dog1.age)
print(Dog1.birthday())
print(Dog2.age)