from collections import Counter, defaultdict, deque
from operator import add, mul
from functools import cache
from math import prod
from copy import deepcopy
from random import randint
import numpy as np
import re
import heapq

def print_grid(grid):
    for line in grid:
        print(''.join(line))

if __name__ == "__main__":

    vals, ops = open(0).read().split('\n\n')
    m = {x: int(y) for x,y in (val.split(': ') for val in vals.split('\n'))}
    op_map = {}
    for op in ops.strip().split('\n'):
        e, r = op.split(' -> ')
        a,o,b = e.split()
        op_map[r] = (a,o,b)
    m.update(op_map)
    start_map = deepcopy(m)

    def solve(m, key):
        val = m[key]
        if type(val) == int:
            return val
        elif type(val) == tuple:
            a = solve(m, val[0])
            b = solve(m, val[2])
            r = 0
            if val[1] == 'AND':
                r = a & b
            elif val[1] == 'OR':
                r = a | b
            elif val[1] == 'XOR':
                r = a ^ b
            else:
                assert False
            m[key] = r
            return r

    res = sorted([k for k in m if k.startswith('z')], reverse=True)

    binary = ''
    for r in res:
        binary += str(solve(m, r))

    print('Solution part 1:', int(binary,2))

    def simplify(key):
        val = start_map[key]
        if type(val) == int:
            return key
        elif type(val) == tuple:
            a = simplify(val[0])
            b = simplify(val[2])
            return '(' + a + ' ' + val[1] + ' ' + b + ')'

    bits = len(vals.split('\n'))//2
    cur_map = deepcopy(op_map)
    swaps = [('qnw', 'z15'), ('z20', 'cqr'), ('nfj', 'ncd'), ('vkg', 'z37')]
    for a,b in swaps:
        cur_map[a], cur_map[b] = cur_map[b], cur_map[a]
    a = randint(0, (2**bits)-1)
    ab = bin(a)[2:].zfill(bits)
    b = randint(0, (2**bits)-1)
    bb = bin(b)[2:].zfill(bits)
    for i in range(0,bits):
        cur_map[f'x{i:02}'] = int(ab[bits-1-i])
        cur_map[f'y{i:02}'] = int(bb[bits-1-i])
    binary = ''
    for r in res:
        binary += str(solve(cur_map, r))
    diff = bin((a+b) ^ int(binary,2))[2:].zfill(bits+1)
    for i, bit in enumerate(reversed(diff)):
        if int(bit) == 1:
            print(i, diff)
            print(simplify(f'z{i:02}'))
            break
    
    print('Solution part 2:', ','.join(sorted([s for t in swaps for s in t])))
