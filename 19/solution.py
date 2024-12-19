from collections import Counter, defaultdict, deque
from operator import add, mul
from functools import cache
from math import prod
from copy import deepcopy
import numpy as np
import re
import heapq

def print_grid(grid):
    for line in grid:
        print(''.join(line))

if __name__ == "__main__":

    towels, patterns = open(0).read().split('\n\n')
    towels = towels.strip().split(', ')
    patterns = patterns.strip().split()

    @cache
    def solve(pat):
        if pat == '':
            return 1
        num = 0
        for towel in towels:
            if pat.startswith(towel):
                num += solve(pat[len(towel):])
        return num

    print('Solution part 1:', sum(bool(solve(p)) for p in patterns))

    print('Solution part 2:', sum(solve(p) for p in patterns))
