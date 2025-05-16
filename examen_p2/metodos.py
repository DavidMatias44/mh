import numpy as np
import random
from colorama import init, Fore

init(autoreset=True)

TAM_POBLACION = 400
GENES_LEN = 9
PORCENTAJE_CRUCE = 0.75
PORCENTAJE_MUTACION = 0.009
GENERACIONES = 500

SUDOKU = [
    [8, 0, 6, 0, 0, 0, 1, 0, 7],
    [0, 0, 0, 6, 0, 2, 0, 0, 0],
    [0, 5, 3, 0, 0, 4, 8, 0, 6],
    [7, 0, 4, 8, 0, 0, 6, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0],
    [1, 0, 0, 5, 0, 0, 4, 0, 0],
    [0, 0, 1, 2, 0, 0, 7, 0, 9],
    [2, 0, 0, 0, 9, 6, 0, 0, 0],
    [0, 7, 0, 0, 1, 0, 0, 8, 0]
]

no_cambiar = [[i, j] for i in range(GENES_LEN) for j in range(GENES_LEN) if SUDOKU[i][j] != 0]


def generar_poblacion():
    poblacion = []
    for _ in range(TAM_POBLACION):
        individuo = [fila.copy() for fila in SUDOKU]
        for i in range(GENES_LEN):
            faltan_estos = [num for num in range(1, GENES_LEN + 1) if num not in individuo[i]]
            random.shuffle(faltan_estos)
            for j in range(GENES_LEN):
                if individuo[i][j] == 0:
                    individuo[i][j] = faltan_estos.pop()
        poblacion.append(individuo) 

    return poblacion


def aptitud(individuo):
    colisiones = 0
    
    for fila in individuo:
        colisiones += GENES_LEN - len(set(fila))

    for i in range(GENES_LEN):
        columna = [individuo[j][i] for j in range(GENES_LEN)]
        colisiones += GENES_LEN - len(set(columna))

    for i in range(0, GENES_LEN, 3):
        for j in range(0, GENES_LEN, 3):
            sub_tablero = []
            for k in range(3):
                for l in range(3):
                    sub_tablero.append(individuo[i + k][j + l])
            colisiones += GENES_LEN - len(set(sub_tablero))
        
    return 1 / (1 + colisiones)


def selecciona_progenitores(poblacion, aptitudes):
    total_aptitudes = np.sum(aptitudes)
    probs = [apt / total_aptitudes for apt in aptitudes]
    probs_sum = np.sum(probs)

    elegidos = []
    for _ in range(TAM_POBLACION):
        aux = random.uniform(0, probs_sum)
        suma = 0
        for i, prob in enumerate(probs):
            suma += prob
            if suma >= aux:
                elegidos.append(poblacion[i])
                break
    return elegidos 


def cruza(padre1, padre2):
    hijo = []
    mascara = [random.randint(0, 1) for _ in range(GENES_LEN)] 

    for i in range(GENES_LEN):
        if mascara[i] == 0:
            hijo.append(padre2[i].copy())
        else:
            hijo.append(padre1[i].copy())
    return hijo


def muta(individuo):
    for i in range(GENES_LEN):
        if random.random() < PORCENTAJE_MUTACION:
            estos_si = []
            for j in range(GENES_LEN):
                if SUDOKU[i][j] == 0:
                    estos_si.append(j)

            if len(estos_si) >= 2:
                a, b = random.sample(estos_si, 2)
                individuo[i][a], individuo[i][b] = individuo[i][b], individuo[i][a]
    return individuo


def muestra_resultados(resultado):
    print(Fore.WHITE + "+" + "-" * 23 + "+")
    for i in range(GENES_LEN):
        if i % 3 == 0 and i != 0:
            print(Fore.WHITE + "|" + "-" * 23 + "|")
        fila_str = Fore.WHITE + "| "
        for j in range(GENES_LEN):
            if j % 3 == 0 and j != 0:
                fila_str += Fore.WHITE + "| "
            if SUDOKU[i][j] != 0:
                fila_str += Fore.CYAN + str(resultado[i][j]) + " "
            else:
                fila_str += Fore.WHITE + str(resultado[i][j]) + " "
        fila_str += Fore.WHITE + "|"
        print(fila_str)
    print(Fore.WHITE + "+" + "-" * 23 + "+")


def main():
    poblacion = generar_poblacion()

    for generacion in range(GENERACIONES):
        # poblacion_sorted = poblacion.copy()
        # poblacion_sorted.sort(key=aptitud, reverse=True)
        # mejor = poblacion_sorted[0]
        # print(f"Generación {generacion + 1}:")
        # for fila in mejor:
            # print(f"\t{fila}")
        # print(f"Aptitud: {aptitud(mejor)}\n")

        aptitudes = []
        for individuo in poblacion:
            aptitudes.append(aptitud(individuo))


        if (max(aptitudes) == 1): break
        
        nueva_poblacion = []
        poblacion = selecciona_progenitores(poblacion, aptitudes)
        for i in range(0, TAM_POBLACION, 2):
            padre1, padre2 = poblacion[i], poblacion[i + 1]

            if random.random() < PORCENTAJE_CRUCE:
                hijo1 = cruza(padre1, padre2)
                hijo2 = cruza(padre1, padre2)
            else: 
                hijo1 = padre1
                hijo2 = padre2
                

            hijo1 = muta(hijo1)
            hijo2 = muta(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion[:TAM_POBLACION]
    
    mejor = max(poblacion, key=aptitud)
    print(f"\nMejor solución encontrada:")
    # for fila in mejor:
        # print(f"{fila}") 
    muestra_resultados(mejor)
    print(f"Aptitud: {aptitud(mejor):.3f}") 
    print(f"Errores: {(1 / aptitud(mejor)) - 1}")
    

if __name__ == "__main__":
    main()
