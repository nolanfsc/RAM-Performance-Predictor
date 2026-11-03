def creer_caracteristiques(frequence, cl, trcd, trp, command_rate):
    return [
        1,
        frequence / 6000,
        cl / 30,
        trcd / 40,
        trp / 40,
        command_rate / 2
    ]
def preparer_donnees(donnees):
    X = []
    Y = {
        "read": [],
        "write": [],
        "copy": [],
        "latency": []
    }

    for benchmark in donnees:
        caracteristiques = creer_caracteristiques(
            benchmark["frequence"],
            benchmark["cl"],
            benchmark["trcd"],
            benchmark["trp"],
            benchmark["command_rate"]
        )

        X.append(caracteristiques)

        for indicateur in Y:
            Y[indicateur].append(benchmark[indicateur])

    return X, Y


def transposer_matrice(matrice):
    return [
        [ligne[j] for ligne in matrice]
        for j in range(len(matrice[0]))
    ]


def multiplier_matrices(A, B):
    if len(A[0]) != len(B):
        raise ValueError("Dimensions incompatibles.")

    resultat = []

    for ligne in A:
        nouvelle_ligne = []

        for colonne in transposer_matrice(B):
            valeur = sum(
                ligne[i] * colonne[i]
                for i in range(len(ligne))
            )
            nouvelle_ligne.append(valeur)

        resultat.append(nouvelle_ligne)

    return resultat


def resoudre_systeme(A, B):
    n = len(A)

    matrice = [
        A[i][:] + [B[i]]
        for i in range(n)
    ]

    for i in range(n):
        pivot = max(
            range(i, n),
            key=lambda ligne: abs(matrice[ligne][i])
        )

        if abs(matrice[pivot][i]) < 1e-12:
            raise ValueError("Système impossible à résoudre : matrice singulière.")

        matrice[i], matrice[pivot] = matrice[pivot], matrice[i]

        diviseur = matrice[i][i]

        for j in range(i, n + 1):
            matrice[i][j] /= diviseur

        for k in range(n):
            if k != i:
                facteur = matrice[k][i]

                for j in range(i, n + 1):
                    matrice[k][j] -= facteur * matrice[i][j]

    return [matrice[i][n] for i in range(n)]


def entrainer_modele(X, Y):
    if len(X) < len(X[0]):
        raise ValueError(
            "Pas assez de profils distincts pour entraîner le modèle."
        )

    XT = transposer_matrice(X)
    XTX = multiplier_matrices(XT, X)

    coefficients = {}

    for indicateur, valeurs in Y.items():
        Y_colonne = [[valeur] for valeur in valeurs]
        XTY = multiplier_matrices(XT, Y_colonne)

        second_membre = [
            ligne[0] for ligne in XTY
        ]

        coefficients[indicateur] = resoudre_systeme(
            XTX,
            second_membre
        )

    return coefficients


def predire_performances(coefficients, caracteristiques):
    predictions = {}

    for indicateur, valeurs in coefficients.items():
        prediction = sum(
            valeurs[i] * caracteristiques[i]
            for i in range(len(valeurs))
        )

        predictions[indicateur] = prediction

    return predictions
def creer_caracteristiques(frequence, cl, trcd, trp, command_rate):
    return [
        1,
        frequence / 6000,
        cl / 30,
        trcd / 40,
        trp / 40,
        command_rate / 2
    ]