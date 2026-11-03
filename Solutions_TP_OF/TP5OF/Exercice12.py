def nettoyer(texte):
    """Supprime les caractères non alphabétiques et met en majuscule."""
    return "".join(c for c in texte.upper() if c.isalpha())
print(nettoyer("Été, à Paris !"))