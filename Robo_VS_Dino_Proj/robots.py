import random



class Robot:
    def __init__(self, Name, Health,):
        self.name = Name
        self.health = Health
        self.weapon = Weapon()
        self.weapon_damage = random.randint(15, 25)


arsenal_of_weapons = [
    'Lazer Sword', 
    'Mecha Chainsaw', 
    'Rocket Pod', 
    ]

class Weapon:
    def __init__(self):
        self.name = random.choice(list(arsenal_of_weapons))