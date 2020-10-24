"""
    1st approach
	- 6 = 3*2 = 2+2+2, 7 = 3*2 = 2+2+2+1
	- be careful of the negative
	- be careful of the boundaries
	Time		O(quotient)
	Space		O(1)
	
    LTE but AC in golang?!?!
	18jun2019
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            raise ValueError("divisor cannot be 0")
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1

        if dividend < 0:
            dividend = -dividend

        if divisor < 0:
            divisor = -divisor

        res = 0
        while dividend >= divisor:
            dividend -= divisor
            res += 1

        res = res * sign

        if res < -(2**31):
            return -(2**31)
        elif res > (2**31)-1:
            return (2**31)-1

        return res

s = Solution()

a = 32
b = 3
print(s.divide(a, b))

a = 91
b = 3
print(s.divide(a, b))

a = -2147483648
b = -1
# print(s.divide(a, b))

print('------')

"""
    2nd approach: bitop
    - the 1st approach is too slow, because it approaches the quotient one divisor by one divisor
    - we can speed up the the speed by using the fact that every number is a binarian 2^0 + 2^1 + 2^2 + ....
    - it means that...
        e.g. 32/3 = 10
        3*10 = 3*(1 * 2^3 + 0 * 2^2 + 1 * 2^1 + 0 * 2^0)
                  8         0         2         0
    - so how to find that number?
        lets find the most significant bit
        e.g.
        dvd / divisor
        32  / 3
        -------
              3 * 1 = 3
              3 * 2 = 6
              3 * 4 = 12
              3 * 8 = 24
              3 * 16= 48 <- bigger than dvd(32) now, add 2^3 to result, result += 8. next dvd = 32 - 24 = 8
        8 / 3
        -----
            3 * 1 = 3
            3 * 2 = 6
            3 * 4 = 12 <- bigger than dvd(8) now, add 2^1 to result, result += 2. next dvd = 8 - 6 = 2
        2 / 3
        -----
            divisor > dvd, no operation
        
        so the result = 8 + 2 = 10

    ref:
    - https://www.youtube.com/watch?v=uD1Cw1JbD8E

    Time    O(logn)
    Space   O(1)
    20 ms, faster than 78.71%
"""


class Solution:
    def divide(self, dividend, divisor):

        sign = 1 if (dividend < 0) == (divisor < 0) else -1
        dividend = abs(dividend)
        divisor = abs(divisor)

        res = 0
        while divisor <= dividend:
            temp = divisor
            significant = 1
            while temp <= dividend:
                temp <<= 1  # multiply by 2
                significant <<= 1  # go to the next significant bit
            # after the while loop, we get the number that its just larget than dividend
            res += significant >> 1  # res += significant/2
            dividend -= temp >> 1  # dividend -= temp/2

        res = res * sign

        if res < -(2**31):
            return -(2**31)
        elif res > (2**31)-1:
            return (2**31)-1

        return res

s = Solution()

a = 32
b = 3
print(s.divide(a, b))

a = 91
b = 3
print(s.divide(a, b))

a = -2147483648
b = -1
print(s.divide(a, b))

print("-----")

"""
    3rd: binary search
    - the best way for interviews to tackle this problem

    Time    O(logN)
    Space   O(1)
    36 ms, faster than 45.66%
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            sign = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        left = -(2**31)
        right = 2**31
        res = None
        while left <= right:
            mid = (left + right) // 2
            if dividend < mid * divisor:
                right = mid - 1 
            elif dividend > mid * divisor:
                left = mid + 1
            else:
                res = mid * sign
                break
        if res == None:
            res = right * sign
        
        if res < -(2**31):
            return -(2**31)
        elif res > (2**31)-1:
            return (2**31)-1

        return res

s = Solution()

a = 32
b = 3
print(s.divide(a, b))

a = 91
b = 3
print(s.divide(a, b))

a = -2147483648
b = -1
print(s.divide(a, b))