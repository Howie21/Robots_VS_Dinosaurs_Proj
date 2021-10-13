from herd import Herd
from fleet import Fleet
import random

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
        dino_attacks = ['Bite', 'Thrash', 'Ram', 'Neck Slap']
        if defending_robot.health > 0 and attacking_dino.energy >= 10:
            dino_attack = random.choice(dino_attacks)
            print(f'{attacking_dino.name} attacks {defending_robot.name} for {attacking_dino.attack_power} Damage using {dino_attack} ')
            defending_robot.health = defending_robot.health - (attacking_dino.attack_power / 2)
            attacking_dino.energy = attacking_dino.energy - 10
            defending_robot.power_level += 10
            if defending_robot.health <= 0:
                self.display_winner(dino, robot)
        elif defending_robot.health > 0 and attacking_dino.energy < 10:
            print(f'{attacking_dino.name} only has {attacking_dino.energy} right now. They will miss this turn. ')
            attacking_dino.energy += 10


        
    
    def robo_attack(self, robot, dino):
        pass
    
    def display_winner(self, winner, loser):
        print(f'{winner.name} beat {loser.name} using {winner.weapon} ')
        if loser == self.dino_herd[0] or loser == self.dino_herd[1] or loser == self.dino_herd[2]:
            self.dino_herd.remove[loser]
        elif loser == self.robot_group[0] or loser == self.robot_group[1] or loser == self.robot_group[2]:
            self.robot_group.remove[loser]
