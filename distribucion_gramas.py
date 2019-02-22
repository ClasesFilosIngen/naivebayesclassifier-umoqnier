#!/usr/bin/python

from nltk.corpus import europarl_raw, conll2002
from utilities import n_gramas
from collections import Counter
import pickle
import os


def get_corpus(idioma):
    """
    Esta función obtiene el corpus de la biblioteca nltk con base en el idioma seleccionado
    :param idioma: Cadena abreviada que hace referencia el idioma
    :return: Lista de palabras que componen el corpus del idioma selecionado
    """
    if idioma == "EN":
        return europarl_raw.english.words()
    elif idioma == "FR":
        return europarl_raw.french.words()
    elif idioma == "ES":
        return conll2002.words('esp.train')


def data_visualization(data, idioma):
    """
    Esta función dibuja las gráficas de los n-gramas más comúnes de un idioma
    :param data: Diccionario compuesto por {n-grama: número de ocurrencias}
    :param idioma: Cadena del idioma en turno
    :return:
    """
    import matplotlib.pyplot as plt
    data.sort(key=lambda elem: elem[1], reverse=True)
    x, y = list(), list()
    for d in data:
        x.append(d[0])
        y.append(d[1])
    plt.title("10 most common 3-grams on " + idioma)
    plt.xlabel("3-grams")
    plt.ylabel("Occurrences")
    plt.plot(x, y)
    plt.figure(1)
    plt.show()


def trending_gramas(n, total_gramas=10, visualizar=0):
    """
    Función que obtiene los n-gramas más comúnes de algún idioma 
    :param n: Número que será la ene de los n-gramas
    :param total_gramas: Tamaño de la lista de gramas populares a devolver. Default: 10
    :param visualizar: Bandera para visualizar distribuciones. Default: no
    :return: Diccionario compuesto por {idioma: [(grama, ocurrencias), ...]}
    """
    langs = ["EN", "FR", "ES"]
    grams = list()
    data = dict()
    if os.path.isfile("data-ngrams.obj"):
        with open('data-ngrams.obj', 'rb') as f:
            data = pickle.load(f)
    else:
        for l in langs:
            corpus = get_corpus(l)
            print("Processing", len(corpus), "words in >>", l)
            for word in corpus:
                if len(word) >= n:
                    for gram in n_gramas(word, n):
                        grams.append(gram.lower())
            print(">>>>>>>>FINISH processing", l)
            data[l] = grams
            grams = list()
        with open("data-ngrams.obj", "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    top_english = Counter(data["EN"]).most_common(total_gramas)
    top_spanish = Counter(data["ES"]).most_common(total_gramas)
    top_french = Counter(data["FR"]).most_common(total_gramas)
    if visualizar:
        print("Most common 3-grams on English", top_english)
        data_visualization(top_english, "English")
        print("Most common 3-grams on Spanish", top_spanish)
        data_visualization(top_spanish, "Spanish")
        print("Most common 3-grams on French", top_french)
        data_visualization(top_french, "French")
    return {"español": top_spanish, "ingles": top_english, "frances": top_french}

