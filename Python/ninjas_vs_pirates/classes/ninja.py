from classes.characters import Character
import random

class Ninja(Character):

    def __init__( self, name, health=100, energy =100):
        super().__init__(name, health, energy)

    def show_stats( self ):
        print(f"Name: {self.name}\nHealth: {self.health}\nEnergy: {self.energy}\n")

    def attack(self , pirate, attack):

        light = 10
        heavy = 20
        compAttack = random.randint(1,3)

        if attack == "defend":
            if self.energy != 100:
                self.energy +=10

        elif compAttack == 3:
            print("Pirate defended your attack")
            self.energy -= 10

        elif attack == "light" or attack == "heavy":

            if self.health > 0:
                if attack == "light":
                    if self.energy >= 10:
                        pirate.health -= light
                        self.energy -= 20
                        print(f"You did 10 damage and used 10 energy, Pirate's health is now {pirate.health}")
                    else:
                        print("You do not have enought energy for light attack")
                elif attack =="heavy":
                    if self.energy >= 40:
                        pirate.health -= heavy
                        self.energy -= 40
                        print(f"You did 20 damage and used 30 energy, Pirate's health is now {pirate.health}")
                    else:
                        print("You do not have enough energy for heavy attack")
                else:
                    print(f"{attack} attack type does not exist")
            else:
                print("You are dead")
                return

            if pirate.health > 0:

                if compAttack == 1:
                    if pirate.energy >= 40:
                        self.health -= heavy
                        pirate.energy -= 40
                        print(f"Pirate did 10 damage and used 30 energy, Your health is now {self.health}")
                    else:
                        print("Pirate didn't have enough energy for attack")
                else:
                    if pirate.energy >= 10:
                        self.health -= light
                        pirate.energy -= 20
                        print(f"Pirate did 20 damage and used 10 energy, Your health is now {self.health}")
                    else:
                        print("Pirate didn't have enough energy for attack")
            else:
                print("Pirate is dead")
                return

            if self.energy < 100:
                self.energy += 10
            if pirate.energy < 100:
                pirate.energy += 10

        else: 
            print("Not a valid input")


        return self