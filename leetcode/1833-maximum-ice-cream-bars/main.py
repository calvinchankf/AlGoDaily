"""
    1st: sort

    Time    O(NlogN)
    Space   O(1)
    676 ms, faster than 92.05%
"""
class Solution(object):
    def maxIceCream(self, costs, coins):
        costs.sort()
        count = 0
        for c in costs:
            if coins - c >= 0:
                coins -= c
                count += 1
            else:
                break
        return count
