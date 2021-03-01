from collections import *
from heapq import *

"""
    https://www.1point3acres.com/bbs/thread-500537-1-1.html

    Given a list of positive comments, return the top K receivers who receive the most comments

    Input:
    comments = [
        Comment("X", "A", "great"),
        Comment("X", "A", "great1"),
        Comment("X", "A", "great2"), 

        Comment("X", "B", "great3"), 
        Comment("Y", "B", "great4"), 
        Comment("Z", "B", "great5"), 
        
        Comment("X", "C", "great5"), 
        Comment("Y", "C", "great5")
    ]
    K = 2
    Ouput:
    ['A', 'B']

    followup: no duplicate sender
    Ouput: ['B', 'C']
"""


class Comment:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message


def topKReceivers(comments, K):
    ht = defaultdict(set)
    for c in comments:
        sender = c.sender
        receiver = c.receiver
        ht[receiver].add(sender)

    # minheap: O(NlogK, KlogK)
    # minheap = []
    # for receiver in ht:
    #     uniqueSenders = ht[receiver]
    #     heappush(minheap, (len(uniqueSenders), receiver))
    #     if len(minheap) > K:
    #         heappop(minheap)
    # res = []
    # while len(minheap) > 0:
    #     count, receiver = heappop(minheap)
    #     res.append(receiver)
    # return res[::-1]

    # or sort: O(NlogN + K)
    freqs = []
    for receiver in ht:
        uniqueSenders = ht[receiver]
        freqs.append([receiver, len(uniqueSenders)])
    freqs.sort(key=lambda x: -x[1])
    res = []
    for receiver, count in freqs:
        res.append(receiver)
        if len(res) == K:
            break
    return res


a = [
    Comment("X", "A", "great"),
    Comment("X", "A", "great1"),
    Comment("X", "A", "great2"),

    Comment("X", "B", "great3"),
    Comment("Y", "B", "great4"),
    Comment("Z", "B", "great5"),

    Comment("X", "C", "great5"),
    Comment("Y", "C", "great5")
]
b = 2
print(topKReceivers(a, b))

print("-----")

"""
    https://www.1point3acres.com/bbs/thread-718420-1-1.html
    
    another followup: every person can only leave 2 comments at most

    Input:
    comments = [
        Comment("X", "A", "great"),
        Comment("X", "A", "great1"),
        Comment("X", "A", "great2"), 

        Comment("X", "B", "great3"), 
        Comment("Y", "B", "great4"), 
        Comment("Z", "B", "great5"), 
        
        Comment("X", "C", "great5"), 
        Comment("Y", "C", "great5")
    ]
    K = 2
    Limit = 2
    Ouput:
    ['B', 'A']

    Explanation
    X->A    2

    X->B    1
    Y->B    1
    Z->B    1

    X->C    1
    Y->C    1
"""


def topKReceivers(comments, K, L):
    counter = Counter()
    rateLimiting = Counter()
    for c in comments:
        sender = c.sender
        receiver = c.receiver
        key = (sender, receiver)
        if rateLimiting[key] < L:
            rateLimiting[key] += 1
            counter[receiver] += 1

    print(rateLimiting)
    print(counter)

    # minheap: O(NlogK, KlogK)
    # minheap = []
    # for receiver in ht:
    #     uniqueSenders = ht[receiver]
    #     heappush(minheap, (len(uniqueSenders), receiver))
    #     if len(minheap) > K:
    #         heappop(minheap)
    # res = []
    # while len(minheap) > 0:
    #     count, receiver = heappop(minheap)
    #     res.append(receiver)
    # return res[::-1]

    # or sort: O(NlogN + K)
    freqs = []
    for receiver in counter:
        uniqueSenders = counter[receiver]
        freqs.append([receiver, uniqueSenders])
    freqs.sort(key=lambda x: -x[1])
    res = []
    for receiver, count in freqs:
        res.append(receiver)
        if len(res) == K:
            break
    return res


a = [
    Comment("X", "A", "great"),
    Comment("X", "A", "great1"),
    Comment("X", "A", "great2"),

    Comment("X", "B", "great3"),
    Comment("Y", "B", "great4"),
    Comment("Z", "B", "great5"),

    Comment("X", "C", "great5"),
    Comment("Y", "C", "great5")
]
b = 2
c = 2
print(topKReceivers(a, b, c))
