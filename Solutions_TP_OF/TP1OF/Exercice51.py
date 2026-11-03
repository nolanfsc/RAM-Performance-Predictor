
import math


def heron(a):
    x = a / 2.0  # Initialisation de la valeur de départ pour l'itération
    while True:
        y = (x + a / x) / 2.0
        if abs(y - x) < 1e-12:  # Critère de convergence pour arrêter l'itération
            break
        x = y
    return x
print(heron(2))  # Exemple d'utilisation du cours version methode de Héron
print(math.sqrt(2))  # Exemple d'utilisation du cours version racine carrée