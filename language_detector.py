#!/usr/bin/python

from functools import reduce
from utilities import n_grams
from ng_probabilities import most_common_ng
import operator


def to_dict(lista_tuplas):
    result = dict()
    for trigrama, ocurrencias in lista_tuplas:
        result.setdefault(trigrama, ocurrencias)
    return result


def engine(cadena):
    resultados = {}
    n = 3
    distribuciones = most_common_ng(n)
    idiomas = distribuciones.keys()
    for idioma in idiomas:
        peso_relativo = 0
        for palabra in cadena.split():
            if len(palabra) < 3:
                continue
            ng_cadena = n_grams(palabra, n)
            for n_grama in ng_cadena:
                distribuciones_dict = to_dict(distribuciones[idioma])
                if n_grama in distribuciones_dict.keys():
                    peso_relativo += distribuciones_dict[n_grama]
        total_ocurrencias = reduce(lambda x, y: x + y, distribuciones_dict.values())
        resultados[idioma] = peso_relativo / total_ocurrencias
    return max(resultados.items(), key=operator.itemgetter(1))[0]


cadena = "definitivamente estoy convencido de lo que que estoy haciendo en este momento"
print("La cadena '", cadena, "' esta en >>", engine(cadena).upper())
cadena = "i am definitely convinced of what i am doing right now"
print("La cadena '", cadena, "' esta en >>", engine(cadena).upper())
cadena = "je suis definitivement convaincu de ce que je fais en ce moment"
print("La cadena '", cadena, "' esta en >>", engine(cadena).upper())