from collections import *
from heapq import *
import random
"""
    https://www.1point3acres.com/bbs/thread-523161-1-1.html

    Given a list of users, pair them up

    e.g.
    Input:
    ['Alan', 'Da', 'Jen', 'Kevin', 'Neha', 'Rachel']

    Output:
    [('Alan', 'Kevin'), ('Jen', 'Da'), ('Neha', 'Rachel')]
"""


def shuffle(users):
    # Fisher-Yates Algorithm
    items = users[:]
    for i in range(len(items)):
        j = random.randint(i, len(items)-1)
        items[i], items[j] = items[j], items[i]
    return items


def getRandomPairs(users):
    if len(users) % 2 == 1:
        return []
    pairs = []
    arr = shuffle(users)
    while len(arr) > 0:
        a = arr.pop(0)
        b = arr.pop(0)
        pairs.append([a, b])
    return pairs


a = ['Alan', 'Da', 'Jen', 'Kevin', 'Neha', 'Rachel']
print(getRandomPairs(a))

print("----")

"""
    followup:
    Each person belongs to a dept, dont pair up the people from the same dept

    e.g.
    [
        ('Alan', 'tech'),
        ('Da', 'tech'),
        ('Jen', 'sales'),
        ('Kevin', 'sales',
        ('Neha', 'management'),
        ('Rachel', 'management'),
        ('Calvin', 'tech'),
        ('Stanley', 'management'),
    ]

    Time    O(N^2) there are N items. Getting a list of keys of hashtable take O(N)
    Space   O(N)
"""


def getTeamMatches(users):
    users = shuffle(users)
    ht = defaultdict(list)
    for name, dept in users:
        ht[dept].append(name)

    # consider 'aaabbbcc', sometimes 'aa' or 'bb' will remain and unable to match
    res = []
    while len(ht) >= 2:
        keys = list(ht.keys())
        a = keys[0]
        b = keys[1]
        res.append((ht[a].pop(), ht[b].pop()))
        if len(ht[a]) == 0:
            del ht[a]
        if len(ht[b]) == 0:
            del ht[b]
    return res

    # # it gurantee a match, but a big group would always match with another big group?
    # # case1 NO, consider 'aaabbbcc'
    # # we should match the ab first, then the remain would be 'aabbcc', now they have the same opportunity
    # # case2 YES, consider 'aaabbbwxyz'
    # # we should match the aabb first, then the remain would be 'abwxyz', but a will always match with the b, so this is a downside
    # #
    # # One possible solution is, when there are more than 1 item have the same count as the maxheap[0], suffle the them,
    # # but the downside is it takes longer O(N), and we also need to put the names in an object because heapq sort the 2nd param
    # maxheap = []
    # for key in ht:
    #     heappush(maxheap, (-len(ht[key]), key))
    # res = []
    # while len(maxheap) >= 2:
    #     a, keyA = heappop(maxheap)
    #     b, keyB = heappop(maxheap)
    #     res.append((ht[keyA].pop(), ht[keyB].pop()))
    #     if len(ht[keyA]) == 0:
    #         del ht[keyA]
    #     else:
    #         heappush(maxheap, (a+1, keyA))
    #     if len(ht[keyB]) == 0:
    #         del ht[keyB]
    #     else:
    #         heappush(maxheap, (b+1, keyB))
    # return res


a = [
    ('Alan', 'tech'),
    ('Da', 'tech'),
    ('Calvin', 'tech'),

    ('Jen', 'sales'),
    ('Kevin', 'sales'),

    ('Neha', 'management'),
    ('Rachel', 'management'),
    ('Stanley', 'management')
]
print(getTeamMatches(a))

print("-----")

heap = []
heappush(heap, (0, 'one', 1))
heappush(heap, (1, 'c', 11))
heappush(heap, (1, 'b', 2))
heappush(heap, (1, 'a', 3))
heappush(heap, (1, 'b', 3))
heappush(heap, (1, 'b', 4))
heappush(heap, (1, 'a', 5))
heappush(heap, (1, 'c', 1))

while len(heap) > 0:
    print(heappop(heap))
