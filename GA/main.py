import numpy as np
import random


TAM_POBLACION = 10
GENES_LEN = 8
PORCENTAJE_CRUCE = 0.7
PORCENTAJE_MUTACION = 0.1
GENERACIONES = 50

NUM_REINAS = 8


def generar_poblacion():
    # return [[random.randint(0, 1) for _ in range(GENES_LEN)] for _ in range(TAM_POBLACION)]
    return [random.sample(range(1, NUM_REINAS + 1), NUM_REINAS) for _ in range(TAM_POBLACION)]


def obtener_aptitud(individuo):
    # esto varia dependiendo del problema, modificar para los problemas a tratar.
    # return sum(individuo) / len(individuo)

    colisiones = 0
    for i in range(NUM_REINAS):
        for j in range(i + 1, NUM_REINAS):
            if abs(i - j) == abs(individuo[i] - individuo[j]):
                colisiones += 1
    return (28 - colisiones) / 28


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
    # for i in range(GENES_LEN):
        # if random.random() < PORCENTAJE_MUTACION:
            # individuo[i] = 1 - individuo[i]
    # return individuo

    if random.random() < PORCENTAJE_MUTACION:
        i, j = random.sample(range(NUM_REINAS), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo


def main():
    poblacion = generar_poblacion()
    for generacion in range(GENERACIONES):
        poblacion.sort(key=obtener_aptitud, reverse=True)
        mejor = poblacion[0]
        print(f"Gen {generacion + 1}: {mejor} -> Fitness: {obtener_aptitud(mejor)}")
        
        nueva_poblacion = []
        while len(nueva_poblacion) < TAM_POBLACION:
            padre1, padre2 = seleccionar_progenitores(poblacion)
            hijo1, hijo2 = cruzar(padre1, padre2)

            hijo1 = mutar(hijo1)
            hijo2 = mutar(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion[:TAM_POBLACION]
    
    # Resultado final
    mejor = max(poblacion, key=obtener_aptitud)
    print(f"\nMejor solución encontrada: {mejor} -> Fitness: {obtener_aptitud(mejor)}") 


if __name__ == "__main__":
    main()