class Controller:
    def __init__(self, mudel, vaade):
        self.mudel = mudel
        self.vaade = vaade

    # elementide kuvamine
    def kuva_elemendid(self):
        elemendid = self.mudel.loe_elemendid()
        self.vaade.kuva_elemendid(elemendid)