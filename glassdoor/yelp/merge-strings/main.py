"""
    https://www.1point3acres.com/bbs/thread-542585-1-1.html

    Given two strings, merge them
    
    e.g.
    abc + bcd = abcd

    Note: the head of T must be in the middle of S
    So there wont be S = abcd, T = xbcy
"""


def mergeStrings(S, T):
    res = ''
    i, j = 0, 0
    while i < len(S) and j < len(T):
        if S[i] == T[j]:
            res += S[i]
            i += 1
            j += 1
        elif S[i] != T[j]:
            res += S[i]
            i += 1
        else:
            res += T[j]
            j += 1
    res += T[j:]
    return res


a = 'abc'
b = 'bcd'
print(mergeStrings(a, b))
