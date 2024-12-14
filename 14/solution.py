from collections import Counter, defaultdict
from operator import add, mul
from functools import cache
from math import prod
import numpy as np
import re
import heapq

if __name__ == "__main__":

    guards = list(l.strip() for l in open(0).readlines())
    num = re.compile(r"-?\d+")

    rows = 103
    cols = 101
    steps = 100
    mid_row = (rows-1)/2
    mid_col = (cols-1)/2

    def solve(steps):
        ans = [0 for _ in range(4)]
        for guard in guards:
            vals = list(map(int, num.findall(guard)))
            r = vals[1]
            c = vals[0]
            dr = vals[3]
            dc = vals[2]
            nr = (r + dr*steps)%rows
            nc = (c + dc*steps)%cols
            if nr < mid_row and nc < mid_col:
                ans[0] += 1
            elif nr > mid_row and nc < mid_col:
                ans[1] += 1
            elif nr > mid_row and nc > mid_col:
                ans[2] += 1
            elif nr < mid_row and nc > mid_col:
                ans[3] += 1
        return ans

    print('Solution part 1:', prod(solve(100)))

    min_product = float("inf")
    min_step = None
    for i in range(1,rows*cols):
        p = prod(solve(i))
        if p < min_product:
            min_product = p
            min_step = i

    print('Solution part 2:', min_step)
