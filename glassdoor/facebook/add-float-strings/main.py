"""
    https://leetcode.com/discuss/interview-question/551052/Facebook-or-Phone-or-Enterprise-Engineer-or-Addition-of-String-Numbers

    Problem: Given 2 strings str1 and str2, which represent numbers in string, perform addition of the numbers and return the result as a string.

    Example 1: str1 = "123.52" and str2 = "11.2", output should be "134.72"
    Example 2: str1 = "110.75" and str2 = "9", output should be "119.75"

    Constraints: You may not convert entire string to integer directly. Strings may be null and will always have values >= 0.0
"""
def addFloatStrings(s1, s2):
    arr1 = s1.split('.')
    arr2 = s2.split('.')
    
    s1Int, s1Deci = '0', '0'
    s2Int, s2Deci = '0', '0'

    if len(arr1) == 2:
        s1Int, s1Deci = arr1[0], arr1[1]
    elif len(arr1) == 1:
        s1Int = arr1[0]
    
    if len(arr2) == 2:
        s2Int, s2Deci = arr2[0], arr2[1]
    elif len(arr2) == 1:
        s2Int = arr2[0]
    
    # integer
    integer = add2Integers(s1Int, s2Int)

    # the number after the decimal point
    s1Deci, s2Deci = prcocessDecimals(s1Deci, s2Deci)
    decimal = add2Integers(s1Deci, s2Deci)
    if len(decimal) > max(len(s1Deci), len(s2Deci)):
        integer = add2Integers(integer, '1')
        decimal = decimal[1:]

    return integer + '.' + decimal
    

def prcocessDecimals(s1, s2):
    maxLen = max(len(s1), len(s2))
    if len(s1) < maxLen:
        return s1 + (maxLen - len(s1)) * '0', s2
    return s1, s2 + (maxLen - len(s2)) * '0'

def add2Integers(num1, num2):
    res = ""
    carry = 0
    i = len(num1) - 1
    j = len(num2) - 1
    while i >= 0 or j >= 0:
        a = 0
        if i >= 0:
            a = int(num1[i])
            i -= 1
        b = 0
        if j >= 0:
            b = int(num2[j])
            j -= 1
        temp = a + b + carry
        d = temp%10
        carry = temp//10
        res = str(d) + res
    if carry > 0:
        res = str(carry) + res
    return res


a = "123.52"
b = "11.2"
print(addFloatStrings(a, b)) # "134.72"

a = "110.75"
b = "9"
print(addFloatStrings(a, b)) # "119.75"

a = "9"
b = "110.75"
print(addFloatStrings(a, b)) # "119.75"

a = '199.999'
b = '199.99'
print(addFloatStrings(a, b)) # 399.989

a = '199.999'
b = '0.001'
print(addFloatStrings(a, b)) # 200.000