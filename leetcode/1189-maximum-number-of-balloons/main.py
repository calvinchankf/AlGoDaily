"""
    1st: hashtable
    - count the occurence of each character
    - compute the number of 'balloon' we can form
    
    Time    O(N)
    Space   O(26)
    24 ms, faster than 75.12%
"""


class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        ht = 26 * [0]
        for c in text:
            idx = ord(c) - ord('a')
            ht[idx] += 1
        single = min(ht[0], ht[1], ht[13])  # a, b, n
        double = min(ht[11], ht[14])  # l, o
        return min(single, double//2)
