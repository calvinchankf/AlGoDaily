"""
    1st approach: recursion

    Time    O(2^n) every number has 2 options
    Space   O(h)
    LTE
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        return self.ifCanPartition(nums, total//2, 0)

    def ifCanPartition(self, cands, remain, curIdx):
        if remain == 0:
            return True
        if remain < 0 or len(cands) == 0 or curIdx >= len(cands):
            return False
        # choose or not choose
        return self.ifCanPartition(cands, remain - cands[curIdx], curIdx + 1)\
            or self.ifCanPartition(cands, remain, curIdx + 1)


s = Solution()

a = [1, 2, 3, 4]
print(s.canPartition(a))

a = [1, 1, 3, 4, 7]
print(s.canPartition(a))

a = [2, 3, 4, 6]
print(s.canPartition(a))

a = [1, 5, 11, 5]
print(s.canPartition(a))

a = [1, 2, 3, 5]
print(s.canPartition(a))

print("-----")

"""
    2nd approach: top-down recursion with memoization using hashtable
    - every number has 2 options
    - but we can cache the result of the combinations of remainTarget and currentIdx to avoid redundant calculation

    ref:
    - https://en.wikipedia.org/wiki/Partition_problem
    - https://www.educative.io/collection/page/5668639101419520/5633779737559040/5752754626625536

    Time    O(NS) N: number of nums, S: the total sum of all the numbers
    Space   O(h)
    32 ms, faster than 92.21%
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        target = total // 2
        if target * 2 != total:
            return False
        return self.dfs(nums, 0, target, {})

    def dfs(self, nums, i, remain, cache):
        if i == len(nums):
            return remain == 0
        # below 2 conditions are not necessary
        # speed up: return boolean when we reach to target (even when i < N)
        if remain == 0:
            return True
        if remain < 0:
            return False
        # return cache if any
        key = (remain, i)
        if key in cache:
            return cache[key]
        # include or exclude
        cache[key] = self.dfs(nums, i+1, remain - nums[i], cache) \
            or self.dfs(nums, i+1, remain, cache)
        return cache[key]


s = Solution()

a = [1, 2, 3, 4]
print(s.canPartition(a))

a = [1, 1, 3, 4, 7]
print(s.canPartition(a))

a = [2, 3, 4, 6]
print(s.canPartition(a))

a = [1, 5, 11, 5]
print(s.canPartition(a))

a = [1, 2, 3, 5]
print(s.canPartition(a))

print("-----")

"""
    3rd approach: bottom-up iterative 2d array
    - create a 2d array to store if we can add up to target by including/excluding some numbers
    - the array should have len(nums) rows
    - since target = sum//2, every row should have len(target) columns
    - to determind dp[i][remain_sum]
        - if dp[i-1][remain_sum] == True, it means that already add up to 'target', exclude the nums[i], 
        i.e. dp[i][j] = dp[i-1][j]
        - elif j >= nums[i], it means we can substract the j withe nums[i](include nums[i]), to see if later we can subtract the remain_sum down to 0, 
        i.e.e dp[i][j] = dp[i-1][j - nums[i]]

    Time    O(NS)
    Space   O(NS)
    1856 ms, faster than 21.08%
"""


class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)

        # if 's' is a an odd number, we can't have two subsets with same total
        if s % 2 != 0:
            return False

        # we are trying to find a subset of given numbers that has a total sum of 's/2'
        target = s//2
        dp = []
        for i in range(len(nums)):
            temp = (target+1) * [False]
            dp.append(temp)

        # populate the s=0 columns, as we can always for '0' sum with an empty set
        # because dp[i][s-nums[i]] might equal to dp[i][0]
        for i in range(0, len(nums)):
            dp[i][0] = True

        # first row
        for j in range(1, target+1):
            dp[0][j] = nums[0] == j

        # process all subsets for all sums
        for i in range(1, len(nums)):
            for j in range(1, target+1):
                if dp[i - 1][j] == True:
                    # exclude nums[i]
                    dp[i][j] = dp[i-1][j]
                elif j >= nums[i]:
                    # include the nums[i]
                    dp[i][j] = dp[i-1][j - nums[i]]

        # the bottom-right corner will have our answer.
        return dp[-1][target]


s = Solution()

a = [1, 2, 3, 4]
print(s.canPartition(a))

a = [1, 1, 3, 4, 7]
print(s.canPartition(a))

a = [2, 3, 4, 6]
print(s.canPartition(a))

a = [1, 5, 11, 5]
print(s.canPartition(a))

a = [1, 2, 3, 5]
print(s.canPartition(a))
