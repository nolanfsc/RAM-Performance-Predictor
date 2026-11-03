def celsius_vers_fahrenheit(c):
    """Convertit une température de degrés Celsius en degrés Fahrenheit."""
    return c * 9 / 5 + 32

print(celsius_vers_fahrenheit(100))
print(celsius_vers_fahrenheit(-40))

def nombre_de_chiffres(n):
    """Retourne le nombre de chiffres dans un entier n."""
    if n == 0:
        return 1
    count = 0
    while n:
        n //= 10
        count += 1
    return count

print(nombre_de_chiffres(2026))  
print(nombre_de_chiffres(7))