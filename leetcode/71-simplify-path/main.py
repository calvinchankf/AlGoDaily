"""
    1st: stack
    - ugly draft version
    - put every substring (not '.' and '..') into a stack
    - when we see a '..', pop the stack
    - join the stack to return a result

    Time    O(N)
    Space   O(N)
    48 ms, faster than 7.40% 
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            if path[i] == '/':
                cur = ''
                j = i + 1
                while j < len(path) and path[j] != '/':
                    cur += path[j]
                    j += 1
                i = j
                if len(cur) > 0:
                    if cur == '..':
                        if len(stack) > 0:
                            stack.pop()
                    elif cur != '.':
                        stack.append(cur)
            elif i + 1 < len(path) and path[i] + path[i+1] == '..':
                i += 2
                if len(stack) > 0:
                    stack.pop()
            else:
                i += 1
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

print('-----')

"""
    2nd : stack
    - better version
    - put every substring (not '.' and '..') into a stack
    - when we see a '..', pop the stack
    - join the stack to return a result

    Time    O(N)
    Space   O(N)
    48 ms, faster than 7.40% 
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        cur = ''
        while i <= len(path):
            if (i < len(path) and path[i] == '/') or i == len(path):
                if len(cur) > 0:
                    if cur == '.':
                        pass
                    elif cur == '..':
                        if len(stack) > 0:
                            stack.pop()
                    else:
                        stack.append(cur)
                cur = ''
            else:
                cur += path[i]
            i += 1
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
