class Pet():
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} gained 5 energy and 10 health after eating")

    def play(self):
        self.health += 5
        print(f"{self.name} gained 5 health after playing")

    def noise(self):
        print("Woof woof woof")

class Bird(Pet):
    def __init__(self, name, type, tricks, health, energy):
        super().__init__(name, type, tricks, health, energy)

    def birdNoise(self):
        print("Chirp Chirp Chirp")