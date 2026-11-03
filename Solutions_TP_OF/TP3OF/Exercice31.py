def deriver(P):
    """
    Calcule la dérivée du polynôme P.
    """
    if len(P) <= 1:
        return [0]
    return [i * P[i] for i in range(1, len(P))]
print(deriver([2, 3, 0, 5]))  # Exemple d'utilisation