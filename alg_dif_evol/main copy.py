import numpy as np
import random


FACTOR_AMPLIF = 0.9
CROSSOVER_RATE = 0.2
TOLERANCE = 0
NUM_VARS = 8
GENERATIONS = 200
POP_SIZE = 100


def aptitud(solution):
    solution = np.round(solution).astype(int) % NUM_VARS
    
    colisiones = 0
    for i in range(NUM_VARS):
        for j in range(i + 1, NUM_VARS):
            if solution[i] == solution[j] or abs(i - j) == abs(solution[i] - solution[j]):
                colisiones += 1
    return colisiones 


def differential_evolution():
    fitness = np.zeros(POP_SIZE)
    population = np.random.uniform(0, 8, size=(POP_SIZE, NUM_VARS))
    
    for generacion in range(GENERATIONS):
        for i in range(POP_SIZE):
            target_vector = population[i, :].copy()
            mutant_vector = np.zeros(NUM_VARS)
            trial_vector = np.zeros(NUM_VARS)

            # MUTACIÓN
            r1, r2, r3 = 0, 0, 0
            while (r1 == r2 or r1 == r3 or r2 == r3 or r1 == i or r2 == i or r3 == i):
                r1 = int(round(random.uniform(0, POP_SIZE-1)))
                r2 = int(round(random.uniform(0, POP_SIZE-1)))
                r3 = int(round(random.uniform(0, POP_SIZE-1)))

            for j in range(NUM_VARS):
                mutant_vector[j] = population[r1, 0] + FACTOR_AMPLIF * (population[r2, j] - population[r3, j])

            # CRUCE
            r = [0, 0]
            while len(r) != len(np.unique(r)):
                r = [random.randint(0, NUM_VARS-1) for _ in range(int(np.ceil(CROSSOVER_RATE * NUM_VARS)))]

            trial_vector[r] = mutant_vector[r]
            r = list(set(range(NUM_VARS)) - set(r))
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
        
        print(f"Generacion: {generacion+1}. Colisiones: {fitness[0]}")
        # best_current = (np.round(population[0]).astype(int) % 8) + 1
        # print(f"Mejor de la generacion: {best_current}")

        
        if fitness[0] <= TOLERANCE:
            break
    
    best_solution = (np.round(population[0]).astype(int) % 8) + 1
    print(f"Mejor solucion: {best_solution}")
    
    tablero = [[0 for _ in range(NUM_VARS)] for _ in range(NUM_VARS)]
    for i in range(NUM_VARS):
        tablero[best_solution[i] - 1][i] += 1
    for row in tablero:
        print(f"\t{row}")


if __name__ == "__main__":
    differential_evolution()