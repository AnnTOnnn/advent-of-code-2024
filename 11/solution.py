from collections import Counter, defaultdict
from operator import add, mul
from functools import cache
import re
import heapq

if __name__ == "__main__":

    stones = list(map(int, open(0).read().split()))

    @cache
    def blink(stone, steps):
        if steps == 0:
            return 1
        elif stone == 0:
            return blink(1, steps-1)
        elif len(str(stone))%2 == 0:
            num = str(stone)
            left, right = num[:len(num)//2], num[len(num)//2:]
            return blink(int(left), steps-1) + blink(int(right), steps-1)
        else:
            return blink(stone*2024, steps-1)

    print('Solution part 1:', sum((blink(s, 25) for s in stones)))
    print('Solution part 2:', sum((blink(s, 75) for s in stones)))
