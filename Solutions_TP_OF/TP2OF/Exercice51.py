def facteurs_premiers(n):
    facteurs = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            facteurs.append(d)
            n //= d
        d += 1
    if n > 1:
        facteurs.append(n)
    return facteurs
def produit_facteurs(facteurs):
    produit = 1
    for facteur in facteurs:
        produit *= facteur
    return produit
print(facteurs_premiers(360))  # Sortie supposée: [2, 2, 2, 3, 3, 5]
print(produit_facteurs(facteurs_premiers(360)))  # Sortie supposée: 360