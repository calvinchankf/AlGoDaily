#!/bin/python3

import re
import sys
import math
import random
import os

"""
    Given a string consisting of English letters both lowercase and uppercase. Your task is to convert it to the prime word.
    Prime Word is a word consisting of only prime characters and prime character is a letter whose ASCII code is prime.
    Each non-prime character should be replaced by the nearest prime character. If the character is equidistant with 2 prime characters,
    the one with lower ASCII value will be considered as its replacement.

    e.g.1
    input: ABc
    output: CCa

    e.g.2
    input: ABCa
    output: CCCa
"""

#
# implement method/function with name 'solve' below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. s is of type STRING.

def getPrimes(n):
    if n < 2:
        return []
    arePrimes = n * [True]
    arePrimes[0] = False
    arePrimes[1] = False
    res = []
    for i in range(2, n):
        if arePrimes[i] == True:
            res.append(i)
            j = 2
            while i*j < n:
                arePrimes[i*j] = False
                j += 1
    return res

def bsearch(nums, target):
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if right < 0:
        return 0
    if left > len(nums) - 1:
        return len(nums) - 1
    if abs(target - nums[left]) < abs(target - nums[right]):
        return left
    return right

def solve(s):
    primes = getPrimes(500)
    res = ''
    for c in s:
        target = ord(c)
        j = bsearch(primes, target)
        p = primes[j]
        res += chr(p)

    return res


# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
#     fptr.write("\n")
#     s = input()
#     outcome = solve(s)
#     fptr.write(str(outcome)  + '\n');
#     fptr.close()

print(solve('ABc'))
print(solve('ABCc'))

