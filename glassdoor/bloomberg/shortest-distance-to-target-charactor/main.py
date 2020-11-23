from typing import *

"""
    lets say u r give a string and a character, find the shortest index distance from every character to the target character

    e.g.
    s = 'bloomberg', target = 'b'

    result = [0, 1, 2, 2, 1, 0, 1, 2, 3]

    Explanation:
    
    b l o o m b e r g
    0 1 2 2 1 0 1 2 3
      < < > >   < < <

    Assume the input only allows lowercase letters
"""


def shortestDistances(s: str, target: str) -> List[int]:
    n = len(s)
    forward = {}
    backward = {}
    targetCharIdx = -1
    for i in range(n):
        c = s[i]
        if c == target:
            targetCharIdx = i
        elif targetCharIdx > -1 and c not in forward:
            forward[c] = i - targetCharIdx
    targetCharIdx = -1
    for i in range(n-1, -1, -1):
        c = s[i]
        if c == target:
            targetCharIdx = i
        elif targetCharIdx > -1 and c not in backward:
            backward[c] = targetCharIdx - i
    res = n * [-1]
    for i in range(n):
        c = s[i]
        if c == target:
            res[i] = 0
        else:
            if c in forward and c in backward:
                res[i] = min(forward[c], backward[c])
            elif c in forward:
                res[i] = forward[c]
            elif c in backward:
                res[i] = backward[c]
    return res


a = 'bloomberg'
b = 'b'
print(shortestDistances(a, b))

a = 'bloomberg'
b = 'z'
print(shortestDistances(a, b))
