"""
    1st approach: compare strings

    e.g.1
    3, 32
    332 vs 323 = 3(32) vs (32)3 => 332 is larger

    e.g.2
    3, 34
    334, 343 = 3(34) vs (34)3 => 343 is larger

    corner case:
    nums = [0, 0]

    Time    O(nlogn)
    Space   O(n)
    20 ms, faster than 95.71%
"""


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # custom comparator
        def cmptr(a, b):
            ab = int(str(a)+str(b))
            ba = int(str(b)+str(a))
            return ba-ab
        nums.sort(cmp=cmptr)
        # construct result
        res = ""
        for num in nums:
            res += str(num)
        return str(int(res))


a = [3, 30, 34, 5, 9]
print(Solution().largestNumber(a))

a = [0, 0]
print(Solution().largestNumber(a))
