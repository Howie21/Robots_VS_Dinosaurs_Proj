import random

from weapon import Weapon


class Robot:
    def __init__(self, Name, Health,):
        self.name = Name
        self.health = Health
        self.weapon = Weapon()
        self.weapon_damage = random.randint(15, 25)
        self.power_level = Health / 2


