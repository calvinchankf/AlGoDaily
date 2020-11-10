"""
    1st approach: math + hashtable
    - do long division
    - find the recurring part from the remainders
    - if we see a recurring number, we stop
    - construct the non-recurring part + recurring part(if any)

    very good example
     0.123434...
    +---------
4950|611
       0
     ---------
     6110      <- remainder is 611
     4950
     ---------
     11600     <- remainder is 1160
      9900
     ---------
      17000    <- remainder is 1700
      14850
     ---------
       21500   <- remainder is 2150
       19800
     ---------
        17000  <- remainder is 1700
        14850
     ---------
         21500 <- remainder is 2150
         19800
     ---------
          1700 <- remainder is 1700
           ...

    Time    O(logn)
    Space   O(?) hard to say because the length of the recurring part varies
    16 ms, faster than 90.96%
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return '0'
        elif denominator == 1:
            return str(numerator)
        # sign
        sign = ''
        if numerator * denominator < 0:
            sign = '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        # divsion
        ht = {}  # {recurring number1: index1, recurring number2: index2, ...}
        arr = []
        startRecurringAt = -1
        while numerator > 0:
            arr.append(numerator//denominator)
            # similate the way we borrow a zero to divide a number
            numerator = numerator % denominator * 10
            if numerator in ht:
                startRecurringAt = ht[numerator]
                break
            ht[numerator] = len(arr)
        # construct the result string
        res = '' + sign
        for i in range(len(arr)):
            if i == 1:
                res += '.'
            if i == startRecurringAt:
                break
            res += str(arr[i])
        if startRecurringAt == -1:
            return res
        # append the recurring portion
        recurringNums = arr[startRecurringAt:]
        recurringNumStr = ''.join([str(x) for x in recurringNums])
        return res + '(' + recurringNumStr + ')'


s = Solution()
# 0.(012)
print(s.fractionToDecimal(4, 333))
# 0.07(432)
print(s.fractionToDecimal(33, 444))
# 3.(142857)
print(s.fractionToDecimal(22, 7))

# -0.07(432)
print(s.fractionToDecimal(-33, 444))
# -0.07(432)
print(s.fractionToDecimal(33, -444))
# 0.07(432)
print(s.fractionToDecimal(-33, -444))

# 2
print(s.fractionToDecimal(4, 2))
# 20
print(s.fractionToDecimal(40, 2))

print("-----")


"""
    2nd: same as
"""


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        if numerator == 0:
            return '0'
        elif numerator % denominator == 0:
            return str(numerator // denominator)
        # sign
        sign = '-' if numerator * denominator < 0 else ''
        numerator = abs(numerator)
        denominator = abs(denominator)

        prefix = str(numerator // denominator)
        suffix = ''

        remainder = numerator % denominator
        cache = {}  # {recurring number1: index1, recurring number2: index2, ...}
        while remainder not in cache:
            cache[remainder] = len(suffix)
            # similate the way we borrow a zero to divide a number
            suffix += str(remainder * 10 // denominator)
            remainder = remainder * 10 % denominator
            if remainder == 0:
                return sign + prefix + '.' + suffix
        nonRecurringDecimal = suffix[:cache[remainder]]
        recurringDecimal = suffix[cache[remainder]:]
        return sign + prefix + '.' + nonRecurringDecimal + '(' + recurringDecimal + ')'


s = Solution()
# 0.(012)
print(s.fractionToDecimal(4, 333))
# 0.07(432)
print(s.fractionToDecimal(33, 444))
# 3.(142857)
print(s.fractionToDecimal(22, 7))

# -0.07(432)
print(s.fractionToDecimal(-33, 444))
# -0.07(432)
print(s.fractionToDecimal(33, -444))
# 0.07(432)
print(s.fractionToDecimal(-33, -444))

# 2
print(s.fractionToDecimal(4, 2))
# 20
print(s.fractionToDecimal(40, 2))
