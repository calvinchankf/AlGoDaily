"""
    1st: stack
    - similar to lc921
    - the trick is to replace )) to ], the reason is we only care about consecutive ))

    ref:
    https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/discuss/780221/Python-Simple-and-Fast-or-Time-O(n)-or-Space-O(1)

    Time    O(2N)
    Space   O(N)
    152 ms, faster than 100.00% 
"""


class Solution:
    def minInsertions(self, s: str) -> int:
        count = 0
        s = s.replace('))', ']')
        stack = []

        for c in s:
            if c == '(':
                stack.append(c)
            else:
                if len(stack) > 0:
                    # match: there is/are open(s) and c = either ) or ]
                    stack.pop()
                    if c == ')':
                        count += 1
                else:
                    # No Matching ( for ) or ))
                    # For an unmatched ) you need to add 2 chars to get ())
                    # For an unmatched )) you need to add 1 char to get ())
                    if c == ')':
                        count += 2
                    elif c == ']':
                        count += 1

        return count + len(stack) * 2
