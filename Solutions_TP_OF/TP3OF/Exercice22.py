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
for degre in (1000, 5000, 20000):
    P = [1] * (degre + 1)

    debut = time.perf_counter()
    a = evaluer_naif(P, 1.0001)
    t_naif = time.perf_counter() - debut

    debut = time.perf_counter()
    b = evaluer_horner(P, 1.0001)
    t_horner = time.perf_counter() - debut

    print(f"degre {degre:>6} : naif {t_naif:.5f} s | horner {t_horner:.5f} s "
          f"| rapport {t_naif / t_horner:.1f} | ecart des valeurs {abs(a - b):.2e}")