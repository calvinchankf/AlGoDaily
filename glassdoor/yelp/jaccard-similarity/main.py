from collections import *


"""
    https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=664894&ctid=230591
    https://www.1point3acres.com/bbs/thread-685587-1-1.html

    Calculate the jaccard distance between 2 strings

    e.g.1
    abcd
    xbcdx
    res = 3/5

    e.g.2
    abcdd
    xbcddy
    res = 3/6

    Time    O(S+T)
    Space   O(S+T)
"""


def jaccard(s, t):

    # # approach 1: only the distinct characters
    # # e.g.1 => 3/5
    # # e.g.2 =>
    # A = set([c for c in s])
    # B = set([c for c in t])
    # mutual = A.intersection(B)
    # total = A.union(B)
    # return len(mutual) / len(total)

    # approach 2: len(overlapping) / (S + T - len(overlapping))
    # e.g.1 => 3/6 = 0.5
    # e.g.2 => 4/7 = 0.571...
    A = Counter(s)
    B = Counter(t)
    mutual = 0
    total = len(s) + len(t)
    keys = set(list(A.keys()) + list(B.keys()))
    for key in keys:
        mutual += min(A[key], B[key])
    return mutual / (total - mutual)


a = 'abcd'
b = 'xbcdx'
print(jaccard(a, b))

a = 'abcdd'
b = 'xbcddy'
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
