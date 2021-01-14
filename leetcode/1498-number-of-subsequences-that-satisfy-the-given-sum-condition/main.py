"""
    1st: kind of brute force
    - we only care about the min and max in every subsequnce, it means that a sorted subsequence would help
    - for every index, find out how many sequences which fulfills the condition
    - all subsequcens in an array = subsets = 2**N

    Time    O(NlogN + N^2)
    Space   O(1)
    7432 ms, faster than 5.68%
"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        j = n - 1
        for i in range(n):
            while nums[i] + nums[j] > target and i <= j:
                j -= 1
            if i <= j:
                res += 2**(j - i)
                res %= 10**9 + 7
        return res


"""
    2nd: sort + 2 pointers
    - optimize the 1st approach
    - we only care about the min and max in every subsequnce, it means that a sorted subsequence would help
    - for every LEGIT starting index, find out how many sequences whichs fulfills the condition
    - all subsequcens in an array = subsets = 2**N

    Time    O(NlogN + N)
    Space   O(1)
    7368 ms, faster than 10.41% 
"""


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        left = 0
        right = n - 1
        while left <= right:
            total = nums[left] + nums[right]
            if total <= target:
                temp = 2**(right - left) % (10**9 + 7)
                res += temp
                left += 1
            else:
                right -= 1
        return res % (10**9 + 7)
