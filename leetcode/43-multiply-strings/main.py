"""
    see ./idea.jpg

    Time	O(MN)
	Space	O(M+N)
    188 ms, faster than 38.41%
"""


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        M, N = len(num1), len(num2)
        digits = (M + N) * [0]
        for i in range(M):
            for j in range(N):
                _i = M - i - 1
                _j = N - j - 1
                temp = int(num1[_i]) * int(num2[_j])
                digits[i+j] += temp % 10
                digits[i+j+1] += temp//10
        for i in range(len(digits)-1):
            carry = digits[i]//10
            digits[i] = digits[i] % 10
            digits[i+1] += carry
        digits.reverse()
        res = ''
        for i in range(len(digits)):
            if res == '' and digits[i] == 0:
                continue
            res += str(digits[i])
        return res


s = Solution()

a = '123'
b = '456'
print(s.multiply(a, b))

a = '123'
b = '56'
print(s.multiply(a, b))

a = "498828660196"
b = "840477629533"
print(s.multiply(a, b))

a = '0'
b = '456'
print(s.multiply(a, b))
