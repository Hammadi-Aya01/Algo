import random

def selection_tournoi(population, fitnesses, taille_tournoi=3):
    indices = random.sample(range(len(population)), taille_tournoi)
    meilleur_idx = max(indices, key=lambda i: fitnesses[i])
    return population[meilleur_idx][:]

def calculer_fitness(individu, matrice_distances):
    distance = calculer_distance_totale(individu, matrice_distances)
    return 1 / distance if distance > 0 else 0

def algorithme_genetique(matrice_distances, taille_population, 
                        nombre_generations, taux_mutation, 
                        taux_croisement, elitisme=True):
    nombre_villes = len(matrice_distances)
    population = creer_population_initiale(taille_population, nombre_villes)
    meilleure_solution = None
    meilleure_distance = float('inf')
    
    for generation in range(nombre_generations):
        fitnesses = [calculer_fitness(ind, matrice_distances) 
                    for ind in population]
        
        nouvelle_population = []
        if elitisme:
            meilleur_idx = max(range(len(population)), 
                             key=lambda i: fitnesses[i])
            nouvelle_population.append(population[meilleur_idx][:])
        
        while len(nouvelle_population) < taille_population:
            parent1 = selection_tournoi(population, fitnesses)
            parent2 = selection_tournoi(population, fitnesses)
            enfant = croisement_pmx(parent1, parent2)
            enfant = mutation_echange(enfant, taux_mutation)
            nouvelle_population.append(enfant)
        
        population = nouvelle_population
    
    return meilleure_solution, meilleure_distance