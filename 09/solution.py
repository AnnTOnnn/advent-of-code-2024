from collections import Counter, defaultdict
from operator import add, mul
import re
import heapq

if __name__ == "__main__":

    diskmap = open(0).read().strip()

    blocks = []
    for i, v in enumerate(diskmap):
        if i%2==0:
            blocks.extend([i//2]*int(v))
        else:
            blocks.extend(list('.'*int(v)))

    i = 0
    j = len(blocks)-1

    while i < j:
        if blocks[j] != '.':
            if blocks[i] == '.':
                blocks[i] = blocks[j]
                blocks[j] = '.'
            else:
                i += 1
        else:
            j -= 1

    ans = 0
    for i, s in enumerate(blocks):
        if s == '.':
            break
        ans += i*s

    print('Solution part 1:', ans)

    holes = {}
    blocks = []

    index = 0
    for i, v in enumerate(list(map(int, diskmap))):
        if v:
            if i%2==0:
                blocks.append([index, v, i//2])
            else:
                if not holes.get(v): holes[v] = []
                holes[v].append(index)
        index += int(v)

    for k in holes:
        heapq.heapify(holes[k])

    compressed_blocks = []

    for index, length, id_number in reversed(blocks):
        new_idxs = []
        for i in range(9,length-1,-1):
            if holes.get(i):
                if holes[i][0] < index:
                    new_idxs.append((holes[i][0], i))
        if new_idxs:
            new_idxs.sort()
            new_index, hole_length = new_idxs[0]
            new_idx = heapq.heappop(holes[hole_length])
            assert new_index == new_idx
            if hole_length != length:
                diff = hole_length - length
                heapq.heappush(holes[diff], new_index+length)
            compressed_blocks.append([new_index, length, id_number])
        else:
            compressed_blocks.append([index, length, id_number])

    ans = 0
    for index, length, id_number in compressed_blocks:
        for i in range(length):
            ans += (index+i)*id_number

    print('Solution part 2:', ans)
