"""
    2nd: upper bound binary search
    - since 1 <= x <= x^2 for all x > 0
    - we are going to search for a number that which sqaure is just right a bit larger than x

    e.g. 8
    1 2 3 4 5 6 7 8
    ^             ^

    1 2 3 4 5 6 7 8
    ^     ^

    1 2 3 4 5 6 7 8
        ^   ^

    1 2 3 4 5 6 7 8
        ^
    3^2 = 9 is larger than 8, therefore answer should be 3-1=2

    Time    O(logn)
    Space   O(1)
    28 ms, faster than 91.29%
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == x**2:
            return x
        left = 1
        right = x
        while left < right:
            mid = (left + right) // 2
            if x >= mid**2:
                left = mid + 1
            else:
                right = mid
        return left - 1


print(Solution().mySqrt(1))
print(Solution().mySqrt(4))
print(Solution().mySqrt(8))
print(Solution().mySqrt(100))
print(Solution().mySqrt(1587654567))

"""
    2nd approach: common binary search
    - if mid*mid == target, return mid
    - if no absolute value, the result must be the right(since right < left after iteration)
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == x*x:
            return x
        left = 1
        right = x
        while left <= right:
            mid = (left + right)//2
            if x < mid*mid:
                right = mid - 1
            elif x > mid*mid:
                left = mid + 1
            else:
                return mid
        return right
