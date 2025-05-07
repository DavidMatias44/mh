import numpy as np
import random


TAM_POBLACION = 10
GENES_LEN = 8
PORCENTAJE_CRUCE = 0.7
PORCENTAJE_MUTACION = 0.1
GENERACIONES = 20


def generar_poblacion():
    return [[random.randint(0, 1) for _ in range(GENES_LEN)] for _ in range(TAM_POBLACION)]


def obtener_aptitud(individuo):
    return sum(individuo)


def seleccionar_progenitores(poblacion):
    elegidos = []
    for _ in range(2):
        finalistas = random.sample(poblacion, k=2)
        ganador = max(finalistas, key=obtener_aptitud)
        elegidos.append(ganador)
    return elegidos


def cruzar(padre1, padre2):
    if random.random() < PORCENTAJE_CRUCE:
        punto = random.randint(1, GENES_LEN - 1)
        hijo1 = padre1[:punto] + padre2[punto:]
        hijo2 = padre2[:punto] + padre1[punto:]
        return hijo1, hijo2
    else:
        return padre1.copy(), padre2.copy()


def mutar(individuo):
    for i in range(GENES_LEN):
        if random.random < PORCENTAJE_MUTACION:
            individuo[i] = 1 - individuo[i]
    return individuo


def main():
    poblacion = generar_poblacion()
    for individuo in poblacion:
        print(individuo)


if __name__ == "__main__":
    main()