"""
    1st: 2 pointers

    Time    O(A+B)
    Space   O(A+B)
    24 ms, faster than 100.00%
"""


class Solution(object):
    def mergeAlternately(self, word1, word2):
        res = ''
        i, j = 0, 0
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1
        if i < len(word1):
            res += word1[i:]
        if j < len(word2):
            res += word2[j:]
        return res
