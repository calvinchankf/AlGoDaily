from collections import *

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

    followup:no duplicate sender
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
