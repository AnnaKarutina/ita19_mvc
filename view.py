class View:
    def kuva_elemendid(self, elemendid):
        print("Kõik elemendid")
        for element in elemendid:
            print("- {}".format(element))

    def kuva_element(self, nimetus, element):
        print(" Kuvame {} elementi andmed".format(nimetus))
        print(element)
