from collections import *


"""
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=664894&ctid=230591

    Calculate the jaccard distance between 2 strings(compare to the first string)

    e.g.1
    abcd
    xbcdx
    res = 3/5

    e.g.2
    abcdd
    xbcddx
    res = 3/5

    Time    O(S+T)
    Space   O(S+T)
"""


def jaccard(s, t):
    A = set([c for c in s])
    B = set([c for c in t])

    # A or B
    mutual = A.intersection(B)
    total = A.union(B)
    return len(mutual) / len(total)

    # # compare to S
    # count = 0
    # for key in A:
    #     if key in B:
    #         count += min(A[key], B[key])
    # return count / len(s)


a = 'abcd'
b = 'xbcdx'
print(jaccard(a, b))

a = 'abcdd'
b = 'xbcddx'
print(jaccard(a, b))

print("-----")

"""
    followup: given a list of objects, return the one with the highest jaccard score

    Time    O(N)
    Space   O(1)
"""


class Restaurant:
    def __init__(self, name, rate, address):
        self.name = name
        self.rate = rate
        self.address = address


def highestJaccard(original, objs):
    res = None
    resDist = 0
    for obj in objs:
        dist = jaccard(original, obj.name)
        if res == None or dist > resDist:
            resDist = dist
            res = obj
    return res


a = 'abcd'
b = [
    Restaurant('xbcdx', 100, 'arbitary address'),
    Restaurant('xbcddx', 100, 'arbitary address'),
    Restaurant('xbcddxa', 100, 'arbitary address'),
]
print(highestJaccard(a, b).name)
