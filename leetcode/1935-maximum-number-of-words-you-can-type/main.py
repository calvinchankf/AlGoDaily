"""
    1st: hashtable

    Time    O(B + N)
    Space   O(B)
    28 ms, faster than 100.00%
"""


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brokens = set()
        for c in brokenLetters:
            brokens.add(c)
        words = text.split()
        res = 0
        for w in words:
            isBroken = False
            for c in w:
                if c in brokens:
                    isBroken = True
                    break
            if isBroken == False:
                res += 1
        return res
