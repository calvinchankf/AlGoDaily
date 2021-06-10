from typing import List

"""
    1st: sliding window + 2 arrays prefix sum

    Time    O(kN)
    Space   O(k)
    TLE 
"""


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        n = len(nums)
        j = 0
        oneCount = 0
        res = 2**32
        for i in range(n):
            oneCount += nums[i]
            while oneCount > k or nums[j] == 0:
                oneCount -= nums[j]
                j += 1
            if oneCount == k:
                swapCount = self.countSwap(nums, j, i, k)
                res = min(res, swapCount)
        return res

    def countSwap(self, nums, j, i, k):
        forward = []
        oneCount = 0
        total = 0
        for idx in range(j, i+1):
            if nums[idx] == 1:
                oneCount += 1
            elif idx-1 >= j and nums[idx-1] == 0:
                total += oneCount
                forward[-1] = total
            else:
                total += oneCount
                forward.append(total)
        # print(forward)
        backward = []
        oneCount = 0
        total = 0
        for idx in range(i, j-1, -1):
            if nums[idx] == 1:
                oneCount += 1
            elif idx+1 <= i and nums[idx+1] == 0:
                total += oneCount
                backward[-1] = total
            else:
                total += oneCount
                backward.append(total)
        backward = backward[::-1]
        # print(backward)
        if len(forward) == 0:
            return 0
        if len(forward) == 1:
            return min(forward[0], backward[0])
        count = 2**32
        for idx in range(len(forward)-1):
            count = min(count, forward[idx] + backward[idx+1])
        return min(count, forward[-1], backward[0])


"""
    2nd: sliding window + prefix sum + math
    - see idea2.png

    Time    O(N)
    Space   O(k)
    1180 ms, faster than 73.33%
"""


class Solution(object):
    def minMoves(self, nums, k):
        ones = []
        for i in range(len(nums)):
            if nums[i] == 1:
                ones.append(i)
        n = len(ones)
        pfss = [0]
        for i in range(n):
            pfss.append(pfss[-1] + ones[i])
        res = 2**32
        mid = (k + 1) // 2
        midLeft = k // 2
        for i in range(n-k+1):
            right = pfss[i + k] - pfss[i + mid]
            left = pfss[i + midLeft] - pfss[i]
            extraCost = mid * midLeft
            res = min(res, right - left - extraCost)
        return res


s = Solution()

a = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1]
b = 5
print(s.minMoves(a, b))

a = [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1]
b = 6
print(s.minMoves(a, b))
