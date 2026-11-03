A = [[1, 2, 2],
     [1, 3, -2],
     [3, 5, 8]]

print(A[0])        # la premiere ligne
print(A[0][2])     # ligne 0, colonne 2
print(len(A), len(A[0]))   # nombre de lignes, nombre de colonnes

def transpose(A):
    """Renvoie la transposée de la matrice A"""
    n = len(A)        # nombre de lignes
    m = len(A[0])     # nombre de colonnes
    T = [[0] * n for i in range(m)]  # création d'une matrice m x n remplie de zéros
    for i in range(n):
        for j in range(m):
            T[j][i] = A[i][j]
    return T
print(transpose([[1, 2, 3], [4, 5, 6]]))