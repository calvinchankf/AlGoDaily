"""
    1st: greedy
    - learned from others

    case1: [1,1,2,5]
    0: []
    1: [1]
    2: [1,1]
    3: [2,1]
    4: [2,1,1]
    5: [5]          <= [5] + []
    6: [5,1]        <= [5] + [1]
    7: [5,1,1]      <= [5] + [1,1]
    8: [5,2,1]      <= [5] + [2,1]
    9: [5,2,1,1]    <= [5] + [2,1,1]

    case2: [1,1,2,6]
    0: []
    1: [1]
    2: [1,1]
    3: [2,1]
    4: [2,1,1]
    5: fail to come up 5 becox 6 > (1+1+2)+1, so we stop here

    refs:
    - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/discuss/1118770/JavaC%2B%2BPython-Accumulate-the-Coins
    - https://leetcode.com/problems/maximum-number-of-consecutive-values-you-can-make/discuss/1118766/C%2B%2BJavaPython-with-picture

    Time    O(NlogN)
    Space   O(1)
    732 ms, faster than 100.00%
"""


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        pfs = 0
        for c in coins:
            if c > pfs + 1:
                break
            pfs += c
        return pfs + 1
