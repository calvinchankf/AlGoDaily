"""
    0th: brute-fore

    Time    O(N^2)
    LTE
"""


class Solution:
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = nums[:k]
        window = nums[:k]
        for i in range(k, n):

            window.pop(0)
            window.append(nums[i])

            for j in range(k):
                if window[j] < res[j]:
                    break
                elif window[j] > res[j]:
                    res = window[:]
                    break
        return res


"""
    1st: greedy
    - find the largest num in range [0, n - k]
    - this integer is the first element in the result subarray

    Time    O(N)
    Space   O(N)
    828 ms, faster than 100.00%
"""


class Solution(object):
    def largestSubarray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        sub = nums[:n-k+1]
        maxNum = -(2**32)
        maxNumIdx = -1
        for i in range(len(sub)):
            if sub[i] > maxNum:
                maxNum = sub[i]
                maxNumIdx = i
        return nums[maxNumIdx:maxNumIdx+k]
