#!/usr/bin/python 
import itertools

# TODO: Falta probar con casos diversos
# TODO: Refactorizar funciones para mejor desempeño


def candidatos_iniciales(base_datos):
    """
    Función que obtiene los candidatos iniciales que serán singletones
    :param base_datos: Datos a ser analizados por el algoritmo
    :return: Lista de singletones que serán los candidatos iniciales
    """
    data = []
    for t in base_datos:
        for item in t:
            if item not in data:
                data.append(item)
    return data


def generador_candidatos(frecuentes, k):
    """
    Función encargada de generar candidatos a ser frecuentes
    :param frecuentes: Elemento frecuentes de la iteración k
    :param k: Iteración k
    :return: Lista de tuplas que serán elementos candidatos a ser frecuentes
    """
    if k == 2:
        data = list(itertools.combinations([c[0] for c in frecuentes], 2))
        return [tuple(sorted(d)) for d in data]
    else:
        data = list()
        for i, frec in enumerate(frecuentes):
            for stem in frec[:k - 2]:
                for j, other in enumerate(frecuentes[i + 1:]):
                    if frozenset([stem]).issubset(set(other)):
                        data.append(tuple(set(frec).union(set(other))))
                        break
        return data


def frecuentes_iniciales(singletones, base_datos, min_sup):
    """
    Obtiene los elementos frecuentes con base en los singletones iniciales de la base
    :param singletones: Candidatos de 1 elemento
    :param base_datos: Base de elemento a ser analizados
    :param min_sup: Soporte mínimo arbitrario
    :return: Lista de singletones frecuentes en la base de datos
    """
    elementos = list()
    for singleton in singletones:
        cuenta = 0
        for t in base_datos:
            if singleton in t:
                cuenta += 1
        if (cuenta / len(base_datos)) >= min_sup:
            elementos.append(tuple([singleton]))
    return elementos


def descartar_candidatos(candidatos, previos_frecuentes, k):
    """
    Función encargada de descartar candidatos frecuentes si alguna combinación de la iteración k - 1 elementos
    no pertenece a los elementos frecuentes previos.
    :param candidatos: Candidatos generados en la iteración k
    :param previos_frecuentes: Elementos frecuentes de la iteración k - 1
    :param k: K en turno
    :return: Lista de tuplas que son los elementos candidatos que cumplen condición de pertenencia
    """
    data = list()
    for candidato in candidatos:
        flag = 0
        combinaciones = list(itertools.combinations(candidato, k - 1))
        for combinacion in combinaciones:
            if tuple(sorted(combinacion)) not in previos_frecuentes:
                flag = 1
                break
        if not flag:
            data.append(candidato)
    return data


def apriori(base_datos, min_sup, min_conf):
    """
    Algoritmo apriori para obtener items frecuentes en una base de datos
    :param base_datos: Datos que serán analizados. Ej: carrito de compras
    :param min_sup: Soporte mínimo
    :param min_conf: Valor mínimo de confianza
    :return: Lista de tuplas con los elementos frecuentes
    """
    candidatos = candidatos_iniciales(base_datos)
    frecuentes = frecuentes_iniciales(candidatos, base_datos, min_sup)
    previos_frecuentes = list()
    k = 2
    while len(frecuentes) != 0:
        c_dict = dict()
        candidatos_k = generador_candidatos(frecuentes, k)
        if k > 2:
            candidatos_k = descartar_candidatos(candidatos_k, frecuentes, k)
        for t in base_datos:
            for c in candidatos_k:
                if frozenset(c).issubset(set(t)):
                    if c not in c_dict.keys():
                        c_dict[c] = 1
                    else:
                        c_dict[c] += 1
        previos_frecuentes += frecuentes[:]
        frecuentes = [relacion for relacion, frecuencia in zip(c_dict.keys(), c_dict.values())
                      if (frecuencia / len(base_datos)) >= min_sup]
        k += 1
    return previos_frecuentes
