"""
    1st approach: 2 stacks

    - 1st stack for counts
    - 2nd stack for substrings

    e.g. ab2[c3[de]]f

    when it comes to 2[
    cntStack = [2]
    strStack = ['ab', '']

    when it comes to 3[
    cntStack = [2, 3]
    strStack = ['ab', 'c', '']

    when it comes to the character before 1st ], 
    cntStack = [2, 3]
    strStack = ['ab', 'c', 'de']
    
    when it comes to 1st ], multiply 3 with 'de' and append to 'c'
    cntStack = [2]
    strStack = ['ab', 'cdedede']

    when it comes to 2nd ], , multiply 2 with 'cdedede' and append to 'abc'
    cntStack = []
    strStack = ['abcdededecdedede']

    when it comes to f
    cntStack = []
    strStack = ['abcdededecdededef']

    Time    O(n)
    Space   O(n)
    20 ms, faster than 77.65%
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        cntStack = []
        strStack = [""]
        num = 0
        for c in s:
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                cntStack.append(num)
                num = 0
                strStack.append("")
            elif c == ']':
                cnt = cntStack.pop()
                cur = strStack.pop()
                temp = cnt * cur
                strStack[-1] += temp
            else:
                strStack[-1] += c
        return strStack.pop()


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("3[a12[c]]"))

print("-----")

"""
    2nd approach: recursion

    Time    O(n)
    Space   O(n)
    20 ms, faster than 65.98%
"""


class Solution(object):
    def decodeString(self, s):
        q = [c for c in s]
        return self.helper(q)

    def helper(self, q):
        num = 0
        res = ''
        while len(q) > 0:
            c = q.pop(0)
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == '[':
                res += self.helper(q) * num
                num = 0
            elif c == ']':
                return res
            else:
                res += c
        return res


print(Solution().decodeString("3[a]2[bc]"))
print(Solution().decodeString("3[a2[c]]"))
print(Solution().decodeString("2[abc]3[cd]ef"))
print(Solution().decodeString("3[a12[c]]"))
