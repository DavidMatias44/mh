import random
import math


NUM_QUEENS = 7
# MAX_TABU_LIST_LEN = 20
MAX_TABU_LIST_LEN = 5
FRECUENCY_TABLE = [[0 for _ in range(NUM_QUEENS)] for _ in range(NUM_QUEENS)]


def get_neighbors(x):
    neighbors = []
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            neighbor = x.copy()
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors
    

def get_total_collisions(x):
    collisions = 0
    for i in range(NUM_QUEENS):
        for j in range(i + 1, NUM_QUEENS):
            if abs(i - j) == abs(x[i] - x[j]):
                collisions += 1
    return collisions


def get_diff_indexes(x, y):
    res = []
    for i in range(NUM_QUEENS):
        if x[i] != y[i]:
            res.append(i)
        if len(res) == 2: break
    return res


def tabu_search(s0, max_iter=8):
    best_solution = s0
    best_candidate = s0

    tabu_list = []
    tabu_list.append(s0)

    # aux = best_candidate.copy()
    while max_iter > 0:
        i = 0
        neighbors = get_neighbors(best_candidate)
        best_candidate_fitness = math.inf

        for neighbor in neighbors:
            neighbor_fitness = get_total_collisions(neighbor)
            if neighbor not in tabu_list and neighbor_fitness < best_candidate_fitness:
                best_candidate = neighbor
                best_candidate_fitness = neighbor_fitness

                # print(tabu_list)
                # print("======== SWAP ========")
                # print(f"Ant: {tabu_list[-1]}")
                # print(f"Act: {best_candidate}")
                # i, j = get_diff_indexes(tabu_list[-1], best_candidate)
                # print(f"Cambio: {i} <---> {j}")

                # for i_ in range(NUM_QUEENS):
                    # for j_ in range(NUM_QUEENS):
                        # if FRECUENCY_TABLE[i_][j_] != 0:
                            # FRECUENCY_TABLE[i_][j_] -= 1

                # FRECUENCY_TABLE[i][j] += MAX_TABU_LIST_LEN

        
        # for i in range(NUM_QUEENS):
            # print(FRECUENCY_TABLE[i])
        # print()
        
        if best_candidate_fitness == math.inf: break;

        if best_candidate_fitness < get_total_collisions(best_solution):
            best_solution = best_candidate


            
        tabu_list.append(best_candidate)
        if len(tabu_list) > MAX_TABU_LIST_LEN:
            del tabu_list[0]

        max_iter -= 1

    return best_solution


def main():
    a = [4, 5, 3, 6, 7, 1, 2]
    random.shuffle(a)
    print(f"Solución inicial: {a} -> colisiones: {get_total_collisions(a)}")
    
    res = tabu_search(a)
    print(f"Mejor solución:   {res} -> colisiones: {get_total_collisions(res)}")

    for i in range(NUM_QUEENS):
        FRECUENCY_TABLE[i][res[i] - 1] += 1
    
    for row in FRECUENCY_TABLE:
        print(row)

main()
