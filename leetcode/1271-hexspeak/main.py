"""
    1st: brute force
    - convert the input to hexadecimal number
    - do checking

    Time    O(logN)
    Space   O(logN)
    12 ms, faster than 94.34%
"""


class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        if num == 0:
            return 'O'
        n = int(num)
        ht = {10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        hexy = ''
        while n > 0:
            temp = n % 16
            if temp >= 10:
                temp = ht[temp]
            else:
                temp = str(temp)
            hexy = temp + hexy
            n /= 16
        res = ''
        letters = set(['A', 'B', 'C', 'D', 'E', 'F'])
        for c in hexy:
            if c == '0':
                res += 'O'
            elif c == '1':
                res += 'I'
            elif c in letters:
                res += c
            else:
                return 'ERROR'
        return res


"""
    2nd: use built-in hex()
    - convert the input to hexadecimal number
    - do checking

    Time    O(logN)
    Space   O(logN)
    16 ms, faster than 81.60%
"""


class Solution(object):
    def toHexspeak(self, num):
        """
        :type num: str
        :rtype: str
        """
        s = hex(int(num))[2:]
        letters = set(['a', 'b', 'c', 'd', 'e', 'f'])
        res = ''
        for c in s:
            if c == '0':
                res += 'O'
            elif c == '1':
                res += 'I'
            elif c in letters:
                res += c.upper()
            else:
                return 'ERROR'
        return res
