import random
import math


NUM_QUEENS = 4
MAX_TABU_LIST_LEN = 3


def get_neighbors(x):
    neighbors = []
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            neighbor = x.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors
    

def get_total_collisions(x):
    colissions = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if abs(i - j) == abs(x[i] - x[j]):
                colissions += 1
    return colissions


def tabu_search(s0):
    best_solution = s0
    best_candidate = s0

    tabu_list = []
    tabu_list.append(s0)

    # TEST
    # stop = True
    i = 1000
    while i > 0:
        neighbors = get_neighbors(best_candidate)
        best_candidate_fitness = math.inf

        for neighbor in neighbors:
            neighbor_fitness = get_total_collisions(neighbor)
            if neighbor not in tabu_list and neighbor_fitness < best_candidate_fitness:
                best_candidate = neighbor
                best_candidate_fitness = neighbor_fitness
        
        if best_candidate_fitness == math.inf: break;

        if best_candidate_fitness < get_total_collisions(best_solution):
            best_solution = best_candidate
            
        tabu_list.append(best_candidate)
        if len(tabu_list) > MAX_TABU_LIST_LEN:
            del tabu_list[0]

        i -= 1

    return best_solution


def main():
    # TODO: implementar un forma de generar una solucion aleatoria xd.
    # a = [4, 3, 2, 1]
    a = [1, 2, 3, 4]

    res = tabu_search(a)
    print(f"Solución: {res} -> colisiones: {get_total_collisions(res)}")


main()