"""
    1st approach: string checking
    - check if each of the words can be formed by deleting characters from s
    - there are 2 conditions to update the intermediate result
        1. length of this word is longer than the intermediate result
        2. this word is lexicologically lower than intermediate result if both lengths are the same
    
    Time    O(nk) n: number of the words in dictionary, k: length of the s
    Space   O(k) at worst case it would be s
    224 ms, faster than 77.90%
"""


class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ''
        for w in d:
            if self.check(s, w):
                # conditions
                # 1. length of this word is longer than the intermediate result
                # 2. this word is lexicologically lower than intermediate result if both lengths are the same
                if len(w) > len(res) or len(w) == len(res) and w < res:
                    res = w
        return res

    # check if the word can be formed from deleting characters in s
    def check(self, s, w):
        i = 0
        j = 0
        while i < len(s) and j < len(w):
            if s[i] == w[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j == len(w)
