"""
    1st: hashtable
    - for each row, process a string to represent seats allocation
    e.g. reservedSeats = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    {
        1: '0110000100', 
        2: '0000010000', 
        3: '1000000001',
    }

    LTE: 48 / 53 test cases passed.
"""


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        ht = {}
        for r, c in reservedSeats:
            if r not in ht:
                ht[r] = '0000000000'
            ht[r] = ht[r][:c-1] + '1' + ht[r][c:]
        res = 0
        for i in range(1, n+1):
            if i not in ht:
                res += 2
            else:
                row = ht[i]
                if row[1:9] == '00000000':
                    res += 2
                elif row[1:5] == '0000':
                    res += 1
                elif row[5:9] == '0000':
                    res += 1
                elif row[3:7] == '0000':
                    res += 1
        return res


"""
    2nd: hashtable
    - same logic as the above BUT just iterate the reservedSeats so that we dont necessarily go through from 1 to 10^9

    Time    O(R) R:number of reservedSeats
    Space   O(R)
    728 ms, faster than 50.18% 
"""


class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        reservedRows = set()
        ht = {}
        for r, c in reservedSeats:
            if r not in ht:
                ht[r] = '0000000000'
            ht[r] = ht[r][:c-1] + '1' + ht[r][c:]
            reservedRows.add(r)
        res = 0
        lastRow = 0
        for r in sorted(list(reservedRows)):
            diff = r - lastRow - 1
            if diff > 0:
                res += 2 * diff
            row = ht[r]
            if row[1:9] == '00000000':
                res += 2
            elif row[1:5] == '0000' or row[5:9] == '0000' or row[3:7] == '0000':
                res += 1
            lastRow = r
        diff = n - lastRow
        if diff > 0:
            res += 2 * diff
        return res
