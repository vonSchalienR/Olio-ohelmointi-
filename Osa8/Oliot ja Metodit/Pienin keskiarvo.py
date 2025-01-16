def pienin_keskiarvo(henkilo1: dict, henkilo2: dict, henkilo3: dict):
    def laske_keskiarvo(henkilo):
        return (henkilo["tulos1"] + henkilo["tulos2"] + henkilo["tulos3"]) / 3

    # Lasketaan jokaisen henkilön keskiarvo
    keskiarvo1 = laske_keskiarvo(henkilo1)
    keskiarvo2 = laske_keskiarvo(henkilo2)
    keskiarvo3 = laske_keskiarvo(henkilo3)

    # Luodaan lista henkilöistä ja heidän keskiarvoistaan
    henkilot_ja_keskiarvot = [
        (henkilo1, keskiarvo1),
        (henkilo2, keskiarvo2),
        (henkilo3, keskiarvo3)
    ]

    # Etsitään henkilö, jonka keskiarvo on pienin
    pienin = min(henkilot_ja_keskiarvot, key=lambda x: x[1])

    # Palautetaan sanakirjaolio henkilölle, jolla on pienin keskiarvo
    return pienin[0]

# Esimerkki:
henkilo1 = {"nimi": "Anna", "tulos1": 5, "tulos2": 7, "tulos3": 6}
henkilo2 = {"nimi": "Ben", "tulos1": 4, "tulos2": 5, "tulos3": 6}
henkilo3 = {"nimi": "Cara", "tulos1": 8, "tulos2": 7, "tulos3": 9}

pienin = pienin_keskiarvo(henkilo1, henkilo2, henkilo3)
print(pienin)
