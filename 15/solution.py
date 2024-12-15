from collections import Counter, defaultdict, deque
from operator import add, mul
from functools import cache
from math import prod
from copy import deepcopy
import numpy as np
import re
import heapq

if __name__ == "__main__":

    d = {'^':(-1,0), 'v':(1,0), '<':(0,-1), '>':(0,1)}

    grid, moves = open(0).read().split("\n\n")
    grid = [list(line.strip()) for line in grid.split()]
    moves = moves.replace('\n', '')
    rows = len(grid)
    cols = len(grid[0])
    pos = None
    for r in range(rows):
        for c in range(cols):
            s = grid[r][c]
            if s == '@':
                pos = (r,c)
                break
        else:
            continue
        break

    rep = {'#': '##', 'O': '[]', '.': '..', '@': '@.'}
    wide_grid = [[] for _ in range(rows)]

    for r in range(rows):
        for c in range(cols):
            wide_grid[r].extend(rep[grid[r][c]])

    wide_rows = len(wide_grid)
    wide_cols = len(wide_grid[0])
    wide_pos = None
    for r in range(wide_rows):
        for c in range(wide_cols):
            s = wide_grid[r][c]
            if s == '@':
                wide_pos = (r,c)
                break
        else:
            continue
        break

    for move in moves:
        cr, cc = pos
        steps = 0
        blocked = False
        while True:
            nr, nc = cr+d[move][0], cc+d[move][1]
            if grid[nr][nc] == 'O':
                steps += 1
                cr, cc = nr, nc
            elif grid[nr][nc] == '.':
                steps += 1
                break
            else:
                blocked = True
                break
        if not blocked:
            for i in reversed(range(steps)):
                grid[pos[0]+d[move][0]*(i+1)][pos[1]+d[move][1]*(i+1)] = grid[pos[0]+d[move][0]*i][pos[1]+d[move][1]*i]
            grid[pos[0]][pos[1]] = '.'
            pos = (pos[0]+d[move][0], pos[1]+d[move][1])

    ans = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'O':
                ans += r*100 + c

    print('Solution part 1:', ans)

    for move in moves:
        past_grid = deepcopy(wide_grid)
        cr, cc = wide_pos
        moved = [(cr,cc)]
        moving = deque([(cr,cc)])
        blocked = False
        while moving:
            p = moving.popleft()
            nr, nc = p[0]+d[move][0], p[1]+d[move][1]
            assert (0 <= nr < wide_rows and 0 <= nc < wide_cols)
            if move in ['^', 'v']:
                if wide_grid[nr][nc] == '[':
                    moved.append((nr,nc))
                    moved.append((nr,nc+1))
                    moving.append((nr,nc))
                    moving.append((nr,nc+1))
                elif wide_grid[nr][nc] == ']':
                    moved.append((nr,nc))
                    moved.append((nr,nc-1))
                    moving.append((nr,nc))
                    moving.append((nr,nc-1))
                elif wide_grid[nr][nc] == '#':
                    blocked = True
                    break
            else:
                if (wide_grid[nr][nc] == '[') or (wide_grid[nr][nc] == ']'):
                    moved.append((nr,nc))
                    moving.append((nr,nc))
                elif wide_grid[nr][nc] == '#':
                    blocked = True
                    break

        if not blocked:
            for p in moved:
                wide_grid[p[0]][p[1]] = '.'
            for p in moved:
                wide_grid[p[0]+d[move][0]][p[1]+d[move][1]] = past_grid[p[0]][p[1]]
            wide_pos = (wide_pos[0]+d[move][0], wide_pos[1]+d[move][1])

    ans = 0
    for r in range(wide_rows):
        for c in range(wide_cols):
            if wide_grid[r][c] == '[':
                ans += r*100 + c

    print('Solution part 2:', ans)
