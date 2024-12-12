from collections import Counter, defaultdict
from operator import add, mul
from functools import cache
import re
import heapq

if __name__ == "__main__":

    grid = list(line.strip() for line in open(0).readlines())

    rows = len(grid)
    cols = len(grid[0])

    plots = []
    visited = set()

    def find_plot(r, c):
        if (r, c) in visited:
            return set()
        visited.add((r,c))
        spaces = set()
        spaces.add((r,c))
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                if grid[nr][nc] == grid[r][c]:
                    spaces |= find_plot(nr,nc)
        return spaces

    for r in range(rows):
        for c in range(cols):
            if (r,c) in visited: continue
            plots.append(find_plot(r,c))

    ans = 0
    for plot in plots:
        area = len(plot)
        perimeter = 0
        for r, c in plot:
            adjacent = 4
            for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
                nr, nc = r+dr, c+dc
                if (nr,nc) in plot:
                    adjacent -= 1
            perimeter += adjacent
        ans += area*perimeter

    print('Solution part 1:', ans)

    ans = 0
    for plot in plots:
        area = len(plot)
        v_sides = defaultdict(set)
        h_sides = defaultdict(set)
        for r, c in plot:
            for dr in [1,-1]:
                nr = r+dr
                if (nr,c) not in plot:
                    h_sides[(r, nr)].add(c)
            for dc in [1,-1]:
                nc = c+dc
                if (r,nc) not in plot:
                    v_sides[(c, nc)].add(r)
        sides = 0
        for col in v_sides.values():
            side = 1
            col = list(col)
            col.sort()
            for i in range(len(col)-1):
                if col[i+1] - col[i] != 1:
                    side += 1
            sides += side
        for row in h_sides.values():
            side = 1
            row = list(row)
            row.sort()
            for i in range(len(row)-1):
                if row[i+1] - row[i] != 1:
                    side += 1
            sides += side

        ans += area*sides

    print('Solution part 2:', ans)
