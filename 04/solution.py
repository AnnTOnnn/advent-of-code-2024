from collections import Counter
import re

dirs= [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]
word = 'XMAS'
xdirs= [(1,1),(-1,1),(-1,-1),(1,-1)]
xword = 'MAS'

if __name__ == "__main__":

    grid = [list(l.strip()) for l in open(0).readlines()]

    rows = len(grid)
    cols = len(grid[0])

    def in_grid(l):
        for r, c in l:
            if r < 0 or r >= rows:
                return False
            if c < 0 or c >= cols:
                return False
        return True

    ans = 0

    for r in range(rows):
        for c in range(cols):
            for d in dirs:
                pos = []
                for i, s in enumerate(word):
                    pos.append((r+i*d[0], c+i*d[1]))
                if in_grid(pos):
                    for i, s in enumerate(word):
                        if grid[pos[i][0]][pos[i][1]] != s:
                            break
                    else:
                        ans += 1

    print('Solution part 1:', ans)

    ans = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'A':
                for i in range(len(xdirs)):
                    fd = xdirs[i]
                    sd = xdirs[(i+1)%len(xdirs)]
                    fpos = [(r-fd[0], c-fd[1]), (r, c), (r+fd[0], c+fd[1])]
                    spos = [(r-sd[0], c-sd[1]), (r, c), (r+sd[0], c+sd[1])]
                    if in_grid(fpos+spos):
                        for i, s in enumerate(xword):
                            if grid[fpos[i][0]][fpos[i][1]] != s or grid[spos[i][0]][spos[i][1]] != s:
                                break
                        else:
                            ans += 1

    print('Solution part 2:', ans)
