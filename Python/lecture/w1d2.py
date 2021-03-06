dog1 = {
    "name": "Bubba",
    "age": 1,
    "hair_color": "black"
}

class Dog:
    all_dogs = []
    def __init__(self, name, age, hair_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        Dog.all_dogs.append(self)

    def bark(self):
        print(f"Woof, my name is {self.name} and I am {self.age} years old!")

    @classmethod
    def print_dogs(cls):
        if not cls.all_dogs:
            print("No dogs")
        for dog in cls.all_dogs:
            print(f"{dog.name} is {dog.age}")

class User:
    def __init__(self, fname, lname, dog_name = "bubba", age = 1, hair_color = "black"):
        self.first_name = fname
        self.last_name = lname
        self.dog = Dog(dog_name, age, hair_color)

    def pet_bark(self):
        self.dog.bark()

james = User("James", "Luty", "Bella", 2, "Black")
pable = User("Pablo", "Padilla")

print(f"{james.first_name} {james.last_name}")

james.dog.bark()
james.pet_bark()



# bubba = Dog("Bubba", 1, "black")
# cher = Dog("Cher", 1, "white w/ a black spot")

# Dog.print_dogs()

# print(Dog.all_dogs[1].name)

# print(bubba.name)
# print(cher.name)

bubba.bark()
cher.bark()