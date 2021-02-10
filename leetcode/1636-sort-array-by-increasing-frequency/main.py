
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

        freqs.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for f, x in freqs:
            res += f * [x]
        return res


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))
