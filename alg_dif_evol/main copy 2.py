import numpy as np
import random


FACTOR_AMPLIF = 0.9
CROSSOVER_RATE = 0.2
TOLERANCE = 0
NUM_VARS = 9
GENERATIONS = 200
POP_SIZE = 100

SUDOKU = [
    [8, 0, 6, 0, 0, 0, 1, 0, 7],
    [0, 0, 0, 6, 0, 2, 0, 0, 0],
    [0, 5, 3, 0, 0, 4, 8, 0, 6],
    [7, 0, 4, 8, 0, 0, 6, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [1, 0, 0, 5, 0, 0, 4, 0, 0],
    [0, 0, 1, 2, 0, 0, 7, 0, 9],
    [2, 0, 0, 0, 9, 6, 0, 0, 0],
    [0, 7, 0, 0, 1, 0, 0, 8, 0]
]

def aptitud(individuo):
    colisiones = 0
    individuo = np.round(individuo).astype(int).reshape(9, 9)
    # print(individuo)
    # exit(-1)
    
    for fila in individuo:
        numeros = [num for num in fila]
        # print(numeros)
        # colisiones += NUM_VARS - len(set(fila))
        colisiones += len(numeros) - len(set(numeros))
    # print(colisiones)

    for i in range(NUM_VARS):
        columna = [individuo[j][i] for j in range(NUM_VARS)]
        # print(columna)
        colisiones += len(columna) - len(set(columna))
    # print(colisiones)

    for i in range(0, NUM_VARS, 3):
        for j in range(0, NUM_VARS, 3):
            sub_tablero = []
            for k in range(3):
                for l in range(3):
                    sub_tablero.append(individuo[i + k][j + l])
            numeros = [num for num in sub_tablero]
            colisiones += len(numeros) - len(set(numeros))
    
    # exit(-1)
    return colisiones


def generar_poblacion():
    poblacion = []
    for _ in range(POP_SIZE):
        individuo = [fila.copy() for fila in SUDOKU]
        for i in range(NUM_VARS):
            faltan_estos = [num for num in range(1, NUM_VARS + 1) if num not in individuo[i]]
            random.shuffle(faltan_estos)
            for j in range(NUM_VARS):
                if individuo[i][j] == 0:
                    individuo[i][j] = faltan_estos.pop()
        poblacion.append(individuo) 

    return np.array(poblacion)


def differential_evolution():
    population = generar_poblacion() 
    fitness = np.array([aptitud(individuo) for individuo in population])
    # print(population.shape)
    
    for generacion in range(GENERATIONS):
        for i in range(POP_SIZE):
            target_vector = population[i].copy()
            mutant_vector = np.zeros_like(population[0])
            trial_vector = np.zeros(NUM_VARS)

            # print(target_vector.shape, mutant_vector.shape)

            # MUTACIÓN
            r1, r2, r3 = 0, 0, 0
            while (r1 == r2 or r1 == r3 or r2 == r3 or r1 == i or r2 == i or r3 == i):
                r1 = int(round(random.uniform(0, POP_SIZE-1)))
                r2 = int(round(random.uniform(0, POP_SIZE-1)))
                r3 = int(round(random.uniform(0, POP_SIZE-1)))

            # print(r1, r2, r3)

            # for j in range(NUM_VARS):
            mutant_vector = population[r1] + FACTOR_AMPLIF * (population[r2] - population[r3])
            # print(mutant_vector)

            # CRUCE
            r = [0, 0]
            while len(r) != len(np.unique(r)):
                r = [random.randint(0, NUM_VARS-1) for _ in range(int(np.ceil(CROSSOVER_RATE * NUM_VARS)))]

            # trial_vector = mutant_vector
            r = list(set(range(NUM_VARS)) - set(r))
            trial_vector = target_vector.copy()

            for i in range(NUM_VARS):
                for j in range(NUM_VARS):
                    if SUDOKU[i][j] == 0:
                        if random.random() < CROSSOVER_RATE:
                            trial_vector[i][j] = mutant_vector[i][j]

            # print(trial_vector)
            # print(target_vector)
            # EVALUACIÓN
            f1 = aptitud(trial_vector)
            f2 = aptitud(target_vector)
            # print(f1, f2)
            
            # SELECCIÓN
            if f1 < f2:
                population[i] = trial_vector
                fitness[i] = f1
            else:
                population[i] = target_vector
                fitness[i] = f2
            
        idxs = np.argsort(fitness)
        fitness = fitness[idxs]
        population = population[idxs]
        
        print(f"Generacion: {generacion+1}. Colisiones: {fitness[0]}")
        # best_current = (np.round(population[0]).astype(int) % 8) + 1
        # print(f"Mejor de la generacion: {best_current}")

        
        if fitness[0] <= TOLERANCE:
            break
    
    best_solution = np.round(population[0]).astype(int).reshape(9, 9)
    print(f"Mejor solucion:\n {best_solution}")
    
    # tablero = [[0 for _ in range(NUM_VARS)] for _ in range(NUM_VARS)]
    # for i in range(NUM_VARS):
    #     tablero[best_solution[i] - 1][i] += 1
    # for row in tablero:
    #     print(f"\t{row}")


if __name__ == "__main__":
    differential_evolution()