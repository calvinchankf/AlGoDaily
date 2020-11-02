"""
    0th: dynamic programming(recursion + hashtable)

    Time    O(N^2 x 3)
    LTE 35 / 42 test cases passed.
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        hht = {}
        windowSum, windowSumIndices = self.dfs(nums, k, 0, 3, ht)
        return sorted(windowSumIndices)
    
    def dfs(self, nums, k, fromIdx, n, ht):
        if fromIdx == len(nums):
            if n == 0:
                return 0, []
            return -2**31, []
        if n == 0:
            return 0, []
        
        key = (fromIdx, n)
        if key in ht:
            return ht[key]
        
        maxCombinedSum = 0
        maxIndices = []

        maxWindowSum = 0
        maxWindowSumIdx = 0

        windowSum = 0

        j = fromIdx
        for i in range(fromIdx, len(nums)):
            windowSum += nums[i]
            if i - j >= k:
                windowSum -= nums[i-k]
                j += 1
            if i - j + 1 >= k:
                if windowSum > maxWindowSum:
                    maxWindowSum = windowSum
                    maxWindowSumIdx = j

                maxSumFromBack, maxSumIndicesFromBack = self.dfs(nums, k, i+1, n-1, ht)
                temp = maxWindowSum + maxSumFromBack
                if temp > maxCombinedSum:
                    maxCombinedSum = temp
                    maxIndices = maxSumIndicesFromBack + [maxWindowSumIdx]
        
        ht[key] = (maxCombinedSum, maxIndices)
        return ht[key]

s = Solution()

a = [1,2,1,2,6,7,5,1]
b = 2
print(s.maxSumOfThreeSubarrays(a, b)) # [0, 3, 5]

a = [1,2,1,2,1,2,1,2,1]
b = 2
print(s.maxSumOfThreeSubarrays(a, b)) # [0, 2, 4]

a = [1,2,1,2,6,7,5,1,7]
b = 3
print(s.maxSumOfThreeSubarrays(a, b)) # [0, 3, 6]

a = [1,2,1,2,6,7,5,1,7,6,5,4]
b = 3
print(s.maxSumOfThreeSubarrays(a, b)) # [3, 6, 9]\

print("-----")

"""
    1st: 2 arrays trick
    - similar to lc42, 135, 487, 689, 915, 1493

    Time    O(N)
    Space   O(N)
    180 ms, faster than 79.53%
"""
class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        W = [] # array of windowSums
        windowSum = 0
        for i in range(len(nums)):
            windowSum += nums[i]
            if i >= k: 
                windowSum -= nums[i - k]
            if i >= k - 1: 
                W.append(windowSum)

        lefts = [0] * len(W)
        best = 0
        for i in range(len(W)):
            if W[i] > W[best]:
                best = i
            lefts[i] = best

        rights = [0] * len(W)
        best = len(W) - 1
        for i in range(len(W) - 1, -1, -1):
            if W[i] >= W[best]: # >= to get lexicographically smallest
                best = i
            rights[i] = best

            
        ans = None
        for i in range(k, len(W) - k):
            left, right = lefts[i - k], rights[i + k]
            if ans is None or (W[left] + W[i] + W[right] > W[ans[0]] + W[ans[1]] + W[ans[2]]):
                ans = left, i, right
        return ans