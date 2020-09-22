import sys
import calculos
from lectura import generar_diccionario
from simulacion import simular_secuencia

class simbolo():
    pass

def main():
    if len(sys.argv < 2):
        print("Se debe incluir el path al archivo de lectura y la cantidad de símbolos de la secuencia.")
        return
    path = sys.argv[1]
    n = sys.argv[2]
    simbolos = generar_diccionario(path)
    secuencia = simular_secuencia(simbolos, n)
    informacion, entropia = calculos.obtenerDatos(simbolos)
    print("""Cantidad de información presente en la secuencia: {} bits.
    Entropía de la fuente: {} bits.""".format(informacion, entropia))

    

if __name__ == "__main__":
    main()