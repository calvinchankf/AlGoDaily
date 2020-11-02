
from collections import Counter

"""
    1st: hashtable + sort

    Time    O(NlogN)
    Space   O(N)
    36 ms, faster than 100.00%
"""
class Solution(object):
    def frequencySort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = Counter(nums)
        freqs = [(counter[key], key) for key in counter]
        
        def cmpter(a, b):
            if a[0] == b[0]:
                return b[1] - a[1]
            return a[0] - b[0]
        
        freqs.sort(cmp=cmpter)
        res = []
        for f, x in freqs:
            res += f * [x]
        return res