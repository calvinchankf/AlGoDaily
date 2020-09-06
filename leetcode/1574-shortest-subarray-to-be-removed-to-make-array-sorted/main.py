"""
    approach during contest binary search

    e.g. [1,2,3,10,4,2,3,5]
    forward = [1, 2, 3, 10]
    backward = [2, 3, 5]

    then we do binary search to find the longest combined array
    0 -> [1] + [2,3,5]
    1 -> [1,2] + [2,3,5] <- length = 5, which is longest
    2 -> [1,2,3] + [3,5] <- length = 5, which is longest too
    3 -> [1,2,3,10] + []

    Time    O(NlogN)
    Space   O(N)
    2824 ms, faster than 50.00%
"""


class Solution(object):
    def findLengthOfShortestSubarray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        forward = [arr[0]]
        # forward[0] =
        for i in range(1, n):
            if arr[i-1] <= arr[i]:
                forward.append(arr[i])
            else:
                break

        backward = [arr[-1]]
        # backward[n-1] = arr[-1]
        for i in range(n-2, -1, -1):
            if arr[i] <= arr[i+1]:
                backward.insert(0, arr[i])
            else:
                break
        # print(forward, backward)

        k = max(len(forward), len(backward))
        for i in range(len(forward)):
            x = forward[i]
            j = self.lowerBsearch(backward, x)
            # print(i, j)
            if 0 <= j < len(backward):
                temp = i + 1 + len(backward) - j
                k = max(k, temp)
            # else:
            #     k = max(k, i+1)
        return max(n - k, 0)

    def lowerBsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right)/2
            if target <= nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left
