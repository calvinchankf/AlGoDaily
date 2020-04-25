class Solution(object):
    def mergesort(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]

        merge sort: https://www.geeksforgeeks.org/merge-sort/
        - divides input array into two halves recursively
        - merge two sorted halves and then return
        - this version occupies space(not in-place)
        - first divide, second process; the procedure is similar to post order traversal
        Time	O(nlogn)
        Space O(n)
        """
        return self.divide(nums)

    def divide(self, nums):
        if len(nums) == 1:
            return nums
        half = len(nums)/2
        left = self.divide(nums[:half])
        right = self.divide(nums[half:])
        return self.conquer(left, right)

    def conquer(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res += left[i:]
        if j < len(right):
            res += right[j:]
        return res


s = Solution()

a = [45, 6, 7, 89, 0, 1, 2, 2, 34]

print(s.mergesort(a))
