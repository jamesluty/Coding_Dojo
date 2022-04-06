from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")



while michelangelo.health > 0 and jack_sparrow.health > 0:
    user = input(f"Can only choose heavy or light attack or defend {michelangelo.name} turn, Enter attack: ")
    michelangelo.attack(jack_sparrow, user)
    jack_sparrow.show_stats()
    michelangelo.show_stats()
    if michelangelo.health <= 0:
        break
