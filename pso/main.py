import numpy as np
import random


GENERATIONS = 50
POPULATION = 10
PESO = 0.5
C1 = 1.5
C2 = 1.5


def genera_poblacion():
    poblacion = []
    for _ in range(POPULATION):
        poblacion.append(Individuo())
    return poblacion


def aptitud(x):
    return x ** 2 


class Individuo:
    def __init__(self):
        self.posicion = random.uniform(-50, 50)
        self.velocidad = random.uniform(-1, 1)
        self.mejor_pos = self.posicion
        self.mejor_aptitud = aptitud(self.posicion)
    
    def cambiar_velocidad(self, mejor_global):
        r1 = random.random()
        r2 = random.random()
        self.velocidad = PESO * self.velocidad + \
            C1 * r1 * (self.mejor_pos - self.posicion) + \
            C2 * r2 * (mejor_global - self.posicion)

    def cambiar_posicion(self):
        self.posicion += self.velocidad
        nueva_aptitud = aptitud(self.posicion)
        if nueva_aptitud < self.mejor_aptitud:
            self.mejor_aptitud = nueva_aptitud
            self.mejor_pos = self.posicion


if __name__ == "__main__":
    poblacion = genera_poblacion()
    mejor_global = min(poblacion, key=lambda x: x.mejor_aptitud).mejor_pos

    # for individuo in poblacion:
        # print(individuo.posicion)
    
    for generation in range(GENERATIONS):
        for individuo in poblacion:
            individuo.cambiar_velocidad(mejor_global)
            individuo.cambiar_posicion()

        esta_puede_ser = min(poblacion, key=lambda x: x.mejor_aptitud)
        if aptitud(esta_puede_ser.mejor_pos) < aptitud(mejor_global):
            mejor_global = esta_puede_ser.mejor_pos
        
        C1 *= 1.001
        C2 *= 0.999

        print(f"Iteracion {(generation + 1):2}: Mejor: x={mejor_global:.3f}, f(x)={aptitud(mejor_global):.3f}")

        if np.abs(mejor_global) < 0 + 1e-09: break
