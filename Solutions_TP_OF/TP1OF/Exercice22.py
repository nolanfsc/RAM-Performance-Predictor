def presque_egal(a, b, epsilon=1e-9):
    """
    Vérifie si deux nombres flottants a et b sont presque égaux avec une tolérance epsilon.
    
    :param a: Premier nombre flottant
    :param b: Deuxième nombre flottant
    :param epsilon: Tolérance pour la comparaison (par défaut 1e-9)
    :return: True si a et b sont presque égaux, False sinon
    """
    return abs(a - b) < epsilon
print(presque_egal(0.1 + 0.2, 0.3))  # Exemple d'utilisation du cours
print(presque_egal(1.0,1.5))  # Exemple d'utilisation du cours
