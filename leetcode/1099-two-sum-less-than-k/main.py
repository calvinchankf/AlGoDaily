"""
    1st approach: sort + 2 pointers
    - 2 sum closest

    Time    O(nlogn)
    Space   O(1)
    32 ms, faster than 67.83%
"""


class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A = sorted(A)
        left = 0
        right = len(A) - 1
        res = -1
        while left < right:
            total = A[left] + A[right]
            if total < K:
                res = max(res, total)
                left += 1
            else:
                right -= 1
        return res


a = [358, 898, 450, 732, 672, 672, 256, 542, 320, 573, 423, 543, 591, 280, 399, 923, 920, 254, 135, 952, 115, 536, 143, 896, 411,
     722, 815, 635, 353, 486, 127, 146, 974, 495, 229, 21, 733, 918, 314, 670, 671, 537, 533, 716, 140, 599, 758, 777, 185, 549]
b = 1800
print(Solution().twoSumLessThanK(a, b))

print("-----")

"""
    2nd approach: sort + binary search
    - 2 sum closest

    Time    O(2nlogn)
    Space   O(1)
    36 ms, faster than 53.91%
"""


class Solution(object):
    def twoSumLessThanK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        A.sort()
        res = -sys.maxsize
        for i in range(len(A)):
            a = A[i]
            j = self.bsearch(A, K - a)
            if i < j < len(A) and a + A[j] < K:
                res = max(res, a + A[j])
        if res == -sys.maxsize:
            return -1
        return res

    def bsearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1
            else:
                return mid
        return right


a = [34, 23, 1, 24, 75, 33, 54, 8]
b = 60
print(Solution().twoSumLessThanK(a, b))

a = [34, 23, 1, 24, 75, 33, 54, 8]
b = 77
print(Solution().twoSumLessThanK(a, b))

a = [358, 898, 450, 732, 672, 672, 256, 542, 320, 573, 423, 543, 591, 280, 399, 923, 920, 254, 135, 952, 115, 536, 143, 896, 411,
     722, 815, 635, 353, 486, 127, 146, 974, 495, 229, 21, 733, 918, 314, 670, 671, 537, 533, 716, 140, 599, 758, 777, 185, 549]
b = 1800
print(Solution().twoSumLessThanK(a, b))
