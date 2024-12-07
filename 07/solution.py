from collections import Counter, defaultdict
from operator import add, mul
import re

if __name__ == "__main__":

    lines = [l.strip() for l in open(0).readlines()]

    data ={}
    for line in lines:
        value, numbers = line.split(': ')
        numbers = list(map(int, numbers.split()))
        data[int(value)] = numbers

    def solve(tgt, cur, rest, ops):
        if not rest:
            return cur == tgt
        for op in ops:
            res = solve(tgt, op(cur, rest[0]), rest[1:], ops)
            if res:
                return res
        return False

    for i, ops in enumerate([[mul, add], [mul, add, (lambda x, y: int(str(x)+str(y)))]]):
        ans = 0
        for k, v in data.items():
            if solve(k, v[0], v[1:], ops):
                ans += k

        print(f'Solution part {i+1}:', ans)
