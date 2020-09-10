class View:
    def kuva_elemendid(self, elemendid):
        print("Kõik elemendid")
        for element in elemendid:
            print("- {}".format(element))

    def kuva_element(self, nimetus, element):
        print(" Kuvame {} elementi andmed".format(nimetus))
        print(element)

    def lisa_element(self, nimetus, hind, kogus):
        print("Elemendi lisamine")
        print("Lisatud {} hinnaga {}EUR koguses {}".format(nimetus, hind, kogus))


