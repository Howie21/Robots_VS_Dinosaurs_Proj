
from robots import Robot



class Fleet:
    def __init__(self, name, number_of_bots):
        self.name = name
        self.bots = number_of_bots
        self.fleet_bots = []
        self.size_of_fleet = len(self.fleet_bots)

    def create_bots(self, Name, Health):
        bot = Robot(Name, Health)
        self.fleet_bots.append(bot)