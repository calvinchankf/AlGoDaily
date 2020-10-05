"""
    1st: math, dynamic programming
    
    day[1] = k
    day[2] = k * k
    day[i>2] = (day[i-1] + day[i-2]) * (k - 1)

    on day i, there are 2 cases

    case 1:
    dont form duplicate combination with the previous day, day[i-1] * (k-1)

    case 2:
    form duplicate combination with the day before previous day, day[i-2] * (k-1)

    ref:
    - https://leetcode.com/problems/paint-fence/discuss/71151/Lucas-formula-maybe-%22O(1)%22-and-34-liners
    - https://www.dazhuanlan.com/2020/01/04/5e10205cdf382/

    Time    O(N)
    Space   O(N)
    28 ms, faster than 60.43%
"""


class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return k
        day = n * [0]
        day[0] = k
        day[1] = k*k
        for i in range(2, n):
            day[i] = (day[i-2] + day[i-1]) * (k-1)
        return day[n-1]

"""
    2nd: recursion + hashtable
    - similar to lc70, 509

    Time    O(N)
    Space   O(N)
    12 ms, faster than 97.42%
"""
class Solution(object):
    def numWays(self, n, k):
        return self.f(n, k, {})
        
    def f(self, n, k, ht):
        if n == 0:
            return 0
        if n == 1:
            return k
        if n == 2:
            return k*k
        if n in ht:
            return ht[n]
        total = (self.f(n-1, k, ht) + self.f(n-2, k, ht)) * (k-1)
        ht[n] = total
        return ht[n]