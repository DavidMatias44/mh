import random
import math

# vector de pesos y de valores de cada objeto.
weights = [100, 155, 50, 112, 70, 80, 60, 118, 110, 55]
values = [100, 100, 80, 40, 160, 10, 100, 55, 88, 1]

# se inicializa el vector solución.
n = len(weights)
x = [0 for _ in range(n)]

# hay un peso limite
MAX_WEIGHT = 700


def get_total_weight(x, w):
    weight_obtained = 0
    for (xi, wi) in zip(x, w):
        weight_obtained += xi * wi
    return weight_obtained


def get_total_profit(x, v):
    profit_obtained = 0
    for (xi, vi) in zip(x, v):
        profit_obtained += xi * vi
    return profit_obtained


def generate_initial_sol(x, w):
    # Colocar unos en el vector solución tal que maximice v*x.
    for i in range(n):
        x[i] = 1

        w_obtained = get_total_weight(x, w)
        if w_obtained > MAX_WEIGHT:
            x[i] = 0
            w_obtained = get_total_weight(x, w)
            break

    return w_obtained


def get_neighbor():
    # tengo que permutar un 1 y un 0 (?).
    i, j = random.sample(0, n)
    pass


def simulated_annealing(initial_perm, t_max=150, t_min=0.001, max_iter=600, cooling_rate=0.995):
    current_perm = initial_perm.copy()
    current_cost = get_total_profit(current_perm)
    best_perm, best_cost = current_perm[:], current_cost
    t = t_max
    
    while t > t_min:
        for _ in range(max_iter):
            candidate_perm = get_neighbor(current_perm[:])
            candidate_cost = get_total_profit(candidate_perm)
            delta = candidate_cost - current_cost
            
            if delta < 0 or random.random() < math.exp(-delta / t):
                current_perm, current_cost = candidate_perm[:], candidate_cost
                if current_cost < best_cost:
                    best_perm, best_cost = current_perm[:], current_cost
        
        t *= cooling_rate
    
    return best_perm, best_cost


def main():
    print(generate_initial_sol(x, weights))
    print(get_total_profit(x, values))
    print(x)

    simulated_annealing(x)

main()