
from Exercice11 import lettre_vers_nombre, nombre_vers_lettre
from Exercice12 import nettoyer
from Exercice21 import chiffrer


def dechiffrer(texte,a,b):
    """Déchiffre le texte avec la fonction affine f(x) = ax + b mod 26."""
    texte = nettoyer(texte)
    # Calcul de l'inverse de a modulo 26
    a_inv = pow(a, -1, 26)
    return "".join(nombre_vers_lettre((a_inv * (lettre_vers_nombre(c) - b)) % 26) for c in texte)

message = nettoyer("Attaque a l aube")
secret = chiffrer(message, 5, 8)
print(secret)
print(dechiffrer(secret, 5, 8))
print(dechiffrer(secret, 5, 8) == message)

# une clé invalide est refusée au lieu de produire un résultat faux
try:
    dechiffrer(secret, 4, 7)
except ValueError as erreur:
    print("cle refusee :", erreur)