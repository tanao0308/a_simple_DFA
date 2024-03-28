import numpy as np


def get_Sigma(cls='nfa'):
    Sigma = set()
    if cls == 'dfa':
        for sigma in range(10):
            Sigma.add(sigma)
    else:
        for sigma in range(11):
            Sigma.add(sigma)
    return Sigma, len(Sigma)


def get_sigma(c):
    return ord(c) - ord('0')


def get_epsilon():
    return 10


if __name__ == "__main__":
    for i in range(5):
        print(i, end=' ')
        i += 1
