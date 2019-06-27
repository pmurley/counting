#!/usr/bin/python3

import itertools

MINIMUM_N = 3
MAXIMUM_N = 10


def satisfies_condition(l):
    maxnum = None
    minnum = None

    for elem in l:
        e = int(elem)

        if maxnum is None:
            maxnum = e
        if minnum is None:
            minnum = e

        if e > maxnum:
            maxnum = e

        if e < minnum:
            minnum = e

        if e > minnum and e < maxnum:
            return False

    return True


n = MINIMUM_N

while(n <= MAXIMUM_N):
    all_possibilities = itertools.permutations(range(1,n+1))

    success = 0
    failure = 0
    successes = []
    for possibility in all_possibilities:
        if satisfies_condition(possibility):
            success += 1
            successes.append(possibility)
        else:
            failure += 1


    print('n: %d' % n)
    print('Number that satisfy condition: %d' % success)
    print()
    n += 1

print('-----------------------')
print('Cassie is the greatest.')
print('-----------------------')

