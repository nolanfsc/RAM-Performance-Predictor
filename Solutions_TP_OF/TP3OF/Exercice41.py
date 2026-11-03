def dichotomie(f, a, b, epsilon):
    """
    Implémente la méthode de dichotomie pour trouver une racine de la fonction f dans l'intervalle [a, b]. cf. cours développement 
    """
    if f(a) * f(b) >= 0:
        raise ValueError("La fonction doit avoir des signes opposés aux extrémités de l'intervalle.")
    
    while (b - a) / 2 > epsilon:
        c = (a + b) / 2
        if f(c) == 0:
            return c  # c est une racine exacte
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2  # Retourne le milieu de l'intervalle comme approximation de la racine
racine = dichotomie(lambda x: x**2 - 2, 0, 2, 1e-9)
print(racine)
print(abs(racine - 2 ** 0.5) < 1e-9)