"""
    1st approach: hashtable

    Time    O(2n)
    Space   O(n)
    156 ms, faster than 60.47% 
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = {}
        for num in nums:
            if num in m:
                m[num] += 1
            else:
                m[num] = 1
        maxCnt = 0
        res = -1
        for key in m:
            if m[key] > maxCnt:
                maxCnt = m[key]
                res = key
        return res


"""
    2nd approach: Boyer-Moore Voting Algorithm
    - if a number appears more than n/2 times, we can balance off the numbers which are not that number
    
    e.g. [2,2,1,1,1,2,2]
          ^ ^ * * ^ * ^
    the last ^ points to the remaining number <- which is our result

    Time    O(n)
    Space   O(1)
    152 ms, faster than 84.70%
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cand = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                cand = nums[i]
            if nums[i] == cand:
                count += 1
            else:
                count -= 1
        return cand
