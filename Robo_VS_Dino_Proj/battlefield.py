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
        while self.dino_herd.herd_dino != [] and self.robot_group.fleet_bots != []:
            print(f'\nAND SO A NEW BATTLE BEGINS!')
            dino_opponet = random.choice(self.dino_herd.herd_dino)
            robot_opponet = random.choice(self.robot_group.fleet_bots)
            print(f'This round will be: {robot_opponet.name} V {dino_opponet.name} ')
            self.dino_attack(dino_opponet, robot_opponet)

        if self.dino_herd.herd_dino == []:
            print(f'The victors of this battle will be {self.robot_group.name}')
        elif self.robot_group.fleet_bots == []:
            print(f'The winner of this fight is The {self.dino_herd.name}')

    def dino_attack(self, dino, robot):
        attacking_dino = dino
        defending_robot = robot
        dino_attacks = ['Bite', 'Thrash', 'Ram', 'Neck Slap']
        if defending_robot.health > 0 and attacking_dino.energy >= 10:
            dino_attack = random.choice(dino_attacks)
            print(f'{attacking_dino.name} attacks {defending_robot.name} for {str(attacking_dino.attack_power)} Damage using {dino_attack} ')
            defending_robot.health = defending_robot.health - (attacking_dino.attack_power / 2)
            attacking_dino.energy = attacking_dino.energy - 10
            defending_robot.power_level += 10
            if defending_robot.health <= 0:
                self.display_winner(dino, robot)
            elif defending_robot.health > 0:
                self.robo_attack(defending_robot, attacking_dino)
        elif defending_robot.health > 0 and attacking_dino.energy < 10:
            print(f'{attacking_dino.name} only has {attacking_dino.energy} right now. They will miss this turn. ')
            attacking_dino.energy += 10
            self.robo_attack(defending_robot, attacking_dino)

    def robo_attack(self, robot, dino):
        attacking_robot = robot
        defending_dino = dino
        robo_weapon = robot.weapon.name
        if defending_dino.health > 0 and attacking_robot.power_level >= 10:
                print(f'{attacking_robot.name} attacks {defending_dino.name} using {robo_weapon} \nfor {str(attacking_robot.weapon_damage)} Damage ')
                defending_dino.health = defending_dino.health - (attacking_robot.weapon_damage / 2)
                attacking_robot.power_level = attacking_robot.power_level - 10
                defending_dino.energy += 10
                if defending_dino.health <= 0:
                    self.display_winner(robot, dino)
                elif defending_dino.health > 0:
                    self.dino_attack(dino, robot)
        elif defending_dino.health > 0 and attacking_robot.power_level < 10:
            print(f'{attacking_robot.name} was unable to attack while recharging. Power level currently at {attacking_robot.power_level} ')
            attacking_robot.power_level += 10
            self.dino_attack(dino, robot)

        
    
    def display_winner(self, winner, loser):
        for dino in self.dino_herd.herd_dino:
            if loser == dino:
                self.dino_herd.herd_dino.remove(loser)
                print(f'{winner.name} beat {loser.name} using {winner.weapon.name} ')
        for robot in self.robot_group.fleet_bots:
            if loser == robot:
                self.robot_group.fleet_bots.remove(loser)
                print(f'{winner.name} beat {loser.name} ')
