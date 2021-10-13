
import random


arsenal_of_weapons = [
    'Lazer Sword', 
    'Mecha Chainsaw', 
    'Rocket Pod', 
    ]

class Weapon:
    def __init__(self):
        self.name = random.choice(list(arsenal_of_weapons))