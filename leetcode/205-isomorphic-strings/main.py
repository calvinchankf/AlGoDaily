import collections
""" 
    1st approach: 2 hashtables
    - 1st hashtable for str1[i] -> str2[i]
    - 2nd hashtable for str2[i] -> str1[i]

    Time  O(n)
    Space O(n)
    24 ms, faster than 99.62%
"""


class Solution(object):
    def isIsomorphic(self, a, b):
        forward = {}
        backward = {}
        for i in range(len(s)):
            c1 = s[i]
            c2 = t[i]
            if c1 not in forward:
                forward[c1] = c2
            if c2 not in backward:
                backward[c2] = c1
            if forward[c1] != c2 or backward[c2] != c1:
                return False
        return True


""" 
    2nd approach: hashtables
    
    - Compute a word's "signature"

    e.g.
    bbacyba
    0012301

    xxyzwxy
    0012301

    Time  O(n)
    Space O(n)
    16 ms, faster than 99.75%
"""


class Solution(object):
    def isIsomorphic(self, a, b):
        return self.getKey(s) == self.getKey(t)

    def getKey(self, s):
        seen = {}
        pattern = []
        for c in s:
            if c not in seen:
                seen[c] = len(seen)
            pattern.append(seen[c])
        return tuple(pattern)


"""
    followup:

    Given a list of vocabs, return a list of groups of isomorphic strings

    e.g.
    [aab, xxy, xyz, abc, def, xyx]
    return [
        [aab, xxy],
        [xyz, abc, def],
        [xyx]
    ]

    Brute force Time    O(n^3)
    
    better approach
    ---------------

    - Compute a word's "signature"

    e.g.
    bbacyba
    0012301

    xxyzwxy
    0012301

    - group the words with the same signature

    so bbacyba and xxyzwxy are groupIsomorphic
    Time    O(nk) k: average number of characters 
    Space   O(n)
"""


def groupIsomorphic(strs):
    def getSignature(word):
        signature = ""
        seen = {}
        for c in word:
            if c not in seen:
                seen[c] = len(seen)
            signature += str(seen[c]) + '#'
        return signature

    res = collections.defaultdict(list)
    for s in strs:
        code = getSignature(s)
        res[code].append(s)
    return res.values()


a = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']
print(groupIsomorphic(a))

a = ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx', 'bbacyba', 'xxyzwxy']
print(groupIsomorphic(a))
