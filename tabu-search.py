import random
import math


NUM_QUEENS = 4


def get_neighbor(x):
    res = x.copy()
    index1 = random.randint(0, NUM_QUEENS-1)
    index2 = random.randint(0, NUM_QUEENS-1)

    if index1 != index2:
        res[index1], res[index2] = res[index2], res[index1]
        return res

    return get_neighbor(x)
    

def get_total_collisions():
    pass


def tabu_search(s0):
    best_solution = s0
    best_candidate = s0

    tabu_list = []
    tabu_list.append()
    # while 
    pass


def main():
    a = [1, 2, 3, 4]
    for i in range(NUM_QUEENS):
        for j in range(NUM_QUEENS):
            # if 
            pass



main()