"""
    1st : stack
    - better version
    - put every substring (not '.' and '..') into a stack
    - when we see a '..', pop the stack
    - join the stack to return a result

    Time    O(N)
    Space   O(N)
    32 ms, faster than 69.75%
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path[1:]
        stack = []
        arr = path.split('/')
        for w in arr:
            if w == '..':
                if len(stack) > 0:
                    stack.pop()
            elif w == '' or w == '.':
                continue
            else:
                stack.append(w)
        return '/' + '/'.join(stack)


s = Solution()
print(s.simplifyPath('/home/'))
print(s.simplifyPath('/../'))
print(s.simplifyPath('/home//foo/'))
print(s.simplifyPath('/a/./b/../../c/'))
print(s.simplifyPath('/a/../../b/../c//.//'))
print(s.simplifyPath('/a//b////c/d//././/..'))
print(s.simplifyPath('/...'))
print(s.simplifyPath('/..'))
