import math

a = 0.1 + 0.2
b = 0.3
print(abs(a - b) < 1e-9)
print(math.isclose(a, b))

total = 0.0
for i in range(1000):
    total += 0.1
print (total) # Affiche le total calculé qui vaut environ 100
print(abs(total - 100.0) < 1e-12) # Vérifie si le total est égal à 100 avec une tolérance de 1e-12
print(total == 100.0) # Vérifie si le total est exactement égal à 100
print(total-100.0 < 1e-12) # Vérifie si la différence entre le total et 100 est inférieure à 1e-12