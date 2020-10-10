"""
    1st approach:
    - split cases for 1-3,4,5,6-8,9

    Time    O(n)
    Space   O(n)
    48 ms, faster than 100.00%
"""


class Solution(object):
    def intToRoman(self, num):
        m = {
            1: 'I',
            5:  'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        res = ''
        scale = 0
        while num > 0:
            digit = num%10
            num //= 10
            
            x = digit * (10**scale)
            if x in m:
                res = m[x] + res
            else:
                one = 10**scale
                five = 10**scale * 5
                ten = 10**scale * 10
                if 1 <= digit < 4:
                    s = m[one] * digit
                    res = s + res
                elif digit == 4:
                    s = m[one] + m[five]
                    res = s + res
                elif 6 <= digit < 9:
                    s = m[five] + m[one] * (digit - 5)
                    res = s + res
                elif digit == 9:
                    s = m[one] + m[ten]
                    res = s + res
            scale += 1
        return res


print(Solution().intToRoman(0))
print(Solution().intToRoman(10))
print(Solution().intToRoman(58))
print(Solution().intToRoman(200))
print(Solution().intToRoman(120))
print(Solution().intToRoman(508))
print(Solution().intToRoman(203))
print(Solution().intToRoman(3999))
print("-----")

"""
    2nd approach: hashtable
    - concise and less cases

    Time    O(n)
    Space   O(n)
    48 ms, faster than 96.43%
"""


class Solution(object):
    def intToRoman(self, num):
        m = {
            1: 'I',
            4: 'IV',
            5:  'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M'
        }
        # 458
        res = ''
        scale = 0
        while num > 0:
            digit = num % 10
            num //= 10
            x = digit * (10**scale)
            if x in m:
                res = m[x] + res
            else:
                if digit < 5:
                    # 2,3
                    s = m[10**scale] * digit
                    res = s + res
                else:
                    # 6,7,8
                    s = m[5 * 10**scal)] + m[10**scale] * (digit - 5)
                    res=s + res
            scale += 1
        return res


print(Solution().intToRoman(0))
print(Solution().intToRoman(10))
print(Solution().intToRoman(58))
print(Solution().intToRoman(200))
print(Solution().intToRoman(120))
print(Solution().intToRoman(508))
print(Solution().intToRoman(203))
print(Solution().intToRoman(3999))
print("-----")
