
from dinosaurs import Dinosaur


class Herd:
    def __init__(self, name):
        self.name = name
        self.herd_dino = []
        self.size_of_herd = len(self.herd_dino)
    
    def herd_dinos(self,):
        t_rex = Dinosaur('T-Rex', 200)
        triceratops = Dinosaur('Triceratops', 150)
        mosasaurus = Dinosaur('Mosasaurus', 100)
        self.herd_dino.extend([t_rex, triceratops, mosasaurus])

        