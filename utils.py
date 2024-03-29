import numpy as np


def get_Sigma(cls='nfa'):
    Sigma = set()
    if cls == 'dfa':
        for sigma in range(26):
            Sigma.add(sigma)
    else:
        for sigma in range(26+1):
            Sigma.add(sigma)
    return Sigma, len(Sigma)


def get_sigma(c):
    return ord(c) - ord('a')

def get_char(sigma):
    if sigma != 26:
        return chr(sigma + ord('a'))
    else:
        return 'ε'


def get_epsilon():
    return 26
