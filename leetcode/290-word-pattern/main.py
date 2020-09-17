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
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = sentence.split()
        if len(pattern) != len(words):
            return False
        s1 = self.calSignature(pattern)
        s2 = self.calSignature(words)
        return s1 == s2

    def calSignature(self, s):
        signature = ""
        seen = {}
        nth = 0
        for c in s:
            if c not in seen:
                seen[c] = str(nth)
                nth += 1
            signature += seen[c] + '#'
        return signature
