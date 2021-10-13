
from dinosaurs import Dinosaur


class Herd:
    def __init__(self, name):
        self.name = name
        self.herd_dino = []
        self.size_of_herd = len(self.herd_dinos)
    
    def herd_dinos(self, object_var):
        self.herd_dino.append(object_var)

t_rex = Dinosaur('T-Rex', 200)
triceratops = Dinosaur('Triceratops', 150)
mosasaurus = Dinosaur('Mosasaurus', 100)
dino_herd = Herd('Dino Herd')
dino_herd.herd_dinos(t_rex)
dino_herd.herd_dinos(triceratops)
dino_herd.herd_dinos(mosasaurus)