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

"""
    Approach

        b l o o m b e r g
    ->  0 1 2 3 4 0 1 2 3
    <-  0 4 3 2 1 0 * * *
        -----------------
        0 1 2 2 1 0 1 2 3 <- result
"""


def shortestDistances(s: str, target: str) -> List[int]:
    n = len(s)
    forward = n * [2**32]
    backward = n * [2**32]
    targetIdx = -1
    for i in range(n):
        if s[i] == target:
            targetIdx = i
        if targetIdx != -1:
            forward[i] = i - targetIdx
    targetIdx = -1
    for i in range(n-1, -1, -1):
        if s[i] == target:
            targetIdx = i
        if targetIdx != -1:
            backward[i] = targetIdx - i
    res = n * [2**32]
    for i in range(n):
        res[i] = min(forward[i], backward[i])
        if res[i] == 2**32:
            res[i] = -1
    return res


a = 'bloomberg'
b = 'b'
print(shortestDistances(a, b))

a = 'bloomberg'
b = 'z'
print(shortestDistances(a, b))
