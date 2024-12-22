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

    codes = [x.strip() for x in open(0).readlines()]

    num_pos = {'A':(0,2), '0':(0,1), '1':(1,0), '2':(1,1), '3':(1,2), '4':(2,0), '5':(2,1), '6':(2,2), '7':(3,0), '8':(3,1), '9':(3,2)}
    dir_pos = {'A':(0,2), '^':(0,1), '<':(1,0), 'v':(1,1), '>':(1,2)}

    dir2num = {}
    for f in 'A0123456789':
        for t in 'A0123456789':
            r = num_pos[t][0]-num_pos[f][0]
            c = num_pos[t][1]-num_pos[f][1]
            sr = ''
            sc = ''
            if r < 0:
                sr += 'v'*-r
            elif r > 0:
                sr += '^'*r
            if c < 0:
                sc += '<'*-c
            elif c > 0:
                sc += '>'*c
            dir2num[(f,t)] = []
            if sr and sc:
                if (num_pos[f][0]+r, num_pos[f][1]) != (0,0):
                    dir2num[(f,t)].append(sr+sc+'A')
                if (num_pos[f][0], num_pos[f][1]+c) != (0,0):
                    dir2num[(f,t)].append(sc+sr+'A')
            else:
                dir2num[(f,t)].append(sr+sc+'A')

    num2num = {}
    for f in 'A^<v>':
        for t in 'A^<v>':
            r = dir_pos[t][0]-dir_pos[f][0]
            c = dir_pos[t][1]-dir_pos[f][1]
            sr = ''
            sc = ''
            if r < 0:
                sr += '^'*-r
            elif r > 0:
                sr += 'v'*r
            if c < 0:
                sc += '<'*-c
            elif c > 0:
                sc += '>'*c
            num2num[(f,t)] = []
            if sr and sc:
                if (dir_pos[f][0]+r, dir_pos[f][1]) != (0,0):
                    num2num[(f,t)].append(sr+sc+'A')
                if (dir_pos[f][0], dir_pos[f][1]+c) != (0,0):
                    num2num[(f,t)].append(sc+sr+'A')
            else:
                num2num[(f,t)].append(sr+sc+'A')

    @cache
    def dfs(f,t,steps):
        if steps == 1:
            return len(num2num[(f,t)][0])
        minimum = float('inf')
        for seq in num2num[(f,t)]:
            lenght = 0
            cur = 'A'
            for new in seq:
                lenght += dfs(cur,new,steps-1)
                cur = new
            minimum = min(minimum, lenght)
        return minimum

    ans = [[], []]
    for code in codes:
        cur = 'A'
        s = ['']
        for new in code:
            size = len(s)
            l = dir2num[(cur,new)]
            for j in range(size):
                if len(l) > 1:
                    s.append(s[j]+l[1])
                s[j] += l[0]
            cur = new
        for i, depth in enumerate([2,25]):
            minimum = float('inf')
            for a in s:
                l = 0
                cur = 'A'
                for new in a:
                    l += dfs(cur,new,depth)
                    cur = new
                minimum = min(minimum, l)
            ans[i].append((int(code[:-1])*minimum))

    print('Solution part 1:', sum(ans[0]))
    
    print('Solution part 2:', sum(ans[1]))
