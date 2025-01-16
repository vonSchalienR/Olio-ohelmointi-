class Muistilista:
    def __init__(self, otsikko: str, merkinnat: list):
        self.otsikko = otsikko
        self.merkinnat = merkinnat

class Asiakas:
    def __init__(self, tunniste: str, saldo: float, alennusprosentti: int):
        self.tunniste = tunniste
        self.saldo = saldo
        self.alennusprosentti = alennusprosentti

class Kaapeli:
    def __init__(self, malli: str, pituus: float, maksiminopeus: int, kaksisuuntainen: bool):
        self.malli = malli
        self.pituus = pituus
        self.maksiminopeus = maksiminopeus
        self.kaksisuuntainen = kaksisuuntainen

class Pankkitili:
    def __init__(self, saldo: int, omistaja: str):
        self.saldo = saldo
        self.omistaja = omistaja

# Funktio luo uuden tiliolion ja palauttaa sen
def avaa_tili(nimi: str):
    uusi_tili = Pankkitili(0, nimi)
    return uusi_tili

# Funktio asettaa parametrina saamansa rahasumman parametrina olevalle tilille
def laita_rahaa_tilille(tili: Pankkitili, summa: int):
    tili.saldo += summa

# Esimerkki
def main():
    pekan_tili = avaa_tili("Pekka Python")
    print(pekan_tili.saldo)  # Tulostaa 0

    laita_rahaa_tilille(pekan_tili, 500)

    print(pekan_tili.saldo)  # Tulostaa 500

if __name__ == "__main__":
    main()
