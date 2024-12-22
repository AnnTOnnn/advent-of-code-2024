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

    secrets = list(map(int, open(0).read().splitlines()))

    def mix(s,n):
        return s^n

    def prune(s):
        return s%16777216

    def evolve(s):
        s = mix(s,s*64)
        s = prune(s)
        s = mix(s,s//32)
        s = prune(s)
        s = mix(s,s*2048)
        s = prune(s)
        return s

    new_secrets = []
    seq_tot = defaultdict(int)
    for secret in secrets:
        price_changes = [secret%10]
        for _ in range(2000):
            secret = evolve(secret)
            price_changes.append(secret%10)
        new_secrets.append(secret)
        seen = set()
        for i in range(5, len(price_changes)+1):
            pc = price_changes[i-5:i]
            c = tuple(pc[i+1] - pc[i] for i in range(len(pc)-1))
            if c in seen: continue
            seen.add(c)
            seq_tot[c] += pc[-1]

    print('Solution part 1:', sum(new_secrets))
    
    print('Solution part 2:', max(seq_tot.values()))
