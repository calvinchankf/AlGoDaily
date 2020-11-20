"""
    1st approach: 2 hashtables

    Time    O(n)
    Space   O(n)
    16 ms, faster than 99.31%
"""


class Solution(object):
    def wordPattern(self, pattern, sentence):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        forward = {}
        backward = {}
        words = sentence.split()
        if len(pattern) != len(words):
            return False
        for i in range(len(pattern)):
            a = pattern[i]
            b = words[i]
            if a in forward and forward[a] != b:
                return False
            if b in backward and backward[b] != a:
                return False
            forward[a] = b
            backward[b] = a
        return True


"""
    2nd approach: hashtable but calculate signature

    - Compute a word's "signature"
    
    e.g.1
    bbacyba
    0012301

    e.g.2
    xxyzwxy
    0012301

    Time    O(n)
    Space   O(n)
    16 ms, faster than 99.31%
"""


class Solution(object):
    def wordPattern(self, pattern, sentence):
        a = self.getSignature(pattern)
        b = self.getSignature(s.split(' '))
        return a == b

    def getSignature(self, arr):
        ht = {}
        signs = []
        for x in arr:
            if x not in ht:
                ht[x] = len(ht)
            signs.append(ht[x])
        return tuple(signs)
