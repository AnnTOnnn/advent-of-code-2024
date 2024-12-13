from collections import Counter, defaultdict
from operator import add, mul
from functools import cache
import numpy as np
import re
import heapq

if __name__ == "__main__":

    systems = open(0).read().strip().split('\n\n')
    nums = re.compile(r"(\d+)\D+(\d+)")

    ans = [0,0]
    for system in systems:
        lines = system.split('\n')
        x = [list(map(int, [m[1], m[2]])) for m in (nums.search(line) for line in lines)]
        left = np.array(np.transpose([x[0],x[1]]))
        for i, addition in enumerate([0, 10000000000000]):
            right = np.array([v+addition for v in x[2]])
            res = np.linalg.inv(left).dot(right)
            a = round(res[0],3)
            b = round(res[1],3)
            if a.is_integer() and b.is_integer():
                ans[i] += 3*int(a) + int(b)

    print('Solution part 1:', ans[0])

    print('Solution part 2:', ans[1])
