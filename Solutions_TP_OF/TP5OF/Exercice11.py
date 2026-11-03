def lettre_vers_nombre(c):
    """Numéro de 0 à 25 d'une lettre majuscule."""
    return ord(c) - ord("A")

def nombre_vers_lettre(n):
    """Lettre majuscule correspondant à un numéro de 0 à 25."""
    return chr(n % 26 + ord("A"))

print(lettre_vers_nombre("C"), nombre_vers_lettre(2))
print([nombre_vers_lettre(lettre_vers_nombre(c)) == c for c in "ABCXYZ"])