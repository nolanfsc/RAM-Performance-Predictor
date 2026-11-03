def division_euclidienne(a, b):
    """
    Effectue la division euclidienne de a par b.
    
    Args:
        a (int): Le dividende.
        b (int): Le diviseur.
        
    """
    if b == 0:
        raise ValueError("Le diviseur ne peut pas être zéro.")
    
    quotient = a // b
    reste = a % b
    
    return quotient, reste

a= 123456789
print(division_euclidienne(a, 10))  # Exemple d'utilisation du cours