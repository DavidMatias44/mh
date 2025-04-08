import random
import math


NUM_QUEENS = 7
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


def tabu_search(s0, max_iter=1000):
    best_solution = s0
    best_candidate = s0

    tabu_list = []
    tabu_list.append(s0)

    while max_iter > 0:
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

        max_iter -= 1

    return best_solution


def main():
    a = [7, 6, 5, 4, 3, 2, 1]
    random.shuffle(a)
    print(f"Solución inicial: {a} -> colisiones: {get_total_collisions(a)}")
    
    res = tabu_search(a)
    print(f"Mejor solución:   {res} -> colisiones: {get_total_collisions(res)}")


main()