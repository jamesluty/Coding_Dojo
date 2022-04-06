from classes.characters import Character

class Pirate(Character):

    def __init__( self , name, health=100, energy=100):
        super().__init__(name, health, energy)

    def show_stats( self ):
        print(f"Name: {self.name}\nHealth: {self.health}\nEnergy: {self.energy}\n")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        return self

