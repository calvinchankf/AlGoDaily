from collections import defaultdict

"""
    1st: nested hashtable
    - only store nonzero cell (at i,j) in hashtables
    - then we iterate thru the hashtables to calclulate the result on each cell

    e.g.
    A = [
        [1,0,0],
        [-1,0,3]
    ]
    B = [
        [7,0,3],
        [0,0,0],
        [0,0,1]
    ]

    htA = {
        0: {0: 1},
        1: {0: -1, 2: 3}
    }
    htB = {
        0: {0: 7}, 
        2: {2: 1}
    }

    Computation:
    res[0][0] = htA[0][0] + htB[0][0] = 7
                       ^           ^
    res[1][0] = htA[1][0] + htB[0][0] = -7
                       ^           ^
    res[1][2] = htA[1][2] + htB[2][2] = 3
                       ^           ^

    Time    O(A + B + ABA) <- it also depends on the number of non-zero
    Space   O(A+B)
    96 ms, faster than 44.59%
"""


class Solution:
    def multiply(self, A, B):
        htA = defaultdict(dict)
        htB = defaultdict(dict)

        RA, CA = len(A), len(A[0])
        RB, CB = len(B), len(B[0])

        for i in range(RA):
            for j in range(CA):
                if A[i][j] != 0:
                    htA[i][j] = A[i][j]

        for j in range(CB):
            for i in range(RB):
                if B[i][j] != 0:
                    htB[j][i] = B[i][j]

        res = []
        for _ in range(RA):
            res.append(CB * [0])

        for i in htA:
            for j in htB:
                for key in htA[i]:
                    if key in htB[j]:
                        res[i][j] += htA[i][key] * htB[j][key]
        return res


s = Solution()

a = [[1, 0, 0], [-1, 0, 3]]
b = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(s.multiply(a, b))

a = [[1, 0], [0, 0], [2, 0], [3, 0]]
b = [[0, 7, 0], [0, 1, 0]]
print(s.multiply(a, b))

print("----")


"""
    2nd: optimized the 1st
    - we just store the indcies for non-zero cells

    e.g.
    A = [
        [1,0,0],
        [-1,0,3]
    ]
    B = [
        [7,0,0],
        [0,0,0],
        [0,0,1]
    ]

    htA = {
        0: {0},
        1: {0, 2}
    }
    htB = {
        0: {0}, 
        2: {2}
    }

    Time    O(A + B + ABA) <- it also depends on the number of non-zero
    Space   O(A+B)
    56 ms, faster than 90.70%
"""


class Solution:
    def multiply(self, A, B):
        htA = defaultdict(set)
        htB = defaultdict(set)

        RA, CA = len(A), len(A[0])
        RB, CB = len(B), len(B[0])

        for i in range(RA):
            for j in range(CA):
                if A[i][j] != 0:
                    htA[i].add(j)

        for j in range(CB):
            for i in range(RB):
                if B[i][j] != 0:
                    htB[j].add(i)

        res = []
        for _ in range(RA):
            res.append(CB * [0])

        for i in htA:
            for j in htB:
                for key in htA[i]:
                    if key in htB[j]:
                        res[i][j] += A[i][key] * B[key][j]
        return res


s = Solution()

a = [[1, 0, 0], [-1, 0, 3]]
b = [[7, 0, 0], [0, 0, 0], [0, 0, 1]]
print(s.multiply(a, b))

a = [[1, 0], [0, 0], [2, 0], [3, 0]]
b = [[0, 7, 0], [0, 1, 0]]
print(s.multiply(a, b))
