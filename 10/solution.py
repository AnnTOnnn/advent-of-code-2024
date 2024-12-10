from collections import Counter, defaultdict
from operator import add, mul
import re
import heapq

if __name__ == "__main__":

    grid = [list(map(int, l.strip())) for l in open(0).readlines()]

    rows = len(grid)
    cols = len(grid[0])

    def find_score(r, c):
        val = grid[r][c]
        if val == 9:
            return [{(r,c)}, 1]
        score = [set(), 0]
        for dr, dc in [(0,1), (1,0), (0,-1), (-1,0)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and (grid[nr][nc] - val) == 1:
                s, i = find_score(nr, nc)
                score[0] |= s
                score[1] += i
        return score

    scores = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                scores.append(find_score(r,c))

    print('Solution part 1:', sum((len(s[0]) for s in scores)))

    print('Solution part 2:', sum((s[1] for s in scores)))
