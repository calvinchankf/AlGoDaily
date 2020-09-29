"""
    questions to ask:
    - will there be zero? no
    - will there to duplicate numbers? no
"""


class Solution(object):
    """
    1st attempt:
    - iterative bottom-up dynamic programming approch
    - use a hashtable to avoid duplicates
    e.g. candidates = [2,3,5], target = 8
    f[0] = []
    f[1] = []
    f[2] = [[2]]
    f[3] = [[3]]
    f[4] = [[2,2]]
    f[5] = [[2,3],[5]]
    f[6] = [[2,2,2],[3,3]]
    f[7] = [[2,2,3],[2,5]]
    f[8] = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    beats 15.56%
    """

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(target+1):
            result.append([])
        for i in range(target+1):
            future_result = []
            seen = {}
            for candidate in candidates:
                cur = i - candidate
                if cur < 0:
                    continue
                that_results = result[cur]
                if len(that_results) == 0 and cur == 0:
                    future_result.append([candidate])
                else:
                    for that_result in that_results:
                        temp = that_result + [candidate]
                        temp = sorted(temp)
                        key = "".join(str(n) for n in temp)
                        if key in seen:
                            continue
                        seen[key] = True
                        future_result.append(temp)

            result[i] = future_result

        return result[target]


s = Solution()

print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([1, 2, 3, 4], 15))
print("------------------------------")


class Solution(object):
    """
    2nd approach: recursive dfs, avoid duplicate by considering the candidates which are >= num
    beats 76.61%
    """

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

    def dfs(self, candidates, target, path, from_idx):
        if target == 0:
            self.result.append(path)
            return
        for i in range(from_idx, len(candidates)):
            if target < candidates[i]:
                return
            can = candidates[i]
            self.dfs(candidates, target-can, path+[can], i)


s = Solution()

print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([1, 2, 3, 4], 15))
print("------------------------------")


class Solution(object):
    """
    2nd approach: recursive dfs, avoid duplicate by considering the candidates which are >= num
    144 ms, faster than 14.76%
    """

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
                if len(path) == 0 or path[-1] <= can:
                    self.dfs(candidates, target, path+[can], total+can)


s = Solution()

print(s.combinationSum([2, 3, 5], 8))
print(s.combinationSum([2, 3, 6, 7], 7))
print(s.combinationSum([1, 2, 3, 4], 15))
print("------------------------------")
