"""
    1st: recursion
    - similar to lc463, lc1254
    - when recursion reaches to boundary, return -1, else return area(sum of 1 nearby)
    
    Time    O(RC)
    Space   O(RC)
    792 ms, faster than 9.94%
"""


class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        visited = set()
        result = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1 and (i, j) not in visited:
                    temp = self.dfs(A, visited, i, j)
                    if temp > 0:
                        result += temp
        return result

    def dfs(self, A, visited, i, j):
        if i < 0 or i == len(A) or j < 0 or j == len(A[0]):
            return -1
        if A[i][j] == 0:
            return 0
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        total = 1
        top = self.dfs(A, visited, i-1, j)
        bottom = self.dfs(A, visited, i+1, j)
        left = self.dfs(A, visited, i, j-1)
        right = self.dfs(A, visited, i, j+1)
        if top == -1 or bottom == -1 or left == -1 or right == -1:
            return -1
        return total + top + bottom + left + right


"""
    2nd: BFS
    - mutate all the cells of an island which touches the boundary
    - count the remaining ones 
    
    Time    O(2RC)
    Space   O(RC)
    572 ms, faster than 32.75%
"""


class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        visited = set()
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i == 0 or j == 0 or i == len(A)-1 or j == len(A[0])-1) and (i, j) not in visited:
                    self.bfs(A, i, j, visited)
        res = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    res += 1
        return res

    def bfs(self, A, x, y, visited):
        q = [(x, y)]
        while len(q) > 0:
            i, j = q.pop(0)
            if i < 0 or i == len(A) or j < 0 or j == len(A[0]):
                continue
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if A[i][j] == 1:
                A[i][j] = 0
                q.append((i-1, j))
                q.append((i+1, j))
                q.append((i, j-1))
                q.append((i, j+1))
