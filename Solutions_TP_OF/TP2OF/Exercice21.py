def pgcd_naif(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

print(pgcd_naif(1071,462))  # Sortie supposée: 21

def pgcd_euclidien(a, b):
    if b == 0:
        return abs(a)
    else:
        return pgcd_euclidien(b, a % b)

print(pgcd_euclidien(1071,462))  # Sortie supposée: 21