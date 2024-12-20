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
    start_pos = None
    end_pos = None

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start_pos = (r,c)
            elif grid[r][c] == 'E':
                end_pos = (r,c)

    pico = {}
    r, c = start_pos
    pico[(r,c)] = 0

    while (r,c) != end_pos:
        for nr,nc in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
            if not (0 <= nr < rows and 0 <= nc < cols): continue
            if grid[nr][nc] == '#': continue
            if pico.get((nr,nc)) != None: continue
            pico[(nr,nc)] = pico[(r,c)] + 1
            r,c = nr,nc

    shorter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#': continue
            for nr, nc in [(r+2, c), (r+1,c+1), (r,c+2), (r-1,c+1)]:
                if not (0 <= nr < rows and 0 <= nc < cols): continue
                if grid[nr][nc] == '#': continue
                if abs(pico[(r,c)] - pico[(nr,nc)]) >= 102:
                    shorter += 1
    
    print('Solution part 1:', shorter)

    shorter = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '#': continue
            for rad in range(2,21):
                for dr in range(rad+1):
                    dc = rad-dr
                    for nr, nc in {(r+dr, c+dc), (r+dr,c-dc), (r-dr,c+dc), (r-dr,c-dc)}:
                        if not (0 <= nr < rows and 0 <= nc < cols): continue
                        if grid[nr][nc] == '#': continue
                        if pico[(r,c)] - pico[(nr,nc)] >= 100+rad:
                            shorter += 1
    
    print('Solution part 2:', shorter)
