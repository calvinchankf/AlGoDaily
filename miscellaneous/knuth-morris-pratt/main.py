"""
    ref:
    - https://www.youtube.com/watch?v=BXCEFAzhxGY
    - https://www.youtube.com/watch?v=GTJr8OvyEVQ
    - https://github.com/mission-peace/interview/blob/master/src/com/interview/string/SubstringSearch.java

    Time    O(S+T)
    Space   O(T)
"""


def knuth_morris_pratt(s, t):
    pattern = buildPattern(t)
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        elif j > 0:
            j = pattern[j-1]
        else:
            i += 1
    return j == len(t)


def buildPattern(s):
    n = len(s)
    pattern = n * [0]
    i, j = 1, 0
    while i < n:
        if s[i] == s[j]:
            pattern[i] = j + 1
            i += 1
            j += 1
        elif j > 0:
            # This is tricky, consider AAACAAAA
            j = pattern[j-1]
        else:
            i += 1
    return pattern

# a = 'dsgwadsgzd'
# print(buildPattern(a))

# a = 'AAACAAAA'
# print(buildPattern(a))


a = 'adsgwadsxdsgwadsgz'
b = 'dsgwadsgz'
print(knuth_morris_pratt(a, b))

a = 'adsgwadsxdsgwadsgz'
b = 'dsgwadsgzd'
print(knuth_morris_pratt(a, b))

a = 'aefoaefcdaefcdaed'
b = 'aefcdaed'
print(knuth_morris_pratt(a, b))

a = 'aefoaefcdaefcdaed'
b = 'aefcdaede'
print(knuth_morris_pratt(a, b))
