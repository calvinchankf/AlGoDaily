"""
    Find the greatest common divisor between 2 numbers

    Questions:
    - negtive numbers?
    - zeros?
"""


"""
    common way:

    findGcd(100, 40)
    
    -> 40, 100%40
    findGcd(40, 20)
    
    -> 40, 40%20
    findGcd(20, 0)

    so gcd = 20
"""


def findGcd(a, b):
    if b == 0:
        return a
    return findGcd(b, a % b)


class Solution(object):
    def gcd(self, arr):
        """
            Euclidian Algorithm
            dividend = divisor*quotient+remainder
            100=45*2+10
            45=10*4+5
            10=5*2+0
            in the last row, the remainder is 0, therefore 5 is the common divisor

            Time    O(n)
            Space   O(1)

            amcat amazon: passed 13 out of 13 testcases
        """
        if len(arr) == 0:
            return 0
        res = arr[0]
        for i in range(1, len(arr)):
            res = self.findGcd(res, arr[i])
        return res

    def findGcd(self, a, b):
        if a == 0 or b == 0:
            return 0
        dividend = max(a, b)
        divisor = min(a, b)
        while divisor != 0:
            remainder = dividend % divisor
            if remainder == 0:
                break
            dividend = divisor
            divisor = remainder
        return divisor


print(Solution().gcd([1206, 3768, 366]))
print(Solution().gcd(
    [2 * 11 * 13 * 17 * 19 * 23, 13 * 17 * 23 * 3, 2 * 13 * 17]))
print(Solution().gcd([17, 19, 11]))
print(Solution().gcd([-1701, 3768]))  # ?
print(Solution().gcd([1701, -3768]))  # ?
print(Solution().gcd([-1701, -3768]))  # ?
print(Solution().gcd([1, 2]))
print(Solution().gcd([]))
