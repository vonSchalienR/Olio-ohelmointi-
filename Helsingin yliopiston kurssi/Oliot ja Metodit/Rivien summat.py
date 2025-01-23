def rivien_summat(matriisi: list):
    for rivi in matriisi:
        summa = sum(rivi)  # Lasketaan rivin alkioiden summa
        rivi.append(summa)  # Lisätään summa rivin loppuun


matriisi = [[1, 2], [3, 4]]
rivien_summat(matriisi)
print(matriisi)