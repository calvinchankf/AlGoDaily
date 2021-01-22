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

    ???
"""
