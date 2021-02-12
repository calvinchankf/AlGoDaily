from bisect import *
"""
    1st approach: hashtable
    - count the occurence of each number
    - harmonic subsequence is actually the count[num] + count[num+1] or (count[num-1] + count[num])

    e.g. [1,2,1,3,0,0,2,2,1,3,3]

    [1,2,1,3,0,0,2,2,1,3,3]
               ^   ^ ^   ^ arrows represent the last occurence of each number
    
    count = {
        0: 2,
        1: 3,
        2: 3,
        3: 3,
    }

    the answer is count[2] + count[3] = 6

    Time    O(N)
    Space   O(N)
    272 ms, faster than 67.92%
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
        ans = 0
        for x in m:
            if x+1 in m:
                ans = max(ans, m[x] + m[x+1])
        return ans


"""
    2nd approach: hashtable, but in one pass
    - count the occurence of each number
    - simlar to 1st approach but since we are inside a loop we need to check the lower bound and the upperbound
        count[num] + count[num+1] or count[num-1] + count[num]

    Time    O(N)
    Space   O(N)
    332 ms, faster than 40.14% 
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        ans = 0
        for num in nums:
            if num not in m:
                m[num] = 1
            else:
                m[num] += 1
            # check if there are harmonic numbers
            if num-1 in m:
                ans = max(ans, m[num] + m[num-1])
            if num+1 in m:
                ans = max(ans, m[num] + m[num+1])
        return ans


"""
    3rd: sort + binary search
    
    Time    O(NlogN)
    Space   O(N)
"""


class Solution(object):
    def findLHS(self, nums):
        nums.sort()
        ht = {}
        res = 0
        for i in range(len(nums)):
            x = nums[i]
            j = bisect_left(nums, x-1)
            if nums[j] == x-1:
                res = max(res, i - j + 1)
        return res
