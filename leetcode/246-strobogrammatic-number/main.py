"""
    1st approach: 2 pointers + hashtable
	- if start and end == 0,1,8, left++, right--
	- if start == 6 and end == 9 or vice versa, left++, right--
	- else it is not a strobogrammatic number

    Time    O(N)
    Space   O(1)
	24 ms, faster than 92.67%
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        m = {
            '0': '0',
            '1': '1',
            '8': '8',
            '6': '9',
            '9': '6'
        }
        i = 0
        j = len(num) - 1
        while i <= j:
            if num[j] not in m or num[i] != m[num[j]]:
                return False
            i += 1
            j -= 1
        return True
