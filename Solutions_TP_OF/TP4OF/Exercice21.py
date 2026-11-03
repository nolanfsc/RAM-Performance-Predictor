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