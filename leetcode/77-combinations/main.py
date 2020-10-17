class Solution(object):
    """
    Implementation similar to permutations

    select k from n number, it is a combination problem
    therefore, the time complexity is nCk

    nCk = n!/(n-k)!k!

    Time    O(nCk)
    Space   O(nCk) due to the recrusion
    beats   13.88%
    """

    def __init__(self):
        self.result = []

    def combine(self, n, k):
        if k < 1 or k > n:
            return []
        # construct the arrary from 1 to n
        nums = []
        for i in range(n):
            nums.append(i+1)
        # dfs
        self.dfs(nums, [], k)
        return self.result

    def dfs(self, nums, path, k):
        if len(path) == k:
            self.result.append(path)
        elif len(path) < k:
            for i in range(len(nums)):
                self.dfs(nums[i+1:], path + [nums[i]], k)


s = Solution()

r = s.combine(4, 2)
print(r)
r = s.combine(4, 3)
print(r)
r = s.combine(5, 4)
print(r)


class Solution(object):
    """
    Implementation similar to permutations
    Time    O(nCk)
    Space   O(nCk) due to the recrusion
    648 ms, faster than 39.65%
    """
    def combine(self, n, k):
        self.res = []
        self.dfs(n, 1, k, [])
        return self.res
    
    def dfs(self, n, start, k, chosen):
        if len(chosen) == k:
            self.res.append(chosen)
            return
        for i in range(start, n+1):
            self.dfs(n, i+1, k, chosen + [i])


s = Solution()

r = s.combine(4, 2)
print(r)
r = s.combine(4, 3)
print(r)
r = s.combine(5, 4)
print(r)
