"""
    1st approach: recursive dfs, avoid duplicate by using a hashtable

    it is hard to determind the Time Complexity, it depends on the input
    1012 ms, faster than 5.07%
    10apr2019
"""


class Solution(object):

    def __init__(self):
        self.result = {}

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs(candidates, target, [], "", 0)
        res = []
        for key in self.result:
            res.append(self.result[key])
        return res

    def dfs(self, candidates, target, path, pathStr, total):
        if total == target:
            self.result[pathStr] = path
        elif total < target:
            for i in range(len(candidates)):
                can = candidates[i]
                self.dfs(candidates[i+1:], target, path +
                         [can], pathStr+","+str(can), total+can)


Solution()

a = [10, 1, 2, 7, 6, 1, 5]
print(s.combinationSum(a, 8))

a = [2, 5, 2, 1, 2]
print(s.combinationSum(a, 5))

a = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29,
     24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12]
print(s.combinationSum(a, 27))

print("-----")

"""
    2nd approach: simialar to lc90(subset 2)

    it is hard to determind the Time Complexity, it depends on the input
    108 ms, faster than 32.29%
    17june2019
"""


class Solution(object):
    def __init__(self):
        self.result = []

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        self.dfs(candidates, target, [], 0)
        return self.result

    def dfs(self, candidates, target, path, total):
        if total == target:
            self.result.append(path)
        elif total < target:
            for i in range(len(candidates)):
                can = candidates[i]
                if i == 0 or candidates[i-1] != candidates[i]:
                    self.dfs(candidates[i+1:], target, path+[can], total+can)


s = Solution()


a = [10, 1, 2, 7, 6, 1, 5]
print(s.combinationSum(a, 8))

a = [2, 5, 2, 1, 2]
print(s.combinationSum(a, 5))

a = [14, 6, 25, 9, 30, 20, 33, 34, 28, 30, 16, 12, 31, 9, 9, 12, 34, 16, 25, 32, 8, 7, 30, 12, 33, 20, 21, 29,
     24, 17, 27, 34, 11, 17, 30, 6, 32, 21, 27, 17, 16, 8, 24, 12, 12, 28, 11, 33, 10, 32, 22, 13, 34, 18, 12]
print(s.combinationSum(a, 27))
