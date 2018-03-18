from math import *
from pprint import pprint
import random
import itertools
from collections import Counter, defaultdict
import sys

def test_minus(narr):
    clicks = 0
    for i, v in enumerate(narr):
        if not v % 2:
            continue
        if i == len(narr) - 1:
            clicks += 1
        else:
            j = len(narr) - i - 2
            clicks += (narr[i + 1] + 1) * 10**j
            narr[i + 1] = 9
    return clicks

def test_plus(narr):
    clicks = 0
    narr = list(reversed(narr))
    for _ in range(2):
        for i, v in enumerate(narr):
            if not v % 2:
                continue
            narr[i] += 1
            for j in range(i, len(narr)):
                if narr[j] == 10:
                    narr[j] = 0
                    if j == len(narr) - 1:
                        narr.append(1)
                    else:
                        narr[j + 1] += 1
            if i == 0:
                clicks += 1
            else:
                clicks += 10** i - int(''.join(str(e) for e in reversed(narr[0:i])))
            for j in range(0, i):
                narr[j] = 0
    return clicks


def run():
    T = int(input())
    for i in range(T):
        N = int(input())
        narr = list(map(int, list(str(N))))
        n = narr[:]
        clicks = test_minus(narr)
        clicks2 = test_plus(n)
        if clicks2 < clicks:
            M = N + clicks2
        else:
            M = N - clicks

        #print(N, M)
        print(f'Case #{i+1}: {min(clicks, clicks2)}')
        # e = 0


if __name__ == '__main__':
    run()
