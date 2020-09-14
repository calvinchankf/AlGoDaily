"""
    1st approach: hashtable

    e.g.1 => 19
    
    1^2 + 9^2 = 82
    8^2 + 2^2 = 68
    6^2 + 8^2 = 100
    1^2 + 0^2 + 02 = 1
    return True

    e.g.2 => 2
    2^2 = 4
    4^2 = 16
    1^2 + 6^2 = 37
    3^2 + 7^2 = 58
    5^2 + 8^2 = 89
    8^2 + 9^2 = 145
    1^2 + 4^2 + 5^2 = 42
    4^2 + 2^2 = 20
    2^2 + 0^2 = 4 <------------ seen!!!
    return False

    Time    O(?) it is hard to determind, but any number can only appear once at most, so the upperbound is O(2^31-1)
    Space   O(?) the upperbound is O(2^31-1)
    16 ms, faster than 96.23%
"""


class Solution(object):
    def isHappy(self, n):
        ht = {}
        while n != 1:
            temp = 0
            while n > 0:
                d = n % 10
                temp += d**2
                n = n//10
            if temp in ht:
                return False
            ht[temp] = True
            n = temp
        return True


s = Solution()
print(s.isHappy(2))
print(s.isHappy(3))
print(s.isHappy(4))
print(s.isHappy(5))
print(s.isHappy(5))
print(s.isHappy(6))
print(s.isHappy(7))
print(s.isHappy(8))
print(s.isHappy(9))
print(s.isHappy(10))
print(s.isHappy(11))
print(s.isHappy(12))
print(s.isHappy(13))
print(s.isHappy(14))
print(s.isHappy(15))
print(s.isHappy(15))
print(s.isHappy(16))
print(s.isHappy(17))
print(s.isHappy(18))
print(s.isHappy(19))
print(s.isHappy(20))

"""
   If happy numbers are generally prime (19, 79, 239) should it always end in a 9?
   Can u think of a happy number that doesn't end in 9? 
"""
