"""
    2nd: math + backtracking
    - learned from others

    e.g. 331
    = 1 + 3^2 + 3^4 + 3^5
    = 1 + 3^2( 1 + 3^2 + 3^3)
    = 1 + 3^2( 1 + 3^2( 1 + 3^1 ) )

    ref:
    - https://leetcode.com/problems/check-if-number-is-a-sum-of-powers-of-three/discuss/1097105/C%2B%2BJava-Backtracking-and-Math

    Time    O(sqrt of N base 3)
    Space   O(sqrt of N base 3)
    28 ms, faster than 100.00%
"""
class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        if n % 3 == 0:
            return self.checkPowersOfThree(n//3)
        if n % 3 == 1:
            return self.checkPowersOfThree((n-1)//3)
        return False