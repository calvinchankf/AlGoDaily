"""
    backtracking
    - learned from others

    idea: 
    - build the tree from the 1st digit
    - in each recursion, explore the legit posibilities and then try the next digit

    ref:
    - https://leetcode.com/problems/beautiful-arrangement/solution/

    Time    O(K) < O(N!) K = number of valid permutations
    Space   O(N)
    1524 ms, faster than 46.33%
"""


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        seen = set()
        self.count = 0
        self.backtracking(N, 1, seen)
        return self.count

    def backtracking(self, N, idx, seen):
        if idx > N:
            self.count += 1
        for num in range(1, N+1):
            if num in seen:
                continue
            if num % idx == 0 or idx % num == 0:
                seen.add(num)
                self.backtracking(N, idx + 1, seen)
                seen.remove(num)
