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
    regs, prog = open(0).read().split('\n\n')
    regs = [reg.strip() for reg in regs.split('\n')]
    A = int(regs[0].split(': ')[1])
    B = int(regs[1].split(': ')[1])
    C = int(regs[2].split(': ')[1])
    program = [int(x) for x in prog.split(': ')[1].split(',')]

    combo = {0:lambda: 0, 1:lambda: 1, 2:lambda: 2, 3:lambda: 3, 4:lambda: A, 5:lambda: B, 6:lambda: C}
    ip = 0
    last_opcode = len(program)
    out = []

    while ip < last_opcode:
        opcode = program[ip]
        operand = program[ip+1]
        ip += 2
        if opcode == 0:
            A = A//(2**combo[operand]())
        elif opcode == 1:
            B = B^operand
        elif opcode == 2:
            B = combo[operand]()%8
        elif opcode == 3:
            if A != 0:
                ip = operand
        elif opcode == 4:
            B = B^C
        elif opcode == 5:
            out.append(combo[operand]()%8)
        elif opcode == 6:
            B = A//(2**combo[operand]())
        elif opcode == 7:
            C = A//(2**combo[operand]())

    print('Solution part 1:', ','.join(map(str,out)))

    def solve(prog, res):
        if prog == []: return res
        for i in range(8):
            a = (res << 3) | i
            b = a%8
            b = b^1
            c = a >> b
            b = b^5
            b = b^c
            if b%8 == prog[-1]:
                rest = solve(prog[:-1], a)
                if rest is None: continue
                return rest

    print('Solution part 2:', solve(program, 0))
