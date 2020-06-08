"""
    1st: recursion + math + hashtable
    - use recutsion to find out all the combinations(with length == 2)
    - find the gcd of any pair to simplified every fraction

    Time    O(nC2 logN)
    Space   O(nC2)
    580 ms, faster than 25.00%
"""


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        self.res = set()
        self.dfs([], n)
        return self.res

    def findGcd(self, a, b):
        if b == 0:
            return a
        return self.findGcd(b, a % b)

    def dfs(self, chosen: List[int], n: int):
        if len(chosen) == 2:
            a = chosen[0]
            b = chosen[1]
            gcd = self.findGcd(a, b)
            fraction = str(b//gcd) + '/' + str(a//gcd)
            self.res.add(fraction)
        elif len(chosen) < 2:
            for i in range(1, n + 1):
                if len(chosen) == 0:
                    self.dfs([i], n)
                elif i < chosen[0]:
                    self.dfs(chosen + [i], n)


"""
    2nd: iteration + math
    - optimze the 1st approach
    - since the length == 2 for every fraction, we can just do a nested forloop
    - find the gcd of any pair to simplified every fraction

    260 ms, faster than 50.00%
"""


class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        res = []
        for i in range(1, n):
            for j in range(i+1, n+1):
                if self.findGcd(i, j) == 1:
                    res.append(f'{i}/{j}')
        return res

    def findGcd(self, a, b):
        if b == 0:
            return a
        return self.findGcd(b, a % b)
