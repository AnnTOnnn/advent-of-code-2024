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

    connections = open(0).read().splitlines()
    con_map = defaultdict(list)

    for c in connections:
        a,b = c.split('-')
        con_map[a].append(b)
        con_map[b].append(a)

    threes = set()
    seen = set()
    for k,v in con_map.items():
        for one in v:
            if one in seen: continue
            for two in con_map[one]:
                if two in seen: continue
                for three in con_map[two]:
                    if three in seen: continue
                    if k == three and (k.startswith('t') or one.startswith('t') or two.startswith('t')):
                        threes.add(tuple(sorted([k,one,two])))
        seen.add(k)

    print('Solution part 1:', len(threes))

    sets = set()

    def find_set(cur, included):
        s = tuple(sorted(included))
        if s in sets: return
        sets.add(s)
        for new in con_map[cur]:
            if new in included: continue
            if all(new in con_map[i] for i in included):
                find_set(new, included | {new})

    for c in con_map:
        find_set(c,{c})
    
    print('Solution part 2:', ','.join(max(sets, key=len)))
