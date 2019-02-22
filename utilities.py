#!/usr/bin/python


def n_gramas(cadena, n):
    """
    Esta función recibe una cadena y un entero.
    :param cadena: Cadena a procesar.
    :param n: Número entero que es la ene de los n-gramas.
    :return: Lista de n-gramas.
    """
    if len(cadena) <= n:
        return [cadena]
    else:
        return [cadena[i:i+n] for i in range(len(cadena) - n + 1)]
