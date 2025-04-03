import pandas as pd
import numpy as np
import math
import random


def objective_function():
    pass


def sa(initial_perm, t_max, t_min, max_iter, cooling_rate):
    current_perm = initial_perm
    current_cost = objective_function(current_perm)
    best_perm = current_perm.copy()
    best_cost = current_cost
    t = t_max

    while t > t_min:
        for _ in range(max_iter):
            candidate_perm = get_neighbor(current_perm)
            candidate_cost = objective_function(candidate_perm)
            
            delta = candidate_cost - current_cost
            if delta < 0 or random.random() < math.exp(-1 * delta / t):
                current_perm = candidate_perm
                current_cost = candidate_cost
                if candidate_cost < best_cost:
                    best_perm = candidate_perm.copy()
                    best_cost = candidate_cost

        t *= cooling_rate
        print(f"Temp: {t:.2f}, Mejor distancia: {best_cost:.2f}")

    return best_perm, best_cost