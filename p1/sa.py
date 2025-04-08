import math
import random
import pandas as pd


def objetive_function(x):
    # return 10 * len(x) + sum([(xi**2 - 10 * math.cos(2 * math.pi * xi)) for xi in x])
    res = 0
    for xi in x:
        res += xi**2
    return res


# Definir un vecino a no más de 0.1 de distancia.
def get_neighbor(x, step_size=0.1):
    return [xi + random.uniform(-step_size, step_size) for xi in x]


def sa(x_0, t_max, t_min, max_iter, g):
    x = x_0
    t = t_max

    while t >= t_min:
        i = 0
        while i < max_iter:
            x_p = get_neighbor(x)

            current_eval = objetive_function(x)
            candidate_eval = objetive_function(x_p)
            delta_e = candidate_eval - current_eval

            if delta_e < 0 or random.random() < math.exp(-1 * delta_e / t):
                x = x_p

            i = i + 1

        print(f"Temperatura: {t}, current-> points: {x}, {current_eval}, candidate-> points: {x_p} {candidate_eval}")
        t = g * t

    return x


def main():
    # coords_path = "./dj38.csv"
    # coords = pd.read_csv(coords_path, header=None)
    # print(coords)
    # print(sa([-0.12, 0.12], 100, 0.1, 200, 0.99))

    sa([1, 1], 100, 0.1, 200, 0.99)


main()