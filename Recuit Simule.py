import random
import math

def calculer_distance_totale(solution, matrice_distances):
    distance_totale = 0
    for i in range(len(solution) - 1):
        distance_totale += matrice_distances[solution[i]][solution[i + 1]]
    distance_totale += matrice_distances[solution[-1]][solution[0]]
    return distance_totale

def generer_voisin(solution):
    voisin = solution[:]
    i, j = random.sample(range(len(solution)), 2)
    voisin[i], voisin[j] = voisin[j], voisin[i]
    return voisin

def recuit_simule(matrice_distances, temperature_initiale, 
                  temperature_finale, taux_refroidissement, 
                  iterations_par_temperature):
    nombre_villes = len(matrice_distances)
    solution_actuelle = list(range(nombre_villes))
    random.shuffle(solution_actuelle)
    
    meilleure_solution = solution_actuelle[:]
    meilleure_distance = calculer_distance_totale(solution_actuelle, matrice_distances)
    temperature = temperature_initiale
    
    while temperature > temperature_finale:
        for _ in range(iterations_par_temperature):
            solution_voisine = generer_voisin(solution_actuelle)
            distance_voisine = calculer_distance_totale(solution_voisine, matrice_distances)
            
            delta = distance_voisine - distance_actuelle
            if delta < 0 or random.random() < math.exp(-delta / temperature):
                solution_actuelle = solution_voisine
                distance_actuelle = distance_voisine
        
        temperature *= taux_refroidissement
    
    return meilleure_solution, meilleure_distance