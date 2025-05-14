import numpy as np
import random


TAM_POBLACION = 50
GENES_LEN = 8
PORCENTAJE_CRUCE = 0.7
PORCENTAJE_MUTACION = 0.2
GENERACIONES = 100

NUM_REINAS = 8
TABLERO = [[0 for _ in range(NUM_REINAS)] for _ in range(NUM_REINAS)]


def generar_poblacion():
    return [random.sample(range(1, NUM_REINAS + 1), NUM_REINAS) for _ in range(TAM_POBLACION)]


def aptitud(individuo):
    colisiones = 0
    for i in range(NUM_REINAS):
        for j in range(i + 1, NUM_REINAS):
            if (individuo[i] == individuo[j]) or (abs(i - j) == abs(individuo[i] - individuo[j])):
                colisiones += 1
    return 1 / (1 + colisiones)


def obtener_poblacion_cada_elemento_tiene_probabilidades_diferentes(poblacion, aptitudes):
    total_aptitudes = np.sum(aptitudes)
    probs = aptitudes / total_aptitudes 

    indices = np.random.choice(TAM_POBLACION, size=TAM_POBLACION, replace=True, p=probs)

    res = []
    for i in indices:
        res.append(poblacion[i])

    return res


def selecciona_progenitores(poblacion, aptitudes):
    total_aptitudes = np.sum(aptitudes)
    probs = aptitudes / total_aptitudes 

    indices = np.random.choice(TAM_POBLACION, size=TAM_POBLACION, replace=True, p=probs)

    escoge_de_aqui = []
    for i in indices:
        escoge_de_aqui.append(poblacion[i])

    i, j = random.sample(range(TAM_POBLACION), 2)
    return escoge_de_aqui[i], escoge_de_aqui[j]


def cruza(padre1, padre2):
    hijo1 = padre1.copy()
    hijo2 = padre2.copy()

    mascara = [random.random() < 0.5 for _ in range(GENES_LEN)]

    intercambios1 = {}
    intercambios2 = {}
    for i in range(NUM_REINAS):
        if mascara[i]:
            intercambios1[padre2[i]] = padre1[i]
            intercambios2[padre1[i]] = padre2[i]
    
    for i in range(NUM_REINAS):
        if mascara[i]:
            hijo1[i] = padre2[i]
            hijo2[i] = padre1[i]
        else:
            if hijo1[i] in intercambios1:
                hijo1[i] = intercambios1[hijo1[i]]
            if hijo2[i] in intercambios2:
                hijo2[i] = intercambios2[hijo2[i]]
    
    return hijo1, hijo2


def muta(individuo):
    if random.random() < PORCENTAJE_MUTACION:
        i, j = random.sample(range(NUM_REINAS), 2)
        individuo[i], individuo[j] = individuo[j], individuo[i]
    return individuo


def main():
    poblacion = generar_poblacion()

    for generacion in range(GENERACIONES):
        poblacion_sorted = poblacion.copy()
        poblacion_sorted.sort(key=aptitud, reverse=True)
        mejor = poblacion_sorted[0]
        print(f"Generación {generacion + 1}:\n \t{mejor} -> Aptitud: {aptitud(mejor)}\n")

        aptitudes = []
        for individuo in poblacion:
            aptitudes.append(aptitud(individuo))


        if (max(aptitudes) == 1): break
        
        nueva_poblacion = []
        while len(nueva_poblacion) < TAM_POBLACION:
            padre1, padre2 = selecciona_progenitores(poblacion, aptitudes)
            hijo1, hijo2 = cruza(padre1, padre2)

            hijo1 = muta(hijo1)
            hijo2 = muta(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion[:TAM_POBLACION]
    
    mejor = max(poblacion, key=aptitud)
    print(f"\nMejor solución encontrada: {mejor} -> Fitness: {aptitud(mejor)}") 

    for i in range(NUM_REINAS):
        TABLERO[mejor[i] - 1][i] += 1
    
    for row in TABLERO:
        print(row)


if __name__ == "__main__":
    main()
