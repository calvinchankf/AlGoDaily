"""
    1st approach
	1. count num: freq into a hashtable
	2. sort the hashtable keys by frequency
	3. append the key to the result according to a descending index order(freqency)

	Time	O(n)
	Space	O(n)
	36 ms, faster than 86.91%
"""


class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        ht = {}
        for c in s:
            if c in ht:
                ht[c] += 1
            else:
                ht[c] = 1
        keys = [(ht[key], key) for key in ht]
        keys.sort(reverse=True)
        res = ''
        for count, key in keys:
            res += count * key
        return res
