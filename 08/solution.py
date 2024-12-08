from collections import Counter, defaultdict
from operator import add, mul
import re

if __name__ == "__main__":

    grid = [l.strip() for l in open(0).readlines()]

    rows = len(grid)
    cols = len(grid[0])
    antennas = defaultdict(list)
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                antennas[grid[r][c]].append((r,c))

    def inside(r,c):
        return 0 <= r < rows and 0 <= c < cols

    antinodes = set()
    harmonic_antinodes = set()
    for freq, positions in antennas.items():
        l = len(positions)
        for i in range(l-1):
            for j in range(i+1, l):
                ar, ac = positions[i]
                br, bc = positions[j]
                dr = ar-br
                dc = ac-bc
                if inside(ar+dr, ac+dc):
                    antinodes.add((ar+dr, ac+dc))
                if inside(br-dr, bc-dc):
                    antinodes.add((br-dr, bc-dc))
                while inside(ar,ac):
                    harmonic_antinodes.add((ar, ac))
                    ar += dr
                    ac += dc
                while inside(br,bc):
                    harmonic_antinodes.add((br, bc))
                    br -= dr
                    bc -= dc

    print('Solution part 1:', len(antinodes))

    print('Solution part 2:', len(harmonic_antinodes))
