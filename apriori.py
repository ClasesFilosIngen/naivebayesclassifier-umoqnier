#!/usr/bin/python 
import itertools

T = (("carne", "pollo", "leche"), ("carne", "queso"), ("queso", "botas"),
        ("carne", "pollo", "queso"), ("carne", "pollo", "ropa", "queso", "leche"),
        ("pollo", "ropa", "leche"), ("pollo", "leche", "ropa"))


def get_elementos_candidatos(trans):
    data = []
    for t in trans:
        for item in t:
            if item not in data:
                data.append(item)
    return data


def generador_candidatos(frecuentes, k):
    if k == 2:
        data = list(itertools.combinations(frecuentes, 2))
        return [frozenset(d) for d in data]
    else:
        for frec in frecuentes:
            pass
        return []


def get_elementos_frecuentes(singletones, transiciones, min_sup):
    elementos = list()
    for singleton in singletones:
        cuenta = 0
        for t in transiciones:
            if singleton in t:
                cuenta += 1
        if (cuenta / len(transiciones)) >= min_sup:
            elementos.append(singleton)
    return elementos


def apriori(transiciones, min_sup, min_conf):
    candidatos = get_elementos_candidatos(transiciones)
    frecuentes = get_elementos_frecuentes(candidatos, transiciones, min_sup)
    previos_frecuentes = list()
    k = 2
    while len(frecuentes) != 0:
        c_dict = dict()
        candidatos_k = generador_candidatos(frecuentes, k)
        for t in transiciones:
            for c in candidatos_k:
                if c.issubset(set(t)):
                    if c not in c_dict.keys():
                        c_dict[c] = 1
                    else:
                        c_dict[c] += 1
        previos_frecuentes += frecuentes[:]
        frecuentes = [relacion for relacion, frecuencia in zip(c_dict.keys(), c_dict.values())
                             if (frecuencia / len(transiciones)) >= min_sup]
        print(frecuentes)
        k += 1


apriori(T, 0.3, 0.8)
