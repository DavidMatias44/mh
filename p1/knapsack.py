import random
import math


# vector de pesos y de valores de cada objeto.
WEIGHTS = [100, 155, 50, 112,  70, 80,  60, 118, 110, 55]
VALUES  = [100, 100, 80,  40, 160, 10, 100,  55,  88,  1]

NUM_ELEMS = len(WEIGHTS)

# hay un peso limite
MAX_WEIGHT = 700


# calcular el peso total que genera el vector.
def get_total_weight(x):
    weight_obtained = 0
    for (xi, wi) in zip(x, WEIGHTS):
        weight_obtained += xi * wi
    return weight_obtained


# calcular el beneficio total que genera el vector.
def get_total_profit(x):
    profit_obtained = 0
    for (xi, vi) in zip(x, VALUES):
        profit_obtained += xi * vi
    return profit_obtained


# crear una solucion inicial.
def generate_initial_solution():
    x = [0] * NUM_ELEMS
    remaining_weight = MAX_WEIGHT
    
    for index in range(NUM_ELEMS):
        if WEIGHTS[index] <= remaining_weight:
            x[index] = 1
            remaining_weight -= WEIGHTS[index]

    return x 


# cambiar en el vector un 1 por un 0 o viceversa, de manera aleatoria.
def get_neighbor(x):
    neighbor = x.copy()
    index = random.randint(0, NUM_ELEMS-1)

    neighbor[index] = 0 if neighbor[index] else 1

    if get_total_weight(neighbor) > MAX_WEIGHT:
        return get_neighbor(x)

    return neighbor


def simulated_annealing(initial_solution, t_max=50, t_min=0.1, max_iter=100, cooling_rate=0.9):
    current_solution = initial_solution.copy()
    current_profit = -get_total_profit(current_solution)

    best_solution, best_profit = current_solution, current_profit
    t = t_max
    
    while t > t_min:
        for i in range(max_iter):
            candidate_solution = get_neighbor(current_solution)
            candidate_profit = -get_total_profit(candidate_solution)
            delta = candidate_profit - current_profit
            
            if delta < 0 or random.random() < math.exp(-delta / t):
                current_solution, current_profit = candidate_solution, candidate_profit
                if current_profit < best_profit:
                    best_solution, best_profit = current_solution, current_profit

                    print("===================== NUEVA ========================")
                    print(f"Nueva solución: {best_solution}")
                    print(f"Nuevo profit: {-best_profit}\n")
                    
               
        t *= cooling_rate
    
    return best_solution


def main():
    x = generate_initial_solution()
    print("\n===================== INICIAL ======================")
    print(f"Solución incial: {x}")
    print(f"Costo de solución incial: {get_total_weight(x)}")
    print(f"Beneficio de solución incial: {get_total_profit(x)}")


    print()
    x = simulated_annealing(x)
    print("===================== MEJOR ========================")
    print(f"Mejor solución: {x}")
    # print(VALUES)
    print(f"Costo de mejor solución: {get_total_weight(x)}")
    print(f"Beneficio de mejor solución: {get_total_profit(x)}\n")


main()