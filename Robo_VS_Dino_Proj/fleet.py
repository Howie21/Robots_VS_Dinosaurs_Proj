
from robots import Robot


class Fleet:
    def __init__(self, name):
        self.name = name
        self.fleet_bots = []
        self.size_of_fleet = len(self.fleet_bots) - 1

    def build_fleet(self):
        mecha_godzilla = Robot("Mecha Godzilla", 200)
        titanium_samuri = Robot("Titanium Samuri", 150)
        jet = Robot('Jet', 100)
        self.fleet_bots.extend(mecha_godzilla, titanium_samuri, jet)
