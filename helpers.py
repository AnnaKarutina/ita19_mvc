elemendid = []

# lisame ELEMENT juurde
def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        if nimetus in element.values():
            nimetused.append(nimetus)
    if nimetus in nimetused:
        print("Element {} on juba olemas".format(nimetus))
    else:
        elemendid.append({"nimetus":nimetus, "hind":hind, "kogus":kogus})

# lisame ELEMENDID KORRAGA juurde
def lisa_elemendid(elementide_nimekiri):
    global elemendid
    elemendid = elementide_nimekiri

# loeme ELEMENDID korraga
def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    return loetud_elemendid

# loeme KONKREETNE element
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei eksisteeri".format(nimetus)
    else:
       return elemendid[nimetused.index(nimetus)]

def main():
    # loome katseandmestik
    katse_elemendid = [
        {"nimetus": "leib", "hind":0.80, "kogus": 20},
        {"nimetus": "piim", "hind":0.50, "kogus": 15},
        {"nimetus": "vein", "hind":5.60, "kogus": 5},
    ]

    # testime elementide lisamist
    lisa_elemendid(katse_elemendid)

    # testime üksiku elemendi lisamist
    lisa_element("kohupiim", 0.90, 15)
    lisa_element("vein", 5.60, 5)

    # testime elementide lugemist
    print(loe_element("vein"))
    print(loe_element("limonaad"))

# käivitame
if __name__ == "__main__":
    main()
