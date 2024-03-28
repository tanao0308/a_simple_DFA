import numpy as np


def get_sigma(c):
    print(c, ord(c) - ord('0'))
    return ord(c) - ord('0')


def get_epsilon():
    return 10


if __name__ == "__main__":
    for i in range(5):
        print(i, end=' ')
        i += 1
