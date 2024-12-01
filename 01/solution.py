from collections import Counter

if __name__ == "__main__":

    lines = [tuple(map(int, l.split())) for l in open(0)]
    lists = list(zip(*lines))
    sort = list(map(sorted, lists))
    print('Solution part 1:', sum([abs(t[0]-t[1]) for t in zip(*sort)]))

    count = list(map(Counter, lists))

    r = 0
    for k, v in count[0].items():
        r += k*count[1][k]*v
    print('Solution part 2:', r)
