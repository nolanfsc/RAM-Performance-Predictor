import time

from Exercice11 import evaluer_naif

def evaluer_naif(P,x):
    """
    Évalue le polynôme P en x en utilisant la méthode naïve.
    """
    resultat = 0
    for i in range(len(P)):
        resultat += P[i] * (x ** i)
    return resultat

print(evaluer_naif([2, 3,0,5], 2))  # Exemple d'utilisation

def evaluer_horner(P, x):
    """
    Évalue le polynôme P en x en utilisant la méthode de Horner.
    """
    resultat = 0
    for coeff in reversed(P):
        resultat = resultat * x + coeff
    return resultat
print(evaluer_horner([2, 3, 0, 5], 2))  # Exemple d'utilisation
for degre in (200, 400, 800):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 3)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer_horner(P, 3)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>4} : rapport {t_naif / t_horner:.1f} | resultats egaux : {a == b}")