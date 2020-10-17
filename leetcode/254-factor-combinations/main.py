import math

"""
    1st approach: recursion
    - for every number from 2 to n-1, if it can divide the current number, it is one of the factors
    
    e.g. 252

    252%2 = 0
    252%3 = 0
    252%4 != 0
    ....

    Time    I am not sure
    Space   I am not sure
    LTE
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.dfs(n, 2, [])
        return self.res

    def dfs(self, num, start, path):
        if num == 1:
            if len(path) > 1:
                self.res.append(path)
            return
        for i in range(start, num+1):
            if num % i == 0:
                self.dfs(num//i, i, path+[i])


print(Solution().getFactors(252))

print("-----")

"""
    2nd approach: recursion
    - for every number from 2 to n-1, if it can divide the current number, it is one of the factors
    - the diffrence from the 1st approach is THAT all prime factors must be <= sqrt of a number 
    
    e.g. 252

    252%2 = 0
    252%3 = 0
    252%4 != 0
    ....

    Time    I am not sure
    Space   I am not sure
    16 ms, faster than 92.01%
"""


class Solution(object):

    def __init__(self):
        self.res = []

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.dfs(n, 2, [])
        return self.res

    def dfs(self, num, start, path):
        # the num never gets down to 1, because we use sqrt to factorize
        # e.g. 9 => 3 * 3 when it comes to 3, since sqrt(3) = 1, we cant factorize any more
        if len(path) > 0:
            self.res.append(path+[num])
        n = int(math.sqrt(num))
        for i in range(start, n+1):
            if num % i == 0:
                self.dfs(num//i, i, path+[i])


print(Solution().getFactors(252))

print("-----")

"""
    3rd: factorization + lc39

    Time    ???
    Space   ???
    20 ms, faster than 80.77%
"""
class Solution(object):
    def getFactors(self, n):
        if n <= 1:
            return []
        nums = sorted(self.genFactors(n))
        self.res = []
        self.dfs(nums, [], 1, n)
        return self.res
        
    def genFactors(self, n):
        r = int(math.sqrt(n))
        res = set()
        for i in range(2, r+1):
            if n%i == 0:
                res.add(i)
                res.add(n//i)
        return res

    
    def dfs(self, nums, chosen, total, n):
        if total == n:
            self.res.append(chosen)
            return
        if total > n:
            return
        for i in range(len(nums)):
            if len(chosen) == 0 or chosen[-1] <= nums[i]:
                self.dfs(nums, chosen + [nums[i]], total * nums[i], n)