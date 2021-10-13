

from robots import Robot


class Fleet:
    def __init__(self, name):
        self.name = name
        self.fleet_bots = []
        self.size_of_fleet = len(self.fleet_bots)

    def build_fleet(self, object_var):
        self.fleet_bots.append(object_var)



mecha_godzilla = Robot("Mecha Godzilla", 200)
titanium_samuri = Robot("Titanium Samuri", 150)
jet = Robot('Jet', 100)
robo_gang = Fleet('Robo Gang')
robo_gang.build_fleet(mecha_godzilla)
robo_gang.build_fleet(titanium_samuri)
robo_gang.build_fleet(jet)