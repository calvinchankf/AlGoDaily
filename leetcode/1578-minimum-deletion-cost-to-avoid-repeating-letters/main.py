"""
    1st: sort
    - sort the cost for every group of consecutive charactors
    - in every group, sum up all of the costs expect the minimum one

    Time    O(NlogN)
    Space   O(N)
    1116 ms, faster than 100.00%
"""


class Solution(object):
    def minCost(self, s, cost):
        n = len(s)
        res = 0
        i = 0
        while i < n:
            cur = [cost[i]]
            j = i
            while j+1 < n and s[j+1] == s[i]:
                j += 1
                cur.append(cost[j])
            # print(i, cur)
            if len(cur) > 1:
                cur.sort()
                res += sum(cur[:-1])
            i = j + 1
        return res


s = Solution()

a = 'abaac'
b = [1, 2, 3, 4, 5]
print(s.minCost(a, b))

a = 'abc'
b = [1, 2, 3]
print(s.minCost(a, b))

a = 'aabaa'
b = [1, 2, 3, 4, 1]
print(s.minCost(a, b))

print('----')

a = 'aabaacc'
b = [1, 2, 3, 4, 1, 3, 4]
print(s.minCost(a, b))
