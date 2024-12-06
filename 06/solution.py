from collections import Counter, defaultdict
import re

if __name__ == "__main__":

    lines = [l.strip() for l in open(0).readlines()]

    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    cur_dir = 0
    start_pos = None
    pos = None
    blocked = set()
    visited = set()

    rows = len(lines)
    cols = len(lines[0])

    def inside(row, col):
        return 0 <= row < rows and 0 <= col < cols

    for r, l in enumerate(lines):
        for c, s in enumerate(l):
            if s == '^':
                start_pos = (r, c)
            elif s == '#':
                blocked.add((r,c))

    pos = start_pos
    while inside(*pos):
        visited.add(pos)
        if (pos[0]+dirs[cur_dir][0], pos[1]+dirs[cur_dir][1]) in blocked:
            cur_dir = (cur_dir+1)%len(dirs)
        else:
            pos = (pos[0]+dirs[cur_dir][0], pos[1]+dirs[cur_dir][1])

    print('Solution part 1:', len(visited))

    normal_visited = visited

    loops = []
    for r, c in normal_visited:
        cur_dir = 0
        pos = start_pos
        new_blocked = blocked.copy()
        new_blocked.add((r,c))
        visited = set()
        while inside(*pos):
            new_pd = (*pos, cur_dir)
            if new_pd in visited:
                loops.append((r,c))
                break
            visited.add(new_pd)
            if (pos[0]+dirs[cur_dir][0], pos[1]+dirs[cur_dir][1]) in new_blocked:
                cur_dir = (cur_dir+1)%len(dirs)
            else:
                pos = (pos[0]+dirs[cur_dir][0], pos[1]+dirs[cur_dir][1])

    print('Solution part 2:', len(loops))
