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
