class Solution(object):
    """
    Recursive DFS

    e.g. [1,2,3,4]

                                            ()
                    (1)                     (2)                 (3)           (4)
    (1,2)               (1,3) (1,4)         (2,3) (2,4)         (3,4)
    (1,2,3) (1,2,4)     (1,3,4)             (2,3,4)
    (1,2,3,4)

    total = 16

    explanation:
    in the recursion tree, for each number, we can either include or exclude it the result, therefore we have 2^n options in total

    Time    O(2^n)
    Space   O(2^n) recursion
    beats   35.29%
    """

    def __init__(self):
        self.result = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.dfs(nums, [])
        return self.result

    def dfs(self, nums, chosen):
        self.result.append(chosen)
        for i in range(len(nums)):
            self.dfs(nums[i+1:], chosen+[nums[i]])


s = Solution()

print(s.subsets([1, 2, 3]))
print(s.subsets([1, 2, 3, 4]))

print("-----")


class Solution(object):
    """
    Iterative DFS
    Time    O(2^n)
    Space   O(2^n)
    beats   3.67%
    """

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        stack = [(nums, [])]  # array of tuples (nums, path)
        while len(stack) > 0:
            pop = stack.pop()
            arr = pop[0]
            path = pop[1]
            result.append(path)
            for i in range(len(arr)):
                stack.append((arr[i+1:], path+[arr[i]]))
        return result


s = Solution()

print(s.subsets([1, 2, 3]))
print(s.subsets([1, 2, 3, 4]))

print("-----")


class Solution(object):
    """
    Recursive DFS
    - the way similar to lc416
    - for each number, we can either include or exclude it the result, therefore we have 2^n options in total

    Time    O(2^n)
    Space   O(2^n) recursion tree
    24 ms, faster than 79.31%
    """

    def __init__(self):
        self.res = {}

    def subsets(self, nums):
        self.recur(nums, [], 0)
        keys = []
        for x in self.res:
            keys.append(list(x))
        return keys

    def recur(self, nums, chosen, curIdx):
        # there might be duplicate combinations
        key = tuple(chosen)
        self.res[key] = chosen
        if curIdx >= len(nums):
            return
        # choose or not choose
        self.recur(nums, chosen + [nums[curIdx]], curIdx+1)
        self.recur(nums, chosen[:], curIdx+1)


s = Solution()

print(s.subsets([1, 2, 3]))
print(s.subsets([1, 2, 3, 4]))

print("-----")


class Solution(object):
    """
    Iteratively append the next item to calculated items
    e.g. [1,2,3]
    []
    [],[1]
    [],[1],[2],[1,2]
    [],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]
    Time    O(2^n)
    Space   O(2^n)
    beats   35.29%
    """

    def subsets(self, nums):
        res = [[]]
        for num in nums:
            n = len(res)
            for i in range(n):
                res += [res[i]+[num]]
            # the above 3 lines can be reduced as res += [item+[num] for item in res] # but only beats 15.25%
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
print(s.subsets([1, 2, 3, 4]))
