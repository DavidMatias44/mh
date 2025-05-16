from metodos import *


def main():
    poblacion = generar_poblacion()

    for generacion in range(GENERACIONES):
        poblacion_sorted = poblacion.copy()
        poblacion_sorted.sort(key=aptitud, reverse=True)
        mejor = poblacion_sorted[0]
        print(f"Generación {generacion + 1}:")
        for fila in mejor:
            print(f"\t{fila}")
        print(f"Aptitud: {aptitud(mejor)}\n")

        aptitudes = []
        for individuo in poblacion:
            aptitudes.append(aptitud(individuo))


        if (max(aptitudes) == 1): break
        
        nueva_poblacion = []
        while len(nueva_poblacion) < TAM_POBLACION:
            padre1, padre2 = selecciona_progenitores(poblacion, aptitudes)

            if random.random() < PORCENTAJE_CRUCE:
                hijo1, hijo2 = cruza(padre1, padre2)
            else: 
                hijo1, hijo2, padre1, padre2

            hijo1 = muta(hijo1)
            hijo2 = muta(hijo2)

            nueva_poblacion.extend([hijo1, hijo2])
        
        poblacion = nueva_poblacion[:TAM_POBLACION]
    
    mejor = max(poblacion, key=aptitud)
    print(f"\nMejor solución encontrada: {mejor} -> Fitness: {aptitud(mejor)}") 
    

if __name__ == "__main__":
    main()