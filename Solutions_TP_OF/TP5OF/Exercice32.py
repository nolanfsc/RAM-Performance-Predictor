def inverse_modulaire(a,b):
    """Renvoie l'inverse modulaire de a modulo b, si il existe."""
    for x in range(1, b):
        if (a * x) % b == 1:
            return x
    return None
print(inverse_modulaire(5, 26))
print((5 * 21) % 26)

try:
    inverse_modulaire(4, 26)
except ValueError as erreur:
    print("erreur attendue :", erreur)