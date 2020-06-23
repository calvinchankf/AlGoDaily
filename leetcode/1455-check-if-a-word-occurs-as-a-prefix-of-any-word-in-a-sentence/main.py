"""
    1st: brute force string.startswith()

    Time    O(MN)
    Space   O(1)
    20 ms, faster than 100.00% 
"""


class Solution(object):
    def isPrefixOfWord(self, sentence, searchWord):
        """
        :type sentence: str
        :type searchWord: str
        :rtype: int
        """
        words = sentence.split()
        for i in range(len(words)):
            if words[i].startswith(searchWord):
                return i + 1
        return -1
