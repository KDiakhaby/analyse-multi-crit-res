# Analyse Hiérarchique des Processus (AHP)

## Critères de Décision et Facteurs Associés

1. **Portabilité/Confort de Mobilité/Poids de l'ordinateur**

2. **Performance/Processeur (CPU)**
  
3. **Coût (Prix et Fiabilité)/Prix d'achat initial**
  
4. **Durabilité/Résistance aux chocs et aux chutes**

## Matrices de Comparaison Pair-à-Pair et Calcul des Poids

### Matrice de Comparaison des Critères

|         | Portabilité | Performance | Coût | Durabilité |
|---------|-------------|-------------|------|------------|
| Portabilité | 1 | 2 | 4 | 3 |
| Performance | 1/2 | 1 | 3 | 2 |
| Coût | 1/4 | 1/3 | 1 | 1/2 |
| Durabilité | 1/3 | 1/2 | 2 | 1 |

#### Calcul de la somme de chaque ligne :
- Ligne Portabilité : 1 + 2 + 4 + 3 = 10
- Ligne Performance : 1/2 + 1 + 3 + 2 = 6.5
- Ligne Coût : 1/4 + 1/3 + 1 + 1/2 = 2.083
- Ligne Durabilité : 1/3 + 1/2 + 2 + 1 = 3.833

#### Normalisation des valeurs :
- Portabilité : 1/10, 2/10, 4/10, 3/10
- Performance : 1/6.5, 1/6.5, 3/6.5, 2/6.5
- Coût : 1/2.083, 1/3.083, 1/2.083, 1/2.083
- Durabilité : 1/3.833, 1/3.833, 2/3.833, 1/3.833

#### Poids des critères :
- Portabilité : 0.429
- Performance : 0.286
- Coût : 0.107
- Durabilité : 0.179

### Matrice pour le Critère "Portabilité"

|         | Dell | HP | Lenovo |
|---------|------|----|--------|
| Dell    | 1    | 1/3| 2      |
| HP      | 3    | 1  | 4      |
| Lenovo  | 1/2  | 1/4| 1      |

#### Normalisation et Poids pour la "Portabilité"
- Dell: 0.2
- HP: 0.6
- Lenovo: 0.2

### Matrice de Comparaison pour le critère "Performance"

|         | Dell | HP | Lenovo |
|---------|------|----|--------|
| Dell    | 1    | 1/4| 2      |
| HP      | 4    | 1  | 3      |
| Lenovo  | 1/2  | 1/3| 1      |

#### Normalisation et poids pour "Performance"
- Dell : 0.2
- HP : 0.6
- Lenovo : 0.2

### Matrice de Comparaison pour le critère "Coût"

|         | Dell | HP | Lenovo |
|---------|------|----|--------|
| Dell    | 1    | 2  | 1/2    |
| HP      | 1/2  | 1  | 1/3    |
| Lenovo  | 2    | 3  | 1      |

#### Normalisation et poids pour "Coût"
- Dell : 0.3
- HP : 0.2
- Lenovo : 0.5

### Matrice de Comparaison pour le critère "Durabilité"

|         | Dell | HP | Lenovo |
|---------|------|----|--------|
| Dell    | 1    | 1/2| 2      |
| HP      | 2    | 1  | 3      |
| Lenovo  | 1/2  | 1/3| 1      |

#### Normalisation et poids pour "Durabilité"
- Dell : 0.2
- HP : 0.6
- Lenovo : 0.2

## Agrégation des Scores et Résultats

les scores globaux sont pour déterminer la marque la plus adaptée :

- HP: Score Global = 0.425
- Lenovo: Score Global = 0.275
- Dell: Score Global = 0.300
