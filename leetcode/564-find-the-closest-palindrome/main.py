"""
    1st: brute force

    Time    O(logN) length of digits of N
    Space   O(1)
    163 / 212 test cases passed.
"""


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        num = int(n)
        delta = 1
        while True:
            if self.isPalindrom(num-delta):
                return str(num-delta)
            if self.isPalindrom(num+delta):
                return str(num+delta)
            delta += 1

    def isPalindrom(self, n):
        s = str(n)
        return n == int(s[::-1])


"""
    2nd: very annoying math
    - we only need to consider 7 candidates

    e.g. "265755"
    candidates = [
        '99999', 
        '100001', 
        '264462',   264 + 462
        '265562',   265 + 562
        '266662',   266 + 662
        '999999', 
        '1000001'
    ]

    e.g. "200001"
    candidates = [
        '99999', 
        '100001', 
        '199991', 
        '200002', 
        '201102', 
        '999999', 
        '1000001'
    ]

    e.g. "20001"
    candidates = [
        '9999', 
        '10001', 
        '19991', 
        '20002', 
        '20102', 
        '99999', 
        '100001'
    ]

    ref:
    - https://leetcode.com/problems/find-the-closest-palindrome/discuss/102391/Python-Simple-with-Explanation

    Time    O(1)
    Space   O(1)
    16 ms, faster than 91.38%
"""


class Solution(object):
    def nearestPalindromic(self, S):
        K = len(S)  # 265755
        lowerbound = 10**(K-1)
        upperbound = 10**K
        candidates = []
        candidates.append(str(lowerbound-1))  # 99999
        candidates.append(str(lowerbound+1))  # 100001
        candidates.append(str(upperbound-1))  # 999999
        candidates.append(str(upperbound+1))  # 1000001

        firstHalf = S[:(K+1)//2]  # 265
        firstHalfNum = int(firstHalf)
        # 264, 265, 266
        for num in [firstHalfNum-1, firstHalfNum, firstHalfNum+1]:
            x = str(num)
            if K % 2 == 0:
                candidates.append(x + x[::-1])  # 264 + 462, ...etc
            else:
                suffix = x[:-1]
                candidates.append(x + suffix[::-1])

        res = None
        candidates.sort(key=lambda x: int(x))
        for cand in candidates:
            if cand == S:
                continue
            if res == None or abs(int(cand) - int(S)) < abs(int(res) - int(S)):
                res = cand
        return res
