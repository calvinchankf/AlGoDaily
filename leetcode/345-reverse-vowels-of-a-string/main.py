"""
    questions to ask:
    - a, e, i, o, u ony? yes
    - capital letters? yes
"""


"""
    1st approach: 2 pointers

    Time  O(n)
    Space O(n)
    48 ms, faster than 87.75%
"""


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        arr = [c for c in s]
        i = 0
        j = n - 1
        while i < j:
            if arr[i] in 'aeiouAEIOU' and arr[j] in 'aeiouAEIOU':
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
            elif arr[i] in 'aeiouAEIOU':
                j -= 1
            elif arr[j] in 'aeiouAEIOU':
                i += 1
            else:
                i += 1
                j -= 1
        return ''.join(arr)

"""
    2nd approach: 2 pointers but with an array

    Time  O(n)
    Space O(n)
    48 ms, faster than 80.98%
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = []
        for c in s:
            arr.append(c)
        vowels = set(['a','e','i','o','u','A','E','I','O','U'])
        left = 0
        right = len(s) - 1
        while left < right:
            while left < right and arr[left] not in vowels:
                left += 1
            while left < right and arr[right] not in vowels:
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return ''.join(arr)