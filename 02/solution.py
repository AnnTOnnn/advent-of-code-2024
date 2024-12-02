from collections import Counter

def level_safe(l):
    diff = l[1]-l[0]
    for i in range(len(l)-1):
        cur_diff = l[i+1]-l[i]
        if cur_diff == 0 or abs(cur_diff) > 3:
            return 0
        if (diff < 0) != (cur_diff < 0):
            return 0
    return 1

def dampened_level_safe(l):
    for i in range(len(l)):
        dl = l[:i] + l[i+1:]
        if level_safe(dl):
            return 1
    return 0

if __name__ == "__main__":

    levels = [list(map(int, l.split())) for l in open(0)]

    safe = 0
    d_safe = 0
    for l in levels:
        safe += level_safe(l)
        d_safe += dampened_level_safe(l)

    print('Solution part 1:', safe)

    print('Solution part 2:', d_safe)
