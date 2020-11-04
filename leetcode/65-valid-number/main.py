"""
    pure if-else logic in one pass
    - too many corner cases

    Time    O(N)
    Space   O(N) <- strings of numberBeforeE, numberAfterE
    36 ms, faster than 50.58%
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        seenE = False
        seenDot = False
        numberBeforeE = ''
        numberAfterE = ''
        for c in s:
            if c.isdigit():
                if seenE == False:
                    numberBeforeE += c
                else:
                    numberAfterE += c
            elif c == 'e':
                if seenE:
                    return False
                seenE = True
            elif c == '.':
                if seenDot or seenE:
                    return False
                seenDot = True
            elif c in '+-':

                if seenDot and seenE == False:
                    return False

                if seenE == False:
                    if len(numberBeforeE) == 0:
                        numberBeforeE += c
                    else:
                        return False
                else:
                    if len(numberAfterE) == 0:
                        numberAfterE += c
                    else:
                        return False
            else:
                return False

        if seenE and (len(numberBeforeE) == 0 or len(numberAfterE) == 0):
            return False
        if seenDot and len(numberBeforeE) == 0 and len(numberAfterE) == 0:
            return False
        if len(numberBeforeE) == 0:
            return False
        if numberBeforeE[0] in '-+' and len(numberBeforeE[1:]) == 0:
            return False
        if len(numberAfterE) > 0 and numberAfterE[0] in '-+' and len(numberAfterE[1:]) == 0:
            return False
        return True


s = Solution()

a = '0'
print(a, s.isNumber(a))

a = ' 0.1 '
print(a, s.isNumber(a))

a = 'abc'
print(a, s.isNumber(a))

a = '1 a'
print(a, s.isNumber(a))

a = '2e10'
print(a, s.isNumber(a))

a = ' -90e3   '
print(a, s.isNumber(a))

a = ' 1e'
print(a, s.isNumber(a))

a = 'e3'
print(a, s.isNumber(a))

a = '6e-1'
print(a, s.isNumber(a))

a = ' 99e2.5 '
print(a, s.isNumber(a))

a = '53.5e93'
print(a, s.isNumber(a))

a = ' --6 '
print(a, s.isNumber(a))

a = '+-3'
print(a, s.isNumber(a))

a = '95a54e53'
print(a, s.isNumber(a))

print('-----')

a = "1-8e65"
print(a, s.isNumber(a))

a = "18e6-5"
print(a, s.isNumber(a))

a = "1-8e6-5"
print(a, s.isNumber(a))

a = "."
print(a, s.isNumber(a))

a = "1."
print(a, s.isNumber(a))

a = ".1"
print(a, s.isNumber(a))

a = ' '
print(a, s.isNumber(a))

a = "4e+"
print(a, s.isNumber(a))

a = "+e4"
print(a, s.isNumber(a))

a = "+e+"
print(a, s.isNumber(a))

a = '0e-4'
print(a, s.isNumber(a))  # True

a = ".-4"
print(a, s.isNumber(a))  # False

a = ".+4"
print(a, s.isNumber(a))  # False

a = "32.e-80123"
print(a, s.isNumber(a))  # True
