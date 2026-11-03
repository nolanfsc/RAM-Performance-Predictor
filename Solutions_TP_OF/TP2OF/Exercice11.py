def diviseur(n):
    if n == 0:
        return "undefined"
    divisors = []
    for i in range(1, abs(n) + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print(diviseur(28))  # Sortie supposée: [1, 2, 4, 7, 14, 28]