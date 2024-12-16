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

    grid = [list(line.strip()) for line in open(0).readlines()]

    rows = len(grid)
    cols = len(grid[0])
    start_pos = (rows-2, 1)
    start_dir = (0, 1)
    end_pos = (1, cols-2)

    que = [(0, *start_pos, *start_dir)]
    seen = set()

    while que:
        cost, r, c, dr, dc = heapq.heappop(que)
        seen.add((r,c,dr,dc))
        if (r,c) == end_pos:
            print('Solution part 1:', cost)
            break
        for ncost, nr, nc, ndr, ndc in [(cost+1, r+dr, c+dc, dr, dc), (cost+1000, r, c, dc, -dr), (cost+1000, r, c, -dc, dr)]:
            if grid[nr][nc] == '#': continue
            if (nr, nc, ndr, ndc) in seen: continue
            heapq.heappush(que, (ncost, nr, nc, ndr, ndc))

    que = [(0, *start_pos, *start_dir)]
    min_cost = defaultdict(lambda: float('inf'))
    min_cost[(*start_pos, *start_dir)] = 0
    backtrack = defaultdict(list)
    min_tot_cost = float('inf')
    end_states = set()

    while que:
        cost, r, c, dr, dc = heapq.heappop(que)
        if cost > min_cost[(r, c, dr, dc)]: continue
        if (r,c) == end_pos:
            if cost > min_tot_cost: break
            min_tot_cost = cost
            end_states.add((r, c, dr, dc))
        for ncost, nr, nc, ndr, ndc in [(cost+1, r+dr, c+dc, dr, dc), (cost+1000, r, c, dc, -dr), (cost+1000, r, c, -dc, dr)]:
            if grid[nr][nc] == '#': continue
            if ncost > min_cost[(nr, nc, ndr, ndc)]: continue
            if ncost < min_cost[(nr, nc, ndr, ndc)]:
                backtrack[(nr, nc, ndr, ndc)] = set()
                min_cost[(nr, nc, ndr, ndc)] = ncost
            backtrack[(nr, nc, ndr, ndc)].add((r,c,dr,dc))
            heapq.heappush(que, (ncost, nr, nc, ndr, ndc))

    pos = deque(end_states)
    visited = set(end_states)

    while pos:
        p = pos.popleft()
        for l in backtrack[p]:
            if l in visited: continue
            visited.add(l)
            pos.append(l)

    print('Solution part 2:', len(set(((r,c) for r,c,_,_ in visited))))
