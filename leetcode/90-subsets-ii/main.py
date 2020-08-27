"""
    1st approach: recursion + hashtable

    Recursive DFS using hashtables to avoid duplicates, see ./idea.jpeg
    Method similar to what I did for Permutation II

    Time    O(2^n) worst
    Space   O(2^n) recursion
    24 ms, faster than 100.00%
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        self.result.append(path)
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen[nums[i]] = True
            self.dfs(nums[i+1:], path+[nums[i]])


"""
    2nd approach: recursion
    - similar to 1st dont need to use a hashtable(since the array is sorted)
    
    Time    O(2^n) worst
    Space   O(2^n) recursion
    24 ms, faster than 100.00%
"""


class Solution(object):

    def __init__(self):
        self.result = []

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, path):
        self.result.append(path)
        for i in range(len(nums)):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                self.dfs(nums[i+1:], path+[nums[i]])


print(Solution().subsetsWithDup([1, 2, 2, 3]))

"""
    Iteratively append the next item to calculated items with a constraint
    e.g. [1,2,2,3]
    []
    [],[1]                                                                      <- len_of_distinct = 1 during computation
    [],[1],[2],[1,2]                                                            <- len_of_distinct = 2 during computation
    [],[1],[2],[1,2],[2,2],[1,2,2]                                              <- len_of_distinct = 2 during computation
    [],[1],[2],[1,2],[2,2],[1,2,2],[3],[1,3],[2,3],[1,2,3],[2,2,3],[1,2,2,3]    <- len_of_distinct = 6 during computation
    Time    O(2^n) the worst. the actaul time depends on the number of duplicates
    Space   O(1)
    beats   13.12%
    ref: https://leetcode.com/problems/subsets-ii/discuss/30145/Accepted-java-iterative-solution
"""


class Solution1(object):
    def subsetsWithDup(self, nums):
        nums = sorted(nums)
        res = [[]]
        len_of_distinct = 1  # the len of previous result which is generated by distinct numbers
        for i in range(len(nums)):
            num = nums[i]
            size = len(res)
            if i > 0 and num != nums[i-1]:
                len_of_distinct = size
            for j in range(size-len_of_distinct, size):
                res += [res[j]+[num]]
        return res


print(Solution1().subsetsWithDup([1, 2, 2, 3]))
