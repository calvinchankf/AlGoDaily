"""
    1st approach:
    - split cases for 1-3,4,5,6-8,9

    Time    O(n)
    Space   O(n)
    48 ms, faster than 100.00%
"""


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = ["I", "V", "X", "L", "C", "D", "M"]
        res = ""
        i = 0
        while num > 0:
            cur = num % 10
            num /= 10
            j = i*2
            i += 1

            if cur == 0:
                continue

            if cur < 5:
                if cur < 4:
                    res = cur*m[j] + res  # add I,II,III
                else:
                    res = m[j] + m[j+1] + res  # add IV
            elif cur == 5:
                res = m[j+1] + res  # add V
            else:
                if cur < 9:
                    res = m[j+1] + (cur-5)*m[j] + res  # add VI,VII,VIII
                else:
                    res = m[j] + m[j+2] + res  # add IX
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
        res = ''
        scale = 0
        while num > 0:
            d = num % 10
            cur = d * (10**scale)
            num = num // 10
            if cur in m:
                res = m[cur] + res
            else:
                if d < 4:
                    res = m[10**scale] * d + res
                if d > 5:
                    res = m[5 * 10**scale] + m[10**scale] * (d - 5) + res
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
