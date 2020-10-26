#!/bin/python3

import re
import sys
import math
import random
import os

"""
    You find it hard to wake up early in the morning. So you set 2 alarms because 1 alarm cannot wake you up.
    You set the first alarm clock N and it rings for every P minutes.
    You set the second alarm clock M and it rings for every K minutes.
    Determine how many minutes it will take for both alarms to ring at the same time.

    e.g.1
    N = 4, P = 10, M = 3, K = 7
    first alarm: 4 -> 14 -> 24
    second alarm: 3 -> 10 -> 17 -> 24
    return 24

    e.g.2
    N = 1, P = 2, M = 2, K = 2
    first alarm: 1 -> 3 -> 5 -> 7
    second alarm: 2 -> 4 -> 6 -> 8 -> 10
    return -1 because they will not meet forever
"""

#
# implement method/function with name 'solve' below.
#
# The function is expected to return a value of type INTEGER.
# The function accepts following parameters:
#  1. p is of type INTEGER.
#  2. n is of type INTEGER.
#  3. k is of type INTEGER.
#  4. m is of type INTEGER.


def solve(p,n,k,m):
    if (n%m == 0 or m%n == 0) and p == k:
        return -1
    a = n
    b = m
    while a != b:
        if a < b:
            a += p
        else:
            b += k
    return a

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_FILE_PATH'], 'w')
#     fptr.write("\n")
#     p = int(input().strip())
#     n = int(input().strip())
#     k = int(input().strip())
#     m = int(input().strip())
#     outcome = solve(p, n, k, m)
#     fptr.write(str(outcome)  + '\n');
#     fptr.close()


print(solve(10,4,7,3))
print(solve(2,1,2,2))