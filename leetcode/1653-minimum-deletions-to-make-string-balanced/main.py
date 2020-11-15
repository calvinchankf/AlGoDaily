"""
    The intuition is that, let's say you have "aababbab"

    indices of all the 'a'
    A = [0,1,3,6]
    indices of all the 'b'
    B = [2,4,5,7]
    We want to delete the tail of A or the head of B, so that all the numbers in A are larger than B.
    i.e. A = [0,1,3], B = [4,5,7]
    Since the indices are sorted, we can loop over A and binary search a point where B[j] > A[i] in B

    Time    O(N + AlogB) i.e. A + B = N
    Space   O(N)
    3816 ms, faster than 100.00%
"""


class Solution(object):
    def minimumDeletions(self, s):
        A = [-1]  # consider 'bbba', u want to delete the a instead of bbb
        B = []
        for i in range(len(s)):
            c = s[i]
            if c == 'a':
                A.append(i)
            else:
                B.append(i)
        res = 2**31 - 1
        for i in range(len(A)):
            a = A[i]
            j = self.upperBoundbsearch(B, a)
            toDeleteInA = len(A) - i - 1
            toDeleteInB = j
            charsToDelete = toDeleteInA + toDeleteInB
            res = min(res, charsToDelete)
        if res == 2**31 - 1:  # or sys.maxsize / 'inf', whatever
            return 0
        return res

    # or python bisect right, whatever
    def upperBoundbsearch(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution()

a = 'aababbab'
print(s.minimumDeletions(a))

a = 'bbaaaaabb'
print(s.minimumDeletions(a))

a = 'bbaa'
print(s.minimumDeletions(a))

a = 'b'
print(s.minimumDeletions(a))

a = "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
print(s.minimumDeletions(a))

# should delete a instead of bbb, so the answer is 1
a = "bbba"
print(s.minimumDeletions(a))
