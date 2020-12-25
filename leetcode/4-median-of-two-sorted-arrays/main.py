"""
    2nd approach: 2 pointers to merge the arrays like merge sort
	- use 2 pointers to merge the arrays and return merged[half] or (merged[half-1]+merged[half])/2

	Time		O(m+n)
	Space 	O(m+n)
	92 ms, faster than 34.65%
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        res = []
        p1 = 0
        p2 = 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        if p1 < len(nums1):
            res += nums1[p1:]
        if p2 < len(nums2):
            res += nums2[p2:]
        if len(res) % 2 == 0:
            half = len(res)//2
            left = res[half-1]
            right = res[half]
            return (left + right)/2.0
        half = len(res)//2
        return float(res[half])


a = [1, 3]
b = [2]
print(Solution().findMedianSortedArrays(a, b))

a = [1, 3]
b = [2, 4]
print(Solution().findMedianSortedArrays(a, b))


a = []
b = [1]
print(Solution().findMedianSortedArrays(a, b))

a = [4, 6, 7, 8]
b = [1, 2, 3, 5]
print(Solution().findMedianSortedArrays(a, b))

print("---------------")

"""
    3rd approach: binary search

    e.g.
    a = [1, 3, 4]
    b = [2, 5, 6, 9]

    we split the 1st array into half and then use the remain to calculate the right position in 2nd array
    1 |3 4
       ^
    2 5 6 |9
           ^
    
    since 6 > 3, we need to move forward the pointer on the 1st array
    1 3 |4
         ^
    2 5 |6 9
         ^

    since 5 > 4, we need to move forward the pointer on the 1st array
    1 3 4 |
           ^
    2 |5 6 9
       ^
    
    we are on the right position, since the total count = 7, 
    the median must be either the left on 1st array or the left on 2nd array

    left = max(4, 2) = 4, this is the result


	Time		O(log(min(M,N))
	Space 	    O(1)
	88 ms, faster than 78.54%
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # get the lengths
        m, n = len(nums1), len(nums2)
        # make sure that m <= n
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        # if the larger array is empty, just return empty
        if n == 0:
            return 0.0

        # binary search
        left = 0
        right = m
        # the number of sum of nums1[left1] and nums2[left] must be the half of the total count
        halfLen = (m + n + 1) // 2
        while left <= right:
            mid1 = (left + right) // 2
            mid2 = halfLen - mid1
            if mid1 < m and nums1[mid1] < nums2[mid2-1]:
                # mid1 is too small, increase it
                left = mid1 + 1
            elif mid1 > 0 and nums1[mid1-1] > nums2[mid2]:
                # mid1 is too big, decrease it
                right = mid1 - 1
            else:
                # mid1 is perfect

                # find the left
                maxLeft = 0
                if mid1 == 0:
                    maxLeft = nums2[mid2-1]
                elif mid2 == 0:
                    maxLeft = nums1[mid1-1]
                else:
                    maxLeft = max(nums1[mid1-1], nums2[mid2-1])

                if (m + n) % 2 == 1:
                    return maxLeft * 1.0

                # find the right
                minRight = 0
                if mid1 == m:
                    minRight = nums2[mid2]
                elif mid2 == n:
                    minRight = nums1[mid1]
                else:
                    minRight = min(nums1[mid1], nums2[mid2])

                return (maxLeft + minRight) / 2.0


a = [1, 3]
b = [2]
print(Solution().findMedianSortedArrays(a, b))

a = [1, 3]
b = [2, 4]
print(Solution().findMedianSortedArrays(a, b))


a = []
b = [1]
print(Solution().findMedianSortedArrays(a, b))

a = [4, 6, 7, 8]
b = [1, 2, 3, 5]
print(Solution().findMedianSortedArrays(a, b))
