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

    size = 71
    steps = 1024
    coords = [tuple(map(int, l.strip().split(','))) for l in open(0).readlines()]

    def bfs(n):
        blocking = coords[:n]

        q = deque([(0,0,0)])
        seen = {(0,0)}

        while q:
            r, c, cost = q.popleft()
            for nr, nc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
                if not (0 <= nr < size and 0 <= nc < size): continue
                if (nr,nc) in blocking: continue
                if (nr,nc) in seen: continue
                if (nr,nc) == (size-1,size-1): return cost+1
                seen.add((nr,nc))
                q.append((nr,nc,cost+1))
        return False

    print('Solution part 1:', bfs(steps))

    lo = 0
    hi = len(coords)

    while lo < hi:
        mid = (lo+hi)//2
        if bfs(mid+1):
            lo = mid+1
        else:
            hi = mid

    print('Solution part 2:', ','.join(list(map(str,coords[lo]))))
