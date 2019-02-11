#!/usr/bin/python

from nltk.corpus import europarl_raw, conll2002
from utilities import n_grams
from collections import Counter
import matplotlib.pyplot as plt
import pickle
import os


def get_corpus(lang):
    if lang == "EN":
        return europarl_raw.english.words()
    elif lang == "FR":
        return europarl_raw.french.words()
    elif lang == "ES":
        return conll2002.words('esp.train')


def data_visualization(data, lang):
    data.sort(key=lambda elem: elem[1], reverse=True)
    x, y = list(), list()
    for d in data:
        x.append(d[0])
        y.append(d[1])
    plt.title("10 most common 3-grams on " + lang)
    plt.xlabel("3-grams")
    plt.ylabel("Occurrences")
    plt.plot(x, y)
    plt.figure(1)
    plt.show()


def main():
    langs = ["EN", "FR", "ES"]
    n = 3
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
                    for gram in n_grams(word, n):
                        grams.append(gram.lower())
            print(">>>>>>>>FINISH processing", l)
            data[l] = grams
            grams = list()
        with open("data-ngrams.obj", "wb") as f:
            pickle.dump(data, f, protocol=pickle.HIGHEST_PROTOCOL)
    top_english = Counter(data["EN"]).most_common(10)
    top_spanish = Counter(data["ES"]).most_common(10)
    top_french = Counter(data["FR"]).most_common(10)
    print("Most common in English", top_english)
    data_visualization(top_english, "English")
    print("Most common in Spanish", top_spanish)
    data_visualization(top_spanish, "Spanish")
    print("Most common in French", top_french)
    data_visualization(top_french, "French")


if __name__ == '__main__':
    main()

