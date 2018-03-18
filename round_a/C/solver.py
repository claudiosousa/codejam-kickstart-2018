from math import *
from pprint import pprint
import random
import itertools
from collections import Counter, defaultdict
import sys


def run():
    T = int(input())
    for t in range(T):
        N, K = map(int, input().split())
        nbs = list(map(int, input().split()))

        avg = sum(nbs) / N
        res = avg
        if K > 0:
            nbs_above = list(filter(lambda n: n >= avg, nbs))
            avg_above = sum(nbs_above) / len(nbs_above)
            if N >len(nbs_above):
                nbs_below = list(filter(lambda n: n < avg, nbs))
                avg_below = sum(nbs_below) / (N - len(nbs_above))
                odds_bigger = 1 - (len(nbs_below) / N)**(K + 1)

                res = avg_above * odds_bigger + avg_below * (1 - odds_bigger)
            else:
                res = avg_above
        print(f'Case #{t+1}: {res}')


if __name__ == '__main__':
    run()
