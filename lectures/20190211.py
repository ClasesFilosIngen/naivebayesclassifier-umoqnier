#!/usr/bin/python
import this  # Zen of python
# Clase de pre-procesamiento


def n_gramador(cadena, n):
    if len(cadena) <= n:
        return [cadena]
    else:
        return [cadena[:n]] + n_gramador(cadena[1:], n)


def n_gramador2(cadena, n):
    if len(cadena) <= n:
        return [cadena]
    else:
        gramas = []
        for i in range(len(cadena) - (n - 1)):
            gramas.append(cadena[i:i+n])
        return gramas


print(n_gramador("esto es una cadena medio larga para ver una cosa".split(), 2))  # Lo errores no deben pasar explicitamente
