import numpy as np
import pandas as pd
import random
import math
import matplotlib.pyplot as plt
import networkx as nx

from scipy.spatial import distance_matrix


# Cargar coordenadas y calcular matriz de distancias
coords = pd.read_csv("./dj38.csv", header=None).values
num_cities = len(coords)
distance_matrix = distance_matrix(coords, coords)


def objective_function(permutation):
    idx = np.append(permutation, permutation[0])  # Cierra el ciclo del recorrido
    return np.sum(distance_matrix[idx[:-1], idx[1:]])


def get_neighbor(permutation):
    i, j = np.random.choice(num_cities, 2, replace=False)
    permutation[i], permutation[j] = permutation[j], permutation[i]
    return permutation


def simulated_annealing(initial_perm, t_max=150, t_min=0.001, max_iter=600, cooling_rate=0.995):
    """Ejecuta el algoritmo de Recocido Simulado con optimización en iteraciones y tasa de enfriamiento."""
    current_perm = initial_perm.copy()
    current_cost = objective_function(current_perm)
    best_perm, best_cost = current_perm[:], current_cost
    t = t_max
    
    while t > t_min:
        for _ in range(max_iter):
            candidate_perm = get_neighbor(current_perm[:])
            candidate_cost = objective_function(candidate_perm)
            delta = candidate_cost - current_cost
            
            if delta < 0 or random.random() < math.exp(-delta / t):
                current_perm, current_cost = candidate_perm[:], candidate_cost
                if current_cost < best_cost:
                    best_perm, best_cost = current_perm[:], current_cost
        
        t *= cooling_rate  # Reducir temperatura
    
    return best_perm, best_cost

def plot_graphs(coords, best_route):
    """Visualiza los puntos iniciales y la mejor ruta en una sola figura."""
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    
    # Grafo de puntos iniciales
    axes[0].scatter(coords[:, 0], coords[:, 1], c='red', label='Ciudades')
    for i, (x, y) in enumerate(coords):
        axes[0].text(x, y, str(i), fontsize=9, ha='right')
    axes[0].set_title("Ciudades Iniciales")
    axes[0].legend()
    
    # Grafo de la mejor ruta
    G = nx.Graph()
    for i, (x, y) in enumerate(coords):
        G.add_node(i, pos=(x, y))
    for i in range(len(best_route)):
        G.add_edge(best_route[i], best_route[(i + 1) % len(best_route)])
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, with_labels=True, node_color='red', edge_color='blue', node_size=200, font_size=10, ax=axes[1])
    axes[1].set_title("Mejor Ruta Encontrada")
    
    plt.show()
    

def main():
    initial_perm = np.random.permutation(num_cities).tolist()
    
    best_route, best_distance = simulated_annealing(initial_perm)
    
    print("\n Mejor ruta encontrada:", best_route)
    print("\n Distancia total:", best_distance)
    
    plot_graphs(coords, best_route)


if __name__ == "__main__":
    main()
