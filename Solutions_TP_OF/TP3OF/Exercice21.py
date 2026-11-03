def evaluer_horner(P, x):
    """
    Évalue le polynôme P en x en utilisant la méthode de Horner.
    """
    resultat = 0
    for coeff in reversed(P):
        resultat = resultat * x + coeff
    return resultat
print(evaluer_horner([2, 3, 0, 5], 2))  # Exemple d'utilisation