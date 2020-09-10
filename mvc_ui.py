from model import Model
from view import View
from controller import Controller

elemendid = [
    {"nimetus": "leib", "hind":0.80, "kogus": 20},
    {"nimetus": "piim", "hind":0.50, "kogus": 15},
    {"nimetus": "vein", "hind":5.60, "kogus": 5},
]
# testimine
# loome uus andmestik
pood = Controller(Model(elemendid), View())
# kõikide elementide kuvamine
pood.kuva_elemendid()

