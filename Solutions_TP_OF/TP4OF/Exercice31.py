import numpy as np
import random
import time

def produit_matriciel(A, B):
    """Renvoie le produit matriciel de A et B"""
    n = len(A)        # nombre de lignes de A
    m = len(A[0])     # nombre de colonnes de A
    p = len(B[0])     # nombre de colonnes de B
    C = [[0] * p for i in range(n)]  # création d'une matrice n x p remplie de zéros
    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C
print(produit_matriciel([[1, 2], [3, 4]], [[0, 1], [1, 0]]))

random.seed(42)

def matrice_aleatoire(n):
    return [[random.random() for _ in range(n)] for _ in range(n)]

for n in (40, 80, 120):
    A = matrice_aleatoire(n)
    B = matrice_aleatoire(n)
    debut = time.perf_counter()
    produit_matriciel(A, B)
    print(f"n = {n:>3} : {time.perf_counter() - debut:.4f} s")

A = np.array([[1.0, 2.0, 2.0],
              [1.0, 3.0, -2.0],
              [3.0, 5.0, 8.0]])
b = np.array([2.0, -1.0, 8.0])

print(A.shape)
print(A.T)          # transposée
print(A @ A)        # produit matriciel
print(A * A)        # produit terme à terme : ce n'est PAS le produit matriciel

n = 120
A = matrice_aleatoire(n)
B = matrice_aleatoire(n)

debut = time.perf_counter()
produit_matriciel(A, B)
t_python = time.perf_counter() - debut

An, Bn = np.array(A), np.array(B)
debut = time.perf_counter()
An @ Bn
t_numpy = time.perf_counter() - debut

print(f"python pur {t_python:.4f} s")
print(f"numpy      {t_numpy:.6f} s")
print("rapport :", round(t_python / max(t_numpy, 1e-9)))