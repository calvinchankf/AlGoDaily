class Solution(object):

    def kSmallest(self, nums, k):
        return self.helper(nums, 0, len(nums)-1, k)

    def helper(self, nums, left, right, k):
        if k > 0 and k <= len(nums):
            pIdx = self.partition(nums, left, right)
            if pIdx+1 == k:
                return nums[pIdx]
            elif pIdx+1 < k:
                return self.helper(nums, pIdx+1, right, k)
            else:
                return self.helper(nums, left, pIdx-1, k)
        return -1

    def partition(self, nums, left, right):
        pivot = nums[right]
        pIdx = left
        for i in range(left, right):
            if nums[i] <= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        nums[pIdx], nums[right] = nums[right], nums[pIdx]
        return pIdx


# [2, 4, 6, 8, 10, 12]
a = [10, 12, 2, 4, 8, 6]
print(Solution().kSmallest(a, 1))
print(Solution().kSmallest(a, 2))
print(Solution().kSmallest(a, 3))
print(Solution().kSmallest(a, 4))

print("-----")


class Solution(object):

    def kLargest(self, nums, k):
        return self.helper(nums, 0, len(nums)-1, k)

    def helper(self, nums, left, right, k):
        if k > 0 and k <= len(nums):
            pIdx = self.partition(nums, left, right)
            if pIdx+1 == k:
                return nums[pIdx]
            elif pIdx+1 < k:
                return self.helper(nums, pIdx+1, right, k)
            else:
                return self.helper(nums, left, pIdx-1, k)
        return None

    def partition(self, nums, left, right):
        pivot = nums[right]
        pIdx = left
        for i in range(left, right):
            if nums[i] >= pivot:
                nums[i], nums[pIdx] = nums[pIdx], nums[i]
                pIdx += 1
        nums[pIdx], nums[right] = nums[right], nums[pIdx]
        return pIdx


# [12, 10, 8, 6, 4, 2]
a = [10, 12, 2, 4, 8, 6]
print(Solution().kLargest(a, 1))
print(Solution().kLargest(a, 2))
print(Solution().kLargest(a, 3))
print(Solution().kLargest(a, 4))
