import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


coords_path = "./dj38.csv"
coords = pd.read_csv(coords_path, header=None).values
num_cities = coords.shape[0]
distance_matrix = [[0] * num_cities for _ in range(num_cities)]

for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            dx = coords[i][0] - coords[j][0]
            dy = coords[i][1] - coords[j][1]
            distance_matrix[i][j] = math.sqrt(dx**2 + dy**2)


def objective_function(permutation):
    total_distance = 0
    for i in range(num_cities):
        from_city = permutation[i]
        to_city = permutation[(i + 1) % num_cities]
        total_distance += distance_matrix[from_city][to_city]
    return total_distance


def get_neighbor(current_perm):
    new_perm = current_perm.copy()
    i, j = random.sample(range(num_cities), 2)
    new_perm[i], new_perm[j] = new_perm[j], new_perm[i]  # Intercambiar dos ciudades
    return new_perm


def sa(initial_perm, t_max, t_min, max_iter, cooling_rate):
    current_perm = initial_perm # esto tiene los nodos en orden
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


def print_nodes(best_perm):
    pass
    # 

def main():
    initial_perm = list(range(num_cities))
    random.shuffle(initial_perm)

    perms_len = len(initial_perm)
    for index in range(perms_len):
        if index != perms_len - 1:
            print(f"From: {index}->{initial_perm[index]} to: {index + 1}->{initial_perm[index+1]}")

            x, y = coords[initial_perm[index]]
            plt.scatter(x, y)

            x1, y1 = coords[initial_perm[index+1]]
            plt.plot([x, y], [x1, y1], c=np.random.rand(3,))

        # print(coords[elem])
        # current = coords[elem] 
        # prev = current # xd

        # x, y = current
        # plt.scatter(x, y)
        # print(f"Coordenadas: {coords_path[elem]}")

    plt.show()

    # best_route, best_distance = sa(
    #     initial_perm=initial_perm,
    #     t_max=100,
    #     t_min=0.1,
    #     max_iter=300,
    #     cooling_rate=0.99
    # )

    # print("\nMejor ruta encontrada:", best_route)
    # print("Distancia total:", best_distance)


if __name__ == "__main__":
    # main()

    x = [1, 2, 3]
    y = [1, 4, 9]

    for xi, yi in zip(x, y):
        # print(xi, yi)
        plt.scatter(xi, yi)
    # pass
    plt.plot(xi, yi, c='red')
    plt.show()

# current -> punto inicial.
# next    -> punto destino (dibujar una raya).
# repetir: ahora next es current.