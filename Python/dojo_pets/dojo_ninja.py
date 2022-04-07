from dojo_pet import Pet
from dojo_pet import Bird

class Ninja():
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self, pet):
        print(f"{self.first_name} {self.last_name} is taking {pet.name} for a walk.")
        pet.play()

    def feed(self, pet):
        print(f"{self.first_name} {self.last_name} is feeding {pet.name} some {self.pet_food}.")
        pet.eat()

    def bathe(self, pet):
        print(f"{self.first_name} {self.last_name} is giving {pet.name} a bathe.")
        if (pet.type != "Bird"):
            pet.noise()
        else:
            pet.birdNoise()



james = Ninja("James", "Luty", "Beggin Strips", "Dog Food", "Dog")
bella = Pet("Bella", "Black Lab", "Sit", 100, 200)
turbo = Bird("Turbo", "Bird", "Fly", 50, 100)

# james.walk()
# james.bathe()
james.bathe(turbo)