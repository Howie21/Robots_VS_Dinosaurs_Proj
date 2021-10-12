from herd import Herd
from dinosaurs import Dinosaur
from robots import Robot
from fleet import Fleet

mecha_godzilla = Robot("Mecha Godzilla", 200)
titanium_samuri = Robot("Titanium Samuri", 150)
jet = Robot('Jet', 100)
robo_gang = Fleet('Robo Gang')
robo_gang.build_fleet(mecha_godzilla)
robo_gang.build_fleet(titanium_samuri)
robo_gang.build_fleet(jet)
t_rex = Dinosaur('T-Rex', 200)
triceratops = Dinosaur('Triceratops', 150)
mosasaurus = Dinosaur('Mosasaurus', 100)
dino_herd = Herd('Dino Herd')
dino_herd.herd_dinos(t_rex)
dino_herd.herd_dinos(triceratops)
dino_herd.herd_dinos(mosasaurus)