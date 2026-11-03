import csv
import os


def lire_benchmarks(chemin):
    if not os.path.exists(chemin):
        raise FileNotFoundError(
            f"Le fichier de données est introuvable : {chemin}"
        )

    with open(chemin, mode="r", newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)

        champs_requis = [
            "numero_mesure", "frequence", "cl", "trcd",
            "trp", "tras", "command_rate",
            "read", "write", "copy", "latency"
        ]

        if not lecteur.fieldnames or not all(
            champ in lecteur.fieldnames for champ in champs_requis
        ):
            raise ValueError("Le fichier CSV ne contient pas toutes les colonnes nécessaires.")

        donnees = list(lecteur)

    if not donnees:
        raise ValueError("Le fichier CSV ne contient aucune mesure.")

    champs_entiers = [
        "numero_mesure", "frequence", "cl",
        "trcd", "trp", "tras", "command_rate"
    ]

    champs_decimaux = ["read", "write", "copy", "latency"]

    try:
        for benchmark in donnees:
            for champ in champs_entiers:
                benchmark[champ] = int(benchmark[champ])

            for champ in champs_decimaux:
                benchmark[champ] = float(benchmark[champ])

    except (ValueError, TypeError):
        raise ValueError("Une ou plusieurs valeurs du CSV sont invalides.")

    return donnees

def charger_plateforme(plateforme):
    fichiers = {
        "intel_ddr4": "donnees/benchmarks_intel_ddr4.csv",
        "amd_ddr5": "donnees/benchmarks_amd_ddr5.csv"
    }

    if plateforme not in fichiers:
        raise ValueError("Plateforme inconnue.")

    return lire_benchmarks(fichiers[plateforme])


import random


def generer_donnees_simulees(nombre=30):
    random.seed(42)

    donnees = []

    frequences = [5200, 5600, 5800, 6000, 6200, 6400]

    for i in range(nombre):
        frequence = random.choice(frequences)

        cl = int(frequence / 200) + random.choice([-2, 0, 2])
        trcd = cl + random.choice([2, 4, 6])
        trp = trcd + random.choice([0, 2])
        tras = trcd + trp
        command_rate = random.choice([1, 2])

        # Estimation simulée des performances
        read = (
            64000
            + (frequence - 6000) * 5
            - (cl - 28) * 30
            - (trcd - 34) * 15
            + random.uniform(-250, 250)
        )

        write = (
            90000
            + (frequence - 6000) * 4
            - (cl - 28) * 20
            - (trcd - 34) * 10
            + random.uniform(-350, 350)
        )

        copy = (
            64000
            + (frequence - 6000) * 4
            - (cl - 28) * 25
            - (trcd - 34) * 12
            + random.uniform(-250, 250)
        )

        latency = (
            63.5
            + (cl - 28) * 0.15
            + (trcd - 34) * 0.08
            + (frequence - 6000) * -0.002
            + random.uniform(-0.5, 0.5)
        )

        donnees.append({
            "profil": f"SIM-{i + 1:02d}",
            "numero_mesure": 1,
            "frequence": frequence,
            "cl": cl,
            "trcd": trcd,
            "trp": trp,
            "tras": tras,
            "command_rate": command_rate,
            "read": round(read, 2),
            "write": round(write, 2),
            "copy": round(copy, 2),
            "latency": round(latency, 2),
            "origine": "simulee"
        })

    return donnees
