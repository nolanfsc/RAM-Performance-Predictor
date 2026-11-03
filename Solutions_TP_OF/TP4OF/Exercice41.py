def resoudre_gauss(A, b):
    """Résout le système Ax = b par la méthode de Gauss"""
    n = len(A)
    for k in range(n):
        max_index = max(range(k, n), key=lambda i: abs(A[i][k]))
        if A[max_index][k] == 0:
            raise ValueError("Le système n'a pas de solution unique")
        A[k], A[max_index] = A[max_index], A[k]
        b[k], b[max_index] = b[max_index], b[k]
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= factor * A[k][j]
            b[i] -= factor * b[k]
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
    return x

A = [[1, 2, 2], [1, 3, -2], [3, 5, 8]]
b = [2, -1, 8]
x = resoudre_gauss(A, b)
print([round(v, 10) for v in x])

# vérification : A x doit redonner b
verif = [sum(A[i][j] * x[j] for j in range(3)) for i in range(3)]
print([round(v, 10) for v in verif])