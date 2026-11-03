from Exercice31 import pgcd
from Exercice41 import dechiffrer, message, secret

def toutes_les_cles_valides():
    return [
        (a, b)
        for a in range(1, 26) if pgcd(a, 26) == 1
        for b in range(26)
    ]

essais = toutes_les_cles_valides()
bons = [(a, b) for a, b in essais if dechiffrer(secret, a, b) == message]

print(len(essais), "clefs essayées")
print("Clé(s) trouvée(s) :", bons)