"""
    1st: 2 pointers

    Time    O(N)
    Space   O(1)
    116 ms, faster than 100.00%
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        left = 0
        right = n - 1
        # process only if start == end
        while left < right and s[left] == s[right]:
            # move forward
            while left+1 < right and s[left] == s[left+1]:
                left += 1
            left += 1
            # move backward
            while right-1 > left and s[right-1] == s[right]:
                right -= 1
            right -= 1
            # exit when indices overlap
            if left >= right:
                break
        return right - left + 1


"""
    2nd: same as 1st but concise
"""


class Solution:
    def minimumLength(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        left = 0
        right = n - 1
        while left < right and s[left] == s[right]:
            c = s[left]
            while left <= right and s[left] == c:
                left += 1
            while left <= right and s[right] == c:
                right -= 1
        if left > right:
            return 0
        return right - left + 1
