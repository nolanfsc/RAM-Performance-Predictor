def evaluer(P, x):
    """
    Évalue le polynôme P en x en utilisant la méthode de Horner.
    """
    resultat = 0
    for coeff in reversed(P):
        resultat = resultat * x + coeff
    return resultat


evaluer_horner = evaluer
print(evaluer([2, 3, 0, 5], 2))  # Exemple d'utilisation

def deriver(P):
    """
    Calcule la dérivée du polynôme P.
    """
    if len(P) <= 1:
        return [0]
    return [i * P[i] for i in range(1, len(P))]
print(deriver([2, 3, 0, 5]))  # Exemple d'utilisation

def newton(P, depart, tolerance):
    derivee = deriver(P)
    x = depart
    for tours in range(1, 6):
        fx = evaluer(P, x)
        dfx = evaluer(derivee, x)
        
        if abs(dfx) < 1e-12:  # Évite la division par zéro
            raise ValueError("La dérivée est trop proche de zéro.")
        
        x_suivant = x - fx / dfx
        
        if abs(x_suivant - x) < tolerance:
            return x_suivant, tours
        
        x = x_suivant
    
    raise ValueError("La méthode n'a pas convergé en cinq itérations.")

# x^3 - 2x - 5
Q = [-5, -2, 0, 1]
racine, tours = newton(Q, 2, 1e-6)
print(racine, "en", tours, "tours")
print(abs(evaluer(Q, racine)) < 1e-10)