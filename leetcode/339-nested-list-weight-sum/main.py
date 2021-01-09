"""
    1st approach: recursive dfs

    Time  O(N)
    Space O(H)
    12 ms, faster than 99.88%
"""


class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        return self.dfs(nestedList, 1)

    def dfs(self, arr, depth):
        res = 0
        for x in arr:
            if x.isInteger():
                res += depth * x.getInteger()
            else:
                res += self.dfs(x.getList(), depth+1)
        return res


"""
    2nd approach: iterative DFS

    Time  O(N)
    Space O(H)
    20 ms, faster than 83.54%
"""


class Solution(object):

    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int
        """
        result = 0
        stack = []
        stack.append((nestedList, 1))
        while len(stack) > 0:
            arr, depth = stack.pop()
            for x in arr:
                if x.isInteger():
                    result += depth * x.getInteger()
                else:
                    stack.append((x.getList(), depth + 1))
        return result


"""
    3rd: BFS
    
    Time  O(n)
    Space O(h)
    28 ms, faster than 84.90%
"""


class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        total = 0
        q = []
        for x in nestedList:
            q.append((x, 1))
        while len(q) > 0:
            x, d = q.pop(0)
            if x.isInteger():
                total += x.getInteger() * d
            else:
                for child in x.getList():
                    q.append((child, d + 1))
        return total
