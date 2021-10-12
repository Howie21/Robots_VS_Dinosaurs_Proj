




class Fleet:
    def __init__(self, name):
        self.name = name
        self.fleet_bots = []
        self.size_of_fleet = len(self.fleet_bots)

    def build_fleet(self, object_var):
        self.fleet_bots.append(object_var)