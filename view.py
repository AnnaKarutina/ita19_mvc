class View:
    def kuva_elemendid(self, elemendid):
        print("Kõik elemendid")
        for element in elemendid:
            print("- {}".format(element))