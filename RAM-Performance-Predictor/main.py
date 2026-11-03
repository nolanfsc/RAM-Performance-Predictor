
from calculs_ram import (
    calculer_moyenne,
    calculer_ecart_type,
    calculer_latence_cas,
    calculer_bande_passante
)

from gestion_donnees import (
    charger_plateforme,
    generer_donnees_simulees
)

from modele_prediction import (
    preparer_donnees,
    entrainer_modele,
    predire_performances,
    creer_caracteristiques
)


def afficher_statistiques(donnees):
    indicateurs = ["read", "write", "copy", "latency"]
    profils = {}

    for benchmark in donnees:
        profil = benchmark["profil"]

        if profil not in profils:
            profils[profil] = []

        profils[profil].append(benchmark)

    print("\n========== STATISTIQUES DES BENCHMARKS ==========")

    for nom_profil, mesures in profils.items():
        print(f"\n--- Profil {nom_profil} ---")

        for indicateur in indicateurs:
            valeurs = [mesure[indicateur] for mesure in mesures]

            moyenne = calculer_moyenne(valeurs)
            ecart_type = calculer_ecart_type(valeurs)

            print(
                f"{indicateur} : "
                f"Moyenne = {moyenne:.2f} | "
                f"Écart-type = {ecart_type:.2f}"
            )



def evaluer_modele(coefficients, donnees_test):
    X_test, Y_test = preparer_donnees(donnees_test)

    print("\n========== ÉVALUATION DU MODÈLE ==========")

    for indicateur in Y_test:
        valeurs_reelles = Y_test[indicateur]
        predictions = []

        for caracteristiques in X_test:
            resultat = predire_performances(
                coefficients,
                caracteristiques
            )

            predictions.append(resultat[indicateur])

        # Erreur absolue moyenne (MAE)
        erreurs = [
            abs(reel - prediction)
            for reel, prediction in zip(valeurs_reelles, predictions)
        ]

        mae = calculer_moyenne(erreurs)

        # Coefficient de détermination R²
        moyenne_reelle = calculer_moyenne(valeurs_reelles)

        somme_erreurs = sum(
            (reel - prediction) ** 2
            for reel, prediction in zip(valeurs_reelles, predictions)
        )

        somme_totale = sum(
            (reel - moyenne_reelle) ** 2
            for reel in valeurs_reelles
        )

        if somme_totale == 0:
            r2 = None
        else:
            r2 = 1 - (somme_erreurs / somme_totale)

        unite = "ns" if indicateur == "latency" else "MB/s"

        print(f"\n{indicateur.upper()}")
        print(f"Erreur moyenne (MAE) : {mae:.2f} {unite}")

        if r2 is not None:
            print(f"Coefficient R² : {r2:.4f}")
        else:
            print("Coefficient R² : impossible à calculer")



def comparer_avec_reel(coefficients, donnees_reelles):
    benchmark = donnees_reelles[0]

    caracteristiques = creer_caracteristiques(
        benchmark["frequence"],
        benchmark["cl"],
        benchmark["trcd"],
        benchmark["trp"],
        benchmark["command_rate"]
    )

    predictions = predire_performances(
        coefficients,
        caracteristiques
    )

    print("\n========== COMPARAISON AVEC AIDA64 ==========")

    for indicateur in predictions:
        valeurs_reelles = [
            mesure[indicateur]
            for mesure in donnees_reelles
        ]

        moyenne_reelle = calculer_moyenne(valeurs_reelles)
        prediction = predictions[indicateur]

        ecart = abs(moyenne_reelle - prediction)
        erreur_relative = (ecart / moyenne_reelle) * 100

        unite = "ns" if indicateur == "latency" else "MB/s"

        print(f"\n{indicateur.upper()}")
        print(f"Moyenne AIDA64 : {moyenne_reelle:.2f} {unite}")
        print(f"Prédiction : {prediction:.2f} {unite}")
        print(f"Écart : {ecart:.2f} {unite}")
        print(f"Erreur relative : {erreur_relative:.2f} %")


def demander_prediction(coefficients):
    print("\n========== PRÉDICTION RAM ==========")

    try:
        frequence = int(input("Fréquence RAM (MT/s) : "))
        cl = int(input("CAS Latency (CL) : "))
        trcd = int(input("tRCD : "))
        trp = int(input("tRP : "))
        command_rate = int(input("Command Rate (1 ou 2) : "))

        if frequence <= 0 or cl <= 0 or trcd <= 0 or trp <= 0:
            print("\nErreur : les valeurs doivent être positives.")
            return

        if command_rate not in [1, 2]:
            print("\nErreur : le Command Rate doit être égal à 1 ou 2.")
            return

        caracteristiques = creer_caracteristiques(
            frequence,
            cl,
            trcd,
            trp,
            command_rate
        )

        predictions = predire_performances(
            coefficients,
            caracteristiques
        )

        print("\n========== PERFORMANCES ESTIMÉES ==========")

        print(f"Lecture : {predictions['read']:.2f} MB/s")
        print(f"Écriture : {predictions['write']:.2f} MB/s")
        print(f"Copie : {predictions['copy']:.2f} MB/s")
        print(f"Latence : {predictions['latency']:.2f} ns")

    except ValueError:
        print("\nErreur : veuillez entrer uniquement des nombres entiers.")


# --------------------------------------------------
# PROGRAMME PRINCIPAL
# --------------------------------------------------

print("========================================")
print("       RAM PERFORMANCE PREDICTOR")
print("========================================")

print("\nChoisissez une plateforme :")
print("1 - Intel DDR4")
print("2 - AMD DDR5")

choix = input("\nVotre choix : ")

if choix == "1":
    plateforme = "intel_ddr4"

elif choix == "2":
    plateforme = "amd_ddr5"

else:
    raise ValueError("Choix invalide.")


# Chargement des données réelles

donnees_reelles = charger_plateforme(plateforme)

print("\nNombre de benchmarks réels :", len(donnees_reelles))


# Analyse des données réelles

afficher_statistiques(donnees_reelles)


# Analyse théorique

print("\n========== ANALYSE THÉORIQUE ==========")

for benchmark in donnees_reelles:
    frequence = benchmark["frequence"]
    cl = benchmark["cl"]

    latence = calculer_latence_cas(frequence, cl)
    bande_passante = calculer_bande_passante(frequence)

    print(f"\nProfil : {benchmark['profil']}")
    print(f"Fréquence : {frequence} MT/s")
    print(f"Latence CAS théorique : {latence:.2f} ns")
    print(f"Latence AIDA64 : {benchmark['latency']:.2f} ns")
    print(f"Bande passante théorique : {bande_passante:.2f} GB/s")
    print(f"Lecture AIDA64 : {benchmark['read']:.2f} MB/s")


# Modèle de prédiction AMD DDR5

if plateforme == "amd_ddr5":

    print("\n========== GÉNÉRATION DES DONNÉES ==========")

    donnees_simulees = generer_donnees_simulees(30)

    donnees_entrainement = donnees_simulees[:24]
    donnees_test = donnees_simulees[24:]

    print("Mesures réelles :", len(donnees_reelles))
    print("Données simulées :", len(donnees_simulees))
    print("Données d'entraînement :", len(donnees_entrainement))
    print("Données de test :", len(donnees_test))

    # Préparation et entraînement

    X_train, Y_train = preparer_donnees(donnees_entrainement)

    coefficients = entrainer_modele(X_train, Y_train)

    print("\nModèle entraîné avec succès !")

    # Évaluation

    evaluer_modele(coefficients, donnees_test)

    # Comparaison avec les mesures réelles

    comparer_avec_reel(coefficients, donnees_reelles)

    # Prédiction personnalisée

    demander_prediction(coefficients)


else:
    print("\nLe modèle de prédiction DDR4 n'est pas encore disponible.")
    print("Les données Intel restent séparées des données AMD DDR5.")


print("\n========== FIN DU PROGRAMME ==========")
