import numpy as np

# Critères de décision
criteres = ['Portabilité', 'Performance', 'Coût', 'Durabilité']
sous_criteres = {
    'Portabilité': ['Poids', 'Dimensions', 'Autonomie'],
    'Performance': ['CPU', 'RAM', 'GPU', 'Affichage'],
    'Coût': ['Prix', 'Fiabilité', 'Durée de vie'],
    'Durabilité': ['Résistance aux chocs', 'Résistance à l eau', 'Facilité de réparation']
}

# Matrice de comparaison des critères
matrice_criteres = np.array([[1, 2, 4, 3],
                           [1/2, 1, 3, 2],
                           [1/4, 1/3, 1, 1/2],
                           [1/3, 1/2, 2, 1]])


# Normalisation et calcul des poids des critères
poids_criteres = []
for row in matrice_criteres:
    row_sum = sum(row)
    poids_criteres.append(row / row_sum)
poids_criteres = np.array(poids_criteres).T[0]

# Exemple de matrice de comparaison pour le critère "Portabilité"
matrice_portabilite = np.array([[1, 1/3, 2],
                              [3, 1, 4],
                              [1/2, 1/4, 1]])

# Normalisation et calcul des poids pour le critère "Portabilité"
poids_portabilite = []
for row in matrice_portabilite:
    row_sum = sum(row)
    poids_portabilite.append(row / row_sum)
poids_portabilite = np.array(poids_portabilite).T[0]

# Agrégation des scores et résultats
marques = ['Dell', 'HP', 'Lenovo']
scores = []
for marque in marques:
    score_marque = 0
    for i, critere in enumerate(criteres):
        if critere == 'Portabilité':
            score_marque += poids_criteres[i] * poids_portabilite[marques.index(marque)]
        # Ajouter les matrices et les poids pour les autres critères
    scores.append(score_marque)

print("Scores globaux:")
for i, marque in enumerate(marques):
    print(f"{marque}: {scores[i]:.3f}")