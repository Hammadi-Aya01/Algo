import random
from collections import deque

def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]
    return distance_totale

def generer_voisinage(solution):
    voisins = []
    n = len(solution)
    for i in range(n - 1):
        for j in range(i + 1, n):
            voisin = solution[:]
            voisin[i], voisin[j] = voisin[j], voisin[i]
            voisins.append((voisin, (i, j)))
    return voisins

def recherche_tabou(matrice_distances, taille_liste_tabou, 
                    nombre_iterations, taille_voisinage_max=50):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)
    
    meilleure_solution = solution_actuelle[:]
    meilleure_distance = calculer_distance_totale(solution_actuelle, matrice_distances)
    liste_tabou = deque(maxlen=taille_liste_tabou)
    
    for iteration in range(nombre_iterations):
        voisins = generer_voisinage(solution_actuelle)
        if len(voisins) > taille_voisinage_max:
            voisins = random.sample(voisins, taille_voisinage_max)
        
        # Sélection du meilleur voisin non-tabou
        # avec critère d'aspiration...
    
    return meilleure_solution, meilleure_distance