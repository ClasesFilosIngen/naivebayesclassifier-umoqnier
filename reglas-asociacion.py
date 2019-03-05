#!/usr/bin/python

import itertools
from apriori import apriori, generador_candidatos
from utilities import contador_ocurrencias

# TODO: Revisar a detalle función ap_gen_rules


class Regla:
    def __init__(self, base, implicacion, apoyo, confianza):
        self.base = base
        self.implicacion = implicacion
        self.apoyo = apoyo
        self.confianza = confianza

    def __str__(self):
        return str(self.base) + ' -> ' + ', '.join(self.implicacion) + ' || Conf> ' + str(self.confianza) + ' Apoyo> ' + str(self.apoyo)


carrito = (("carne", "pollo", "leche"), ("carne", "queso"), ("queso", "botas"),
         ("carne", "pollo", "queso"), ("carne", "pollo", "ropa", "queso", "leche"),
         ("pollo", "ropa", "leche"), ("pollo", "leche", "ropa"))


def calcula_confianza(base, regla_base, regla_gen):
    cuenta_base = contador_ocurrencias(base, regla_base)
    cuenta_gen = contador_ocurrencias(base, regla_gen)
    return cuenta_gen / cuenta_base


def calcula_soporte(base, regla_gen):
    cuenta = contador_ocurrencias(base, regla_gen)
    return cuenta / len(base)


def ap_gen_rules(base, regla, hipotesis, k, m, min_conf, apoyo):
    if k > m+1 and len(hipotesis) != 0:
        if len(hipotesis[0]) == 1:
            hipotesis_siguiente = [tuple([s[0] for s in hipotesis])]
        for h in hipotesis_siguiente:
            confianza = contador_ocurrencias(base, regla) / contador_ocurrencias(base, set(regla) - set([h]))
            if confianza >= min_conf:
                r = Regla(tuple(set(regla) - set(h)), h, apoyo, confianza)
                print(r)
                del r
            else:
                print("Del -->", h)
                continue
        ap_gen_rules(base, regla, hipotesis_siguiente, len(hipotesis_siguiente), m+1, min_conf, apoyo)


def reglas_un_item_consecuente(base, regla, min_conf, apoyo, base_len):
    data = []
    reglas_base = list(itertools.combinations(regla, base_len))
    for r_base in reglas_base:
        confianza = calcula_confianza(base, r_base, regla)
        if confianza >= min_conf:
            r = Regla(','.join(r_base), tuple(set(regla) - set(r_base)), calcula_soporte(base, regla), confianza)
            print(r)
            RULES.append(r)
            data.append(tuple(set(regla) - set(r_base)))
    return data


def generador_reglas(base, reglas, min_conf, apoyo):
    for regla in reglas:
        k = len(regla)
        if k >= 2:
            reglas_un_item = reglas_un_item_consecuente(base, regla, min_conf, apoyo, len(regla) - 1)
            m = 1
            h1 = reglas_un_item
            ap_gen_rules(base, regla, h1, len(regla), m, min_conf, apoyo)


def main():
    min_sup = 0.3
    min_conf = 0.8
    items_frecuentes = apriori(carrito, min_sup)
    generador_reglas(carrito, items_frecuentes, min_conf, min_sup)

    
if __name__ == '__main__':
    main()
