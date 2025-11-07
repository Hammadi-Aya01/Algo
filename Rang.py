import random

def selection_rang(population, fitnesses):
    indices_fitness = [(i, f) for i, f in enumerate(fitnesses)]
    indices_fitness.sort(key=lambda x: x[1])
    
    rangs = {}
    for rang, (idx, _) in enumerate(indices_fitness, start=1):
        rangs[idx] = rang
    
    somme_rangs = sum(rangs.values())
    probabilites_cumulatives = []
    cumul = 0
    for i in range(len(population)):
        cumul += rangs[i] / somme_rangs
        probabilites_cumulatives.append(cumul)
    
    r = random.random()
    for i, prob_cumul in enumerate(probabilites_cumulatives):
        if r <= prob_cumul:
            return population[i][:]
    return population[-1][:]

def croisement_pmx(parent1, parent2):
    taille = len(parent1)
    point1, point2 = sorted(random.sample(range(taille), 2))
    enfant = [-1] * taille
    enfant[point1:point2] = parent1[point1:point2]
    
    mapping = {}
    for i in range(point1, point2):
        mapping[parent1[i]] = parent2[i]
    
    for i in list(range(point1)) + list(range(point2, taille)):
        candidat = parent2[i]
        while candidat in enfant:
            candidat = mapping.get(candidat, candidat)
            if candidat not in mapping:
                break
        enfant[i] = candidat
    return enfant