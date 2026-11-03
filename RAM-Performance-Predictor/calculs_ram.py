def calculer_latence_cas(frequence, cl):
    if frequence <= 0:
        raise ValueError("La fréquence doit être supérieure à 0.")

    if cl <= 0:
        raise ValueError("La valeur CL doit être supérieure à 0.")

    latence = (cl * 2000) / frequence

    return latence

def convertir_timing_ns(frequence, timing):
    if frequence <= 0:
        raise ValueError("La fréquence doit être supérieure à 0.")

    if timing <= 0:
        raise ValueError("Le timing doit être supérieur à 0.")

    temps = (timing * 2000) / frequence

    return temps

def calculer_bande_passante(frequence, canaux=2):
    if frequence <= 0:
        raise ValueError("La fréquence doit être supérieure à 0.")

    if canaux <= 0:
        raise ValueError("Le nombre de canaux doit être supérieur à 0.")

    bande_passante = (frequence * 8 * canaux) / 1000

    return bande_passante

def calculer_moyenne(valeurs):
    if len(valeurs) == 0:
        raise ValueError("La liste ne peut pas être vide.")

    moyenne = sum(valeurs) / len(valeurs)

    return moyenne

def calculer_ecart_type(valeurs):
    if len(valeurs) == 0:
        raise ValueError("La liste ne peut pas être vide.")

    moyenne = calculer_moyenne(valeurs)

    somme_carres = 0

    for valeur in valeurs:
        somme_carres += (valeur - moyenne) ** 2

    variance = somme_carres / len(valeurs)

    ecart_type = variance ** 0.5

    return ecart_type