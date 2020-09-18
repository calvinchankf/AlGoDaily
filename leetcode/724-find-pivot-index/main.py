"""
    1st: 2 arrays
    
    Time    O(3N)
    Space   O(2N)
    172 ms, faster than 56.15% 
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        forward = n * [0]
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            forward[i] = pfs
        backward = n * [0]
        sfs = 0
        for i in range(n-1, -1, -1):
            sfs += nums[i]
            backward[i] = sfs
        for i in range(n):
            if i == 0:
                if backward[i+1] == 0:
                    return 0
            elif i + 1 == n:
                if forward[i-1] == 0:
                    return n - 1
            elif forward[i-1] == backward[i+1]:
                return i
        return -1


"""
    2nd: similar to 1st
    - insert 0s at the begining and the end so that we dont have to think about the edge cases

    Time    O(3N)
    Space   O(2N)
    160 ms, faster than 76.11%
"""


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        nums = [0] + nums + [0]
        n = len(nums)
        forward = n * [0]
        pfs = 0
        for i in range(n):
            pfs += nums[i]
            forward[i] = pfs
        backward = n * [0]
        sfs = 0
        for i in range(n-1, -1, -1):
            sfs += nums[i]
            backward[i] = sfs
        for i in range(1, n-1):
            if forward[i-1] == backward[i+1]:
                return i-1
        return -1
