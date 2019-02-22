#!/usr/bin/python

from functools import reduce
from utilities import n_gramas
from distribucion_gramas import trending_gramas  
import operator
import sys


def to_dict(lista_tuplas):
    result = dict()
    for trigrama, ocurrencias in lista_tuplas:
        result.setdefault(trigrama, ocurrencias)
    return result


def engine(cadena):
    resultados = {}
    n = 3
    distribuciones = trending_gramas(n, 15)
    idiomas = distribuciones.keys()
    for idioma in idiomas:
        peso_relativo = 0
        for palabra in cadena.split():
            if len(palabra) < 3:
                continue
            ng_cadena = n_gramas(palabra, n)
            for n_grama in ng_cadena:
                distribuciones_dict = to_dict(distribuciones[idioma])
                if n_grama in distribuciones_dict.keys():
                    peso_relativo += distribuciones_dict[n_grama]
        total_ocurrencias = reduce(lambda x, y: x + y, distribuciones_dict.values())
        resultados[idioma] = peso_relativo / total_ocurrencias
    return max(resultados.items(), key=operator.itemgetter(1))[0]


def main():
    if len(sys.argv) > 0:
        cadena = sys.argv[0]
        print("La cadena '", cadena, "' esta en >>", engine(cadena).upper(), "<<")
    else:
        print("[ERROR] Se requiere una cadena como argumento del programa.")
        print("$ python detector_idiomas.py <CADENA>")


if __name__ == "__main__":
    main()
