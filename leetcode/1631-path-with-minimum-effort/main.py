from typing import List

"""
    1st: kind of brute force with backtracking

    Time    < O(3^N)
    LTE
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        return self.dfs(heights, 0, 0, set(), heights[0][0])
    
    def dfs(self, heights, i, j, hs, prev):
        R, C = len(heights), len(heights[0])
        if i < 0 or i == R or j < 0 or j == C:
            return 2**31
        if i == R - 1 and j == C - 1:
            return abs(heights[i][j] - prev)
        key = (i, j)
        if key in hs:
            return 2*31
        hs.add(key)
        up = self.dfs(heights, i-1, j, hs, heights[i][j])
        down = self.dfs(heights, i+1, j, hs, heights[i][j])
        left = self.dfs(heights, i, j-1, hs, heights[i][j])
        right = self.dfs(heights, i, j+1, hs, heights[i][j])
        hs.remove(key)
        cur = abs(heights[i][j] - prev)
        return max(min(up, down, left, right), cur)

s = Solution()

a = [[1,2,2],[3,8,2],[5,3,5]]
print(s.minimumEffortPath(a))

a = [[1,2,3],[3,8,4],[5,3,5]]
print(s.minimumEffortPath(a))

a = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(s.minimumEffortPath(a))

a = [[1,10,6,7,9,10,4,9]]
print(s.minimumEffortPath(a))

# a = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
# print(s.minimumEffortPath(a))

print("-----")

"""
    2nd: binary search + BFS
    - it is not appropriate to use DP because it goes 4 directions
    - binary search the threshold 

    Time    O( RC log10**6)
    Space   O(1)
    5604 ms, faster than 50.00%
"""
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        left = 0
        right = 10**6
        while left < right:
            mid = (left + right) // 2
            if self.bfs(heights, mid):
                right = mid
            else:
                left = mid + 1
        return left
    
    def bfs(self, heights, limit):
        R, C = len(heights), len(heights[0])
        seen = set()
        q = [(0, 0, heights[0][0])]
        while len(q) > 0:
            i, j, prev = q.pop(0)
            if i < 0 or i == R or j < 0 or j == C:
                continue
            
            h = heights[i][j]
            if abs(h - prev) > limit:
                continue
            
            key = (i, j)
            if key in seen:
                continue
            seen.add(key)

            if i == R - 1 and j == C - 1:
                return True
            
            q.append((i-1, j, h))
            q.append((i+1, j, h))
            q.append((i, j-1, h))
            q.append((i, j+1, h))
        return False

s = Solution()

a = [[1,2,2],[3,8,2],[5,3,5]]
print(s.minimumEffortPath(a))

a = [[1,2,3],[3,8,4],[5,3,5]]
print(s.minimumEffortPath(a))

a = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
print(s.minimumEffortPath(a))

a = [[1,10,6,7,9,10,4,9]]
print(s.minimumEffortPath(a))

a = [[4,3,4,10,5,5,9,2],[10,8,2,10,9,7,5,6],[5,8,10,10,10,7,4,2],[5,1,3,1,1,3,1,9],[6,4,10,6,10,9,4,6]]
print(s.minimumEffortPath(a))