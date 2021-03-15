"""
    1st: recursion
    - in every recursion, compare the suffix and append the first character from the larger suffix

    hint:
    - https://leetcode.com/problems/largest-merge-of-two-strings/discuss/1053549/JavaC%2B%2BPython-Easy-Greedy 

    Time    O(AB)
    Space   O(AB)
    140 ms, faster than 100.00%
"""


class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        if len(word1) == 0 or len(word2) == 0:
            return word1 + word2
        if word1 >= word2:
            return word1[0] + self.largestMerge(word1[1:], word2)
        return word2[0] + self.largestMerge(word1, word2[1:])
