"""
    1st: lexicographical ordering + bruteforce
    - use the approach in leetcode31 k times
    - and then swap the adjacent numbers until the num becomes kth smaller element <- brute force

    Time    O(KN + N^2) worst
    Space   O(N)
    1916 ms, faster than 43.42%
"""


class Solution(object):
    def getMinSwaps(self, num, k):
        nums = []
        for c in num:
            nums.append(int(c))
        orig = nums[:]
        for i in range(k):
            self.nextPermutation(nums)
        res = 0
        n = len(nums)
        for i in range(n):
            if orig[i] == nums[i]:
                continue
            target = -1
            for j in range(i+1, n):
                if orig[j] == nums[i]:
                    target = j
                    break
            if target == -1:
                continue
            for j in range(target, i, -1):
                orig[j-1], orig[j] = orig[j], orig[j-1]
                res += 1
        return res

    def nextPermutation(self, nums):
        n = len(nums)
        i = n - 1
        while i - 1 >= 0 and nums[i-1] >= nums[i]:
            i -= 1

        if i == 0:
            self.reverse(nums, 0, n-1)
            return

        pivot = i - 1

        j = n - 1
        while j - 1 >= 0 and nums[j] <= nums[pivot]:
            j -= 1

        nums[pivot], nums[j] = nums[j], nums[pivot]

        self.reverse(nums, i, n-1)

    def reverse(self, nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
