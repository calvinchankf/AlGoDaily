"""
    1st approach: dynamic programming
    - similar to lc198, 300, 1671

    ref: Longest Increasing Subsequence
    - https://www.youtube.com/watch?v=CE2b_-XfVDk

    Time    O(N^2)
    Space   O(N)
    1068 ms, faster than 12.81%
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res = 1
        dp = n * [1]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


s = Solution()

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(s.lengthOfLIS(a))

a = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(a))

a = [0, 1, 0, 3, 2, 3]
print(s.lengthOfLIS(a))

a = [7, 7, 7, 7, 7, 7, 7]
print(s.lengthOfLIS(a))

print('-----')


"""
    2nd: binary search
    - we are gonna maintain a sorted array A
        - A[i] represent the end of an increasing subsequence
        - i + 1 represent the length of that increasing subsequence
    1. when there is a larger number coming in, append it to A
    2. when there is a smaller number comming in, use it to replace a number in A

    e.g [100, 9, 2, 9, 3, 7, 101, 6].

    dp = [100]
    dp = [9]
    dp = [2]
    dp = [2, 9]
    dp = [2, 3]
    dp = [2, 3, 7]
    dp = [2, 3, 7, 101]
    dp = [2, 3, 6, 101]
                ^
                binary search 6, since 7 > 6, replace 7 with 6
    
    At the end,
    idx0 = 2,   means there is a subsequnce of length 1, which ends at 2. e.g. sub = [2]
    idx1 = 3,   means there is a subsequnce of length 2, which ends at 3. e.g. sub = [2, 3]
    idx2 = 6,   means there is a subsequnce of length 3, which ends at 6. e.g. sub = [2, 3, 6]
    idx3 = 101, means there is a subsequnce of length 4, which ends at 101. e.g. sub = [2, 3, 7, 101]

    ref:
    - https://leetcode.com/problems/longest-increasing-subsequence/discuss/667975/Python-3-Lines-dp-with-binary-search-explained

    Time    O(NlogN)
    Space   O(N)
    68 ms, faster than 77.49%
"""


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sub = []
        for x in nums:
            if len(sub) == 0 or x > sub[-1]:
                sub.append(x)
            else:
                i = self.lowerBsearch(sub, x)
                sub[i] = x
        return len(sub)

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left


s = Solution()

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(s.lengthOfLIS(a))

a = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(a))

a = [0, 1, 0, 3, 2, 3]
print(s.lengthOfLIS(a))

a = [7, 7, 7, 7, 7, 7, 7]
print(s.lengthOfLIS(a))

print('-----')

"""
    follow up: print the subsequence
"""


class Solution(object):
    def printLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = []
        for i in range(n):
            dp.append([nums[i]])
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # dp[i] = max(dp[j] + 1, dp[i])
                    if len(dp[j]) + 1 > len(dp[i]):
                        dp[i] = dp[j] + [nums[i]]
        res = []
        for x in dp:
            if len(x) > len(res):
                res = x
        return res


s = Solution()

a = [5, 7, -24, 12, 10, 2, 3, 12, 5, 6, 35]
print(s.printLIS(a))

a = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.printLIS(a))

a = [0, 1, 0, 3, 2, 3]
print(s.printLIS(a))

a = [7, 7, 7, 7, 7, 7, 7]
print(s.printLIS(a))
