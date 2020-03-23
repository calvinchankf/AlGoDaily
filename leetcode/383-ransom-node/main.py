"""
    1st: hashtable

    Time    O(M+N)
    Space   O(M+N)
    96 ms, faster than 15.35%
"""


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ht_magazine = 26 * [0]
        ht_ransome = 26 * [0]
        for c in magazine:
            idx = ord(c) - ord('a')
            ht_magazine[idx] += 1
        for c in ransomNote:
            idx = ord(c) - ord('a')
            ht_ransome[idx] += 1
        for i in range(26):
            if ht_ransome[i] > ht_magazine[i]:
                return False
        return True
