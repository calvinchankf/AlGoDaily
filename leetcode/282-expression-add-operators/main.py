"""
    0th: recursion
    LTE 13 / 20 test cases passed.
"""
class Solution(object):
    def addOperators(self, num, target):
        self.res = []
        self.dfs(num, target, '')
        return self.res
        
    def dfs(self, s, target, exp):
        if len(s) == 0:
            if len(exp) > 0 and eval(exp) == target:
                self.res.append(exp)
        for i in range(len(s)):
            sub = s[:i+1]
            num = int(sub)
            
            if str(num) != sub:
                break
            
            if len(exp) == 0:
                self.dfs(s[i+1:], target, sub)
            else:
                self.dfs(s[i+1:], target, exp + '+' + sub)
                self.dfs(s[i+1:], target, exp + '-' + sub)
                self.dfs(s[i+1:], target, exp + '*' + sub)



"""
    1st: recursion
    - using eval() at the bottom of the recursion is too slow, we can evaluation the total along the way
    - keep in mind that * has a higher priority

    e.g.1. 12 + 4 * 6
                ^ the sum up to this point = 16
    total = (16 - 4) + (4 * 6) = 36

    e.g.2. 12 - 4 * 6
                ^ the sum up to this point = 8
    total = (8 - (-4)) + (-4 * 6) = 12

    Therefore, for operrand *, nextTotal = total - prev + prev * num


    Time    O(N * 4^N), every charactor has 4 options(+, -, *, stringAppend)
    Space   O(N)
    936 ms, faster than 77.16%
"""
class Solution(object):
    def addOperators(self, num, target):
        self.res = []
        self.dfs(num, target, '', 0, None)
        return self.res
        
    def dfs(self, s, target, exp, total, prev):
        if len(s) == 0:
            if total == target:
                self.res.append(exp)
        for i in range(len(s)):
            sub = s[:i+1]
            num = int(sub)
            
            if str(num) != sub:
                break
            
            if len(exp) == 0:
                self.dfs(s[i+1:], target, sub, num, num)
            else:
                self.dfs(s[i+1:], target, exp + '+' + sub, total + num, num)
                self.dfs(s[i+1:], target, exp + '-' + sub, total - num, -num)
                self.dfs(s[i+1:], target, exp + '*' + sub, total - prev + prev * num, prev*num)