"""
    1st: hashtable

    Time    O(N + R + N^2R)
    Space   O(R)
    800 ms, faster than 40.00%
"""
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        g = {}
        for i in range(n):
            g.append([])
        for a, b in roads:
            g[a].append((a, b))
            g[b].append((a ,b))
        
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                s = set(g[i] + g[j])
                res = max(res, len(s))
        return res

s = Solution()

a = 4
b = [[0,1],[0,3],[1,2],[1,3]]
print(s.maximalNetworkRank(a, b))

a = 5
b = [[0,1],[0,3],[1,2],[1,3],[2,3],[2,4]]
print(s.maximalNetworkRank(a, b))

a = 8
b = [[0,1],[1,2],[2,3],[2,4],[5,6],[5,7]]
print(s.maximalNetworkRank(a, b))