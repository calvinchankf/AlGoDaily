"""
    1st: top-down recursive
	- use a hashtable to avoid redundant calculation
	
    Time O(n)		duplicates are avoided so only the unseen numbers go through the calculations
	Space O(2n)	    n for hashtable, n for recursive callstack
	12 ms, faster than 98.77%
"""


class Solution(object):

    def fib(self, N):
        return self.f(N, {})
        
    def f(self, n, ht):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n in ht:
            return ht[n]
        fn = self.f(n-1, ht) + self.f(n-2, ht)
        ht[n] = fn
        return fn


print(Solution().fib(0))
print(Solution().fib(1))
print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
print(Solution().fib(13))
print(Solution().fib(40))

print("-----")

"""
    2nd: bottom-up iterative

	Time 	O(n) iterate from 1 to N
	Space	O(n) for the array
	0ms beats 100%
"""


class Solution(object):

    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        dp = [0, 1]
        for i in range(2, N+1):
            dp.append(dp[i-1] + dp[i-2])
        return dp[N]


print(Solution().fib(0))
print(Solution().fib(1))
print(Solution().fib(2))
print(Solution().fib(3))
print(Solution().fib(4))
print(Solution().fib(13))
print(Solution().fib(40))
