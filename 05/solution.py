from collections import Counter, defaultdict
import re

if __name__ == "__main__":

    rules, updates = open(0).read().split('\n\n')

    pages_before = defaultdict(list)

    rules = [tuple(map(int, rule.split('|'))) for rule in rules.split()]

    def correct_update(pages):
        for rule in rules:
            before = pages.index(rule[0]) if rule[0] in pages else None
            after = pages.index(rule[1]) if rule[1] in pages else None
            if before != None and after != None:
                if after < before:
                    return False
        else:
            return True

    correct_order = []
    incorrect_order = []
    for update in updates.split():
        pages = list(map(int, update.split(',')))
        if correct_update(pages):
            correct_order.append(pages)
        else: incorrect_order.append(pages)

    print('Solution part 1:', sum([update[len(update)//2] for update in correct_order]))

    def compare(pages):
        index = [0 for _ in pages]
        for rule in rules:
            before = pages.index(rule[0]) if rule[0] in pages else None
            after = pages.index(rule[1]) if rule[1] in pages else None
            if before != None and after != None:
                index[after] += 1
        corrected = [0 for _ in pages]
        for i in range(len(pages)):
            corrected[index[i]] = pages[i]
        return corrected

    corrected_order = []
    for update in incorrect_order:
        corrected_order.append(compare(update))

    print('Solution part 2:', sum([update[len(update)//2] for update in corrected_order]))
