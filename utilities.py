#!/usr/bin/python


def n_grams(word, n):
    """This funtion get a word and a integer for n. Return a list of n-grams"""
    if n <= len(word):
        return [word[i:i+n] for i in range(len(word) - n + 1)]
    else:
        print("[WARNING] n should be <= that length of the word")
        return word

