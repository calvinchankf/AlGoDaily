"""
    1st: dynamic programming(linear)
    - similar to the stock2 problem lc122
    
    e.g.    [4, 2, 5, 3] end
    dip   0  4  2  5  3
    peak  0  4  4  5  5
    res           +2      +5
    
    for the +2: previously we saw a peak follow by a dip, so we 'consume' it
    for the +5: the approach of problem is peak1 - dip + peak2, so at the end we need to add the 'peak2' to the result

    Time    O(N)
    Space   O(1)
    820 ms, faster than 100.00%
"""


class Solution(object):
    def maxAlternatingSum(self, nums):
        peak = 0
        dip = 0
        res = 0
        for x in nums:
            if x >= dip:
                res += peak - dip
                peak = x
            dip = x
        return res + peak
