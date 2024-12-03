from collections import Counter
import re

if __name__ == "__main__":

    line = open(0).read()

    l = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))", line)

    r = 0
    for n in l:
        if n[0] and n[1]:
            r += int(n[0])*int(n[1])

    print('Solution part 1:', r)

    do = True
    r = 0
    for n in l:
        assert n[2] == '' or n[3] == ''
        if n[2]:
            do = True
        elif n[3]:
            do = False
        else:
            if do:
                r += int(n[0])*int(n[1])

    print('Solution part 2:', r)
