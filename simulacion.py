from random import random

def simular_secuencia(simbolos, n):
    """En base a la longitud n de la secuencia, generar la misma en base
    a las probabilidades de cada símbolo"""

    secuencia = ""

    for i in range(n):
        sumaIntervalo = 0
        numeroAletorio = random()
        for simbolo in simbolos.keys():
            sumaIntervalo += simbolos[simbolo]
            if (sumaIntervalo >= numeroAletorio): # de darse la condición, el numero aleatorio queda dentro del intervalo del símbolo
                secuencia += simbolo
                break
    
    return secuencia