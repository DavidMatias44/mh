import numpy as np
import random


FACTOR_AMPLIF = 0.9
CROSSOVER_RATE = 0.2
TOLERANCE = 0.1
NUM_VARS = 9
GENERATIONS = 50
POP_SIZE = 70


def aptitud(a):
    return random.uniform(0, 1)


def differential_evolution(num_of_vars=9, pop_size=70, generations=50, F=0.9, CR=0.2, tol=0.01):
    fitness = np.zeros(pop_size)
    population = np.array(
        [[random.uniform(-1000, 1000) for _ in range(NUM_VARS)] for _ in range(POP_SIZE)]
    )
    
    for h in range(generations):
        for i in range(pop_size):
            target_vector = population[i, :].copy()
            mutant_vector = np.zeros(num_of_vars)
            trial_vector = np.zeros(num_of_vars)

            # MUTACIÓN
            r1, r2, r3 = 0, 0, 0
            while (r1 == r2 or r1 == r3 or r2 == r3 or r1 == i or r2 == i or r3 == i):
                r1 = int(round(random.uniform(0, POP_SIZE-1)))
                r2 = int(round(random.uniform(0, POP_SIZE-1)))
                r3 = int(round(random.uniform(0, POP_SIZE-1)))

            for j in range(num_of_vars):
                mutant_vector[j] = population[r1, 0] + FACTOR_AMPLIF * (population[r2, j] - population[r3, j])

            # CRUCE
            r = [0, 0]
            while len(r) != len(np.unique(r)):
                r = [random.randint(0, NUM_VARS-1) for _ in range(int(np.ceil(CROSSOVER_RATE * NUM_VARS)))]

            trial_vector[r] = mutant_vector[r]
            r = list(set(range(num_of_vars)) - set(r))
            trial_vector[r] = target_vector[r]

            # EVALUACIÓN
            f1 = aptitud(trial_vector)
            f2 = aptitud(target_vector)
            
            # SELECCIÓN
            if f1 < f2:
                population[i, :] = trial_vector
                fitness[i] = f1
            else:
                population[i, :] = target_vector
                fitness[i] = f2
            
        idxs = np.argsort(fitness)
        fitness = fitness[idxs]
        population = population[idxs, :]
        
        print(f"Gen-{h+1}. Cost value is {fitness[0]}")
        
        if fitness[0] < TOLERANCE:
            break
    
    return population[0, :], fitness[0]


if __name__ == "__main__":
    differential_evolution()