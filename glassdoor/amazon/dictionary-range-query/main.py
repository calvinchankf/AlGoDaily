"""
    https://leetcode.com/discuss/interview-question/218805/Amazon-or-Phone-Screen-or-Dictionary-Range-Query

    Location: SF Bay Area

    Return the words from dictionary the range query.

    Example:

    Input: dict = ['apple', 'boy', 'cat', 'dog', 'element', 'zack', 'zill']

    Output:
    range("a", "z"); // returns  [apple, boy, cat, dog, element]
    range("ebc", "zas"); // returns [element, zack]
"""


class Solution(object):

    def __init__(self, dic):
        self.dic = sorted(dic)

    def wordsBetween(self, a, b):
        left = self.lowerBsearch(self.dic, a)
        right = self.upperBsearch(self.dic, b)
        print(left, right)
        return self.dic[left: right]

    def lowerBsearch(self, A, target):
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right) // 2
            if target <= A[mid]:
                right = mid
            else:
                left = mid + 1
        return left

    def upperBsearch(self, A, target):
        left = 0
        right = len(A)
        while left < right:
            mid = (left + right) // 2
            if target >= A[mid]:
                left = mid + 1
            else:
                right = mid
        return left


s = Solution(
    ['apple', 'boy', 'cat', 'dog', 'element', 'zack', 'zill']
)

a = 'a'
b = 'z'
print(s.wordsBetween(a, b))

a = 'ebc'
b = 'zas'
print(s.wordsBetween(a, b))
