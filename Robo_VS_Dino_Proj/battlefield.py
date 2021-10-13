from herd import Herd
from fleet import Fleet

version = "1.0"

class Battlefield:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.dino_herd = Herd("Triple Threat Pack")
        self.robot_group = Fleet("Mecha Group 6")
        
    

    def run_game(self):
        self.dino_herd.herd_dinos()
        self.robot_group.build_fleet()
        self.display_intro(self.robot_group.fleet_bots, self.dino_herd.herd_dino)
        

    def display_intro(self, robos_list, dinos_list):
        print(f'Welcome to Robots V Dinosaurs {version}. \nIn this Console game you will watch as 3 Robots face off against 3 Dinosaurs, to see who comes out on top! ')
        for robot in robos_list:
            print(f'Fleet {self.robot_group.name} offers {robot.name} ')
        for dino in dinos_list:
            print(f'Nature offers {dino.name} from the Herd {self.dino_herd.name} ')
        print(f'{self.dino_herd.name} will be facing off against {self.robot_group.name} in this eveings fight. \nAnd it looks like they are read to begin ')
        self.battle()

    def battle(self):
        print(f'\nAND SO THE BATTLE BEGINS!')

        

    def dino_attack(self, dino, robot):
        attacking_dino = dino
        defending_robot = robot
        
        
    
    def robo_attack(self, robot, dino):
        
    
    def display_winner(self):
        
    
