import random

class Character:
    all_characters = []
    def __init__(self, name, health = 100, strength = 10, toughness = 10, speed = 8):
        self.name = name
        self.health = health
        self.strength = strength
        self.toughness = toughness
        self.speed = speed
        Character.all_characters.append(self)

    def info(self):
        print(f"***** {self.name} *****")
        print(f"Health: {self.health}")
        print(f"Strength: {self.strength}")
        print(f"Toughness: {self.toughness}")
        return self

    def shout(self):
        print("I am a character!")
        return self

    def changeHealth(self, amount):
        self.health += amount
        return self

    def punch(self, attackee):
        print(f"{self.name} is attacking {attackee.name}")
        connect_roll = random.randint(1, 20)
        if connect_roll > attackee.speed:
            print("Connected a punch")
            attackee.block(self)
        else:
            print("Missed")
            

    def block(self, attacker):
        print(f"{self.name} is blocking against {attacker.name}")
        block_roll = random.randint(1,20)
        if block_roll < self.speed:
            return False
        else:
            damage = random.randint(0, attacker.strength)
            print(f"{self.name} took {damage} amount of damage")
            self.changeHealth(-damage)
        return self

    @classmethod
    def show_stats(cls):
        for character in cls.all_characters:
            character.info()
            character.shout()
        return cls

class Dwarf(Character):
    def __init__(self, name, health=150, strength=13, toughness=11, speed=3):
        super().__init__(name, health, strength, toughness, speed)

    def shout(self):
        print("I am a dwarf!")
        return self

class MountainDwarf (Dwarf):
    def __init__(self, name, health=150, strength=13, toughness=11, speed=10):
        super().__init__(name, health, strength, toughness, speed)

    def shout(self):
        print("I live in the mountains!")
        super().shout()
        return self

class Giant(Character):
    def __init__(self, name):
        super().__init__(name, health=80, strength=16, toughness=13, speed=3)

    def shout(self):
        print("I am a giant!")
        return self

p1 = MountainDwarf("Yoana")
p2 = Giant("Cody")
p1.punch(p2)

# p1 = Character('Dawson', 1000, 15, 10, 2)
# p2 = Character("Tyler", 100, 8, 19, 15)

# print(p1.info())
# print(p2.info())

# p1.punch(p2)
Character.show_stats()