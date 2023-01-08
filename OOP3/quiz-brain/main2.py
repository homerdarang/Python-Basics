class Person:
    def __init__(self,  name, age, address):
        self.name = name
        self.age = int(age)
        self.address = address


pet = Person(input("What is your name? "), input("What is your age? "), input("Where do you live? "))

lina = Person(input("What is your name? "), input("What is your age? "), input("Where do you live? "))


print(pet.name, pet.age, pet.address)
print(lina.name, lina.age, lina.address)