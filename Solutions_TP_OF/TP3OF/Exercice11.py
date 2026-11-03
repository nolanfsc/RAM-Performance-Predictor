def evaluer_naif(P,x):
    """
    Évalue le polynôme P en x en utilisant la méthode naïve.
    """
    resultat = 0
    for i in range(len(P)):
        resultat += P[i] * (x ** i)
    return resultat

print(evaluer_naif([2, 3,0,5], 2))  # Exemple d'utilisation