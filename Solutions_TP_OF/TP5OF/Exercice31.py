def pgcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

valides = [a for a in range(1, 26) if pgcd(a, 26) == 1]
print(valides)
print(len(valides), "valeurs possibles pour a")