#!/usr/bin/python 
import itertools


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


def descartar_candidatos(candidatos, previos_frecuentes, k):
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


def apriori(transiciones, min_sup, min_conf):
    candidatos = get_elementos_candidatos(transiciones)
    frecuentes = get_elementos_frecuentes(candidatos, transiciones, min_sup)
    previos_frecuentes = list()
    k = 2
    while len(frecuentes) != 0:
        c_dict = dict()
        candidatos_k = generador_candidatos(frecuentes, k)
        if k > 2:
            candidatos_k = descartar_candidatos(candidatos_k, frecuentes, k)
        for t in transiciones:
            for c in candidatos_k:
                if frozenset(c).issubset(set(t)):
                    if c not in c_dict.keys():
                        c_dict[c] = 1
                    else:
                        c_dict[c] += 1
        previos_frecuentes += frecuentes[:]
        frecuentes = [relacion for relacion, frecuencia in zip(c_dict.keys(), c_dict.values())
                             if (frecuencia / len(transiciones)) >= min_sup]
        k += 1
    return previos_frecuentes


if __name__ == '__main__':
    carrito = (("carne", "pollo", "leche"), ("carne", "queso"), ("queso", "botas"),
             ("carne", "pollo", "queso"), ("carne", "pollo", "ropa", "queso", "leche"),
             ("pollo", "ropa", "leche"), ("pollo", "leche", "ropa"))
    print("* Carrito de compras *")
    for i, art in enumerate(carrito):
        print("t", i + 1, ":", art)
    items_frecuentes = apriori(carrito, 0.3, 0.8)
    print("* Items frecuentes *")
    for item in items_frecuentes:
        print(item)
