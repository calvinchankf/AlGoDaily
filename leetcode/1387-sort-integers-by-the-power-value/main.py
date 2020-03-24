"""
    1st: recursion + hashtable
    - classic dynamic programming question

    Time    O(N + NlogN)
    Space   O(N)
    192 ms, faster than 75.90%
"""


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.ht = {}
        self.arr = []
        for num in range(lo, hi+1):
            steps = self.dfs(num)
            self.arr.append((steps, num))
        self.arr.sort()
        return self.arr[k-1][1]

    def dfs(self, n):
        if n == 1:
            return 0
        if n in self.ht:
            return self.ht[n]
        if n % 2 == 0:
            temp = self.dfs(n//2)+1
            self.ht[n] = temp
            return temp
        temp = self.dfs(3*n+1)+1
        self.ht[n] = temp
        return temp


s = Solution()
print(s.getKth(12, 15, 2))
print(s.getKth(1, 1, 1))
print(s.getKth(7, 11, 4))
print(s.getKth(10, 20, 5))
print(s.getKth(1, 1000, 777))
