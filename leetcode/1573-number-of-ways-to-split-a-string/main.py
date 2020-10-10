"""
    messy approach in contest: math
    - count the zeros

    e.g. '100100010100110'
    - there are 6 '1's, so we can slice every string that has 2 '1'
    1001 000 101 00 110
         ---     --     <- we have 4 options for 000, 3 options for 00, so the answer is 4*3 = 12
    
    e.g. '00000'
    - there is no '1', but we can still slice the '0' in the middle
    0 000 0
      --- <- total number of slice we can do it 3+2+1 = 6

    Time    O(N)
    Space   O(1)
    444 ms, faster than 100.00%
"""


class Solution(object):
    def numWays(self, s):
        n = len(s)
        count = 0
        for i in range(n):
            if s[i] == '1':
                count += 1

        if count % 3 != 0:
            return 0

        if count == 0:
            x = n - 2
            return (x * (x+1) // 2) % (10**9+7)

        fc = 0
        a = 0
        for i in range(n):
            if s[i] == '1':
                fc += 1
                if fc == count//3:
                    a = i
                    break
        leftCount = 0
        for i in range(a+1, n):
            if s[i] == '0':
                leftCount += 1
            else:
                break

        bc = 0
        b = 0
        for i in range(n-1, -1, -1):
            if s[i] == '1':
                bc += 1
                if bc == count//3:
                    b = i
                    break
        rightCount = 0
        for i in range(b-1, -1, -1):
            if s[i] == '0':
                rightCount += 1
            else:
                break

        # print(leftCount, rightCount)
        return (leftCount+1) * (rightCount+1) % (10**9+7)
