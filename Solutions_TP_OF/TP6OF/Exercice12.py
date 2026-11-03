import math
A = (1, 2)
B = (4, 6)
AB = (B[0] - A[0], B[1] - A[1])
print(AB)

def vecteur(A, B):
    return (B[0] - A[0], B[1] - A[1])
def produit_scalaire(u,v):
    return u[0]*v[0] + u[1]*v[1]
def norme(u):
    return (u[0]**2 + u[1]**2)**0.5
def angle(u,v):
    from math import acos, degrees
    cos_theta = produit_scalaire(u, v) / (norme(u) * norme(v))
    return degrees(acos(cos_theta))

print(norme((3, 4)), produit_scalaire((1, 2), (3, 4)))
print(angle((1, 0), (1, 1)), angle((1, 0), (0, 1)))
print(angle((2, 0), (2, 0)))

def determiant(u, v):
    return u[0]*v[1] - u[1]*v[0]
def distance_point_droite(P, A, B):
    AP = vecteur(A, P)
    AB = vecteur(A, B)
    return abs(determiant(AP, AB)) / norme(AB)

print(distance_point_droite((0, 0), (0, 1), (1, 0)), math.sqrt(2) / 2)
print(distance_point_droite((3, 4), (0, 0), (1, 0)))