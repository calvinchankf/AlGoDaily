"""
    1st: math
    - add the fraction one by one using lcm
    - calculate the final result using gcd

    Time    O(NlogX) N = number of fractions, X = largest value of a denominator
    Space   O(N)
    28 ms, faster than 80.90%
"""


class Solution:
    def fractionAddition(self, expression: str) -> str:
        if len(expression) == 0:
            return '0/1'
        fractions = expression.replace("+", " +").replace("-", " -").split()
        if len(fractions) == 1:
            return fractions[0]

        total = [0, 1]
        for f in fractions:
            a, b = f.split('/')
            a, b = int(a), int(b)

            parent = self.lcm(total[1], b)
            child = total[0] * parent // total[1] + a * parent // b
            total = [child, parent]

        if total[0] == 0:
            return "0/1"
        _gcd = self.gcd(child, parent)
        A = child // _gcd
        B = parent // _gcd
        return '%d/%d' % (A, B)

    def lcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return a * b // self.gcd(a, b)

    def gcd(self, a, b):
        if b == 0:
            return a
        return self.gcd(b, a % b)
