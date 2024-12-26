from collections import Counter, defaultdict, deque
from operator import add, mul
from functools import cache
from math import prod
from copy import deepcopy
from random import randint
import numpy as np
import re
import heapq

def print_grid(grid):
    for line in grid:
        print(''.join(line))

if __name__ == "__main__":

    schematics = open(0).read().split('\n\n')

    keys = []
    locks = []

    for s in schematics:
        s = s.strip().splitlines()
        l = []
        if s[0] == '#####': #lock
            for col in zip(*s[1:-1]):
                l.append(Counter(col).get('#', 0))
            locks.append(l)
        else: #key
            for col in zip(*s[1:-1]):
                l.append(Counter(col).get('#', 0))
                
            keys.append(l)

    ans = 0
    for lock in locks:
        for key in keys:
            if all(lock[i] + key[i] <= 5 for i in range(5)):
                ans += 1

    print('Solution part 1:', ans)
    
