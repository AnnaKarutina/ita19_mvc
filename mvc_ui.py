from model import Model

elemendid = [
    {"nimetus": "leib", "hind":0.80, "kogus": 20},
    {"nimetus": "piim", "hind":0.50, "kogus": 15},
    {"nimetus": "vein", "hind":5.60, "kogus": 5},
]
# testimine
# loome uus andmestik
pood = Model(elemendid)
# kontrollime sisu
print(pood.loe_elemendid())
# lisame element juurde
pood.lisa_element("kohupiim", 0.60, 15)
print(pood.loe_elemendid())
# lisame olemasolev element - trükib meie veateade ilusti
pood.lisa_element("vein", 10.0, 15)
print(pood.loe_elemendid())
# muudame elemendi sisu
pood.uuenda_element("vein", 10.60, 15)
print(pood.loe_elemendid())
# proovime muuta element, mis ei eiksisteeri - ilusti trükib meie veateade
pood.uuenda_element("limonaad", 10.60, 15)
print(pood.loe_elemendid())
# kustutame üks element
pood.kustuta_element("vein")
print(pood.loe_elemendid())
# kustutame kõik elemendid
pood.kustuta_elemendid()
print(pood.loe_elemendid())