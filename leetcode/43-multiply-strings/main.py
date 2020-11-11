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
        M, N = len(num1), len(num2)
        nums = (M+N) * [0]
        num1 = num1[::-1]
        num2 = num2[::-1]
        for i in range(M):
            for j in range(N):
                p = int(num1[i]) * int(num2[j])
                nums[i+j] += p % 10
                nums[i+j+1] += p//10
        # for every slot, calculate the digit and put carry to the next slot
        carry = 0
        for i in range(len(nums)):
            d = (carry + nums[i]) % 10
            carry = (carry + nums[i])//10
            nums[i] = d
        # construct the result
        res = ''
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == 0 and res == '':  # ignore leading zeros
                continue
            res += str(nums[i])
        if res == '':
            return '0'
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
