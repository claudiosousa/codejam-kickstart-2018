from math import *
from pprint import pprint
import random
import itertools
from collections import Counter, defaultdict
import sys


def run():
    T = int(input())
    for t in range(T):
        L = int(input())
        Larr = input().split()
        words = Counter((l[0], *sorted(l[1:-1]), l[-1]) for l in Larr)

        # lasts = {}
        # words_indexed = {}
        # for w in words:
        #     if w[0] not in words_indexed:
        #         words_indexed[w[0]] = defaultdict(set)
        #     words_indexed[w[0]][len(w)].add(w[-1])
        S1, S2, N, A, B, C, D = input().split()
        N, A, B, C, D = map(int, [N, A, B, C, D])

        Narr = [S1, S2]
        s1 = ord(S1)
        s2 = ord(S2)
        for i in range(2, N):
            s3 = (A * s2 + B * s1 + C) % D
            Narr.append(chr(s3 % 26 + 97))
            s1, s2 = s2, s3

        found = 0
        for w in words:
            for i, c in enumerate(Narr):
                if c == w[0] and len(Narr) >= i + len(w) and w[-1] == Narr[i + len(w) - 1]:
                    sortedw = (w[0], *sorted(Narr[i + 1:i + len(w) - 1]), w[-1])
                    if sortedw == w:
                        found += words[w]
                        break

        print(f'Case #{t+1}: {found}')


if __name__ == '__main__':
    run()
