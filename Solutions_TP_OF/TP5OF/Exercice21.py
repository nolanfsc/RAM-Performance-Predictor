

from Exercice11 import lettre_vers_nombre, nombre_vers_lettre
from Exercice12 import nettoyer

def chiffrer(texte,a,b):
    """Chiffre le texte avec la fonction affine f(x) = ax + b mod 26."""
    texte = nettoyer(texte)
    return "".join(nombre_vers_lettre((a * lettre_vers_nombre(c) + b) % 26) for c in texte)
message = "ATTAQUEALAUBE"
print(chiffrer(message, 5, 8))
print(chiffrer(message, 1, 3))   # le chiffre de César