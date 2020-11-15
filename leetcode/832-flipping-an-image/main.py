"""
    0th: brute force

    Time		O(N)
	Space		O(N)
	48ms beats 79%
"""


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        R, C = len(A), len(A[0])
        for i in range(R):
            row = A[i]
            r = row[::-1]
            newRow = C * [0]
            for j in range(C):
                if r[j] == 0:
                    newRow[j] = 1
            A[i] = newRow
        return A


"""
    1st approach
	1. swap the columns
	2. NOT the binary value using ^
        - zero to one: 0^1 = 1
        - one to zeor: 1^1 = 1


	Time		O(2N)
	Space		O(1)
	4ms beats 100%
	18apr2019
"""


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            c = len(A[0])
            half = c/2
            for j in range(half):
                A[i][j], A[i][c-j-1] = A[i][c-j-1], A[i][j]

        for i in range(len(A)):
            for j in range(len(A[0])):
                A[i][j] = A[i][j] ^ 1

        return A


a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(Solution().flipAndInvertImage(a))

print("-------------------------")

"""
    2nd approach
	1. swap the columns
	2. NOT the binary value using ^
        - zero to one: 0^1 = 1
        - one to zeor: 1^1 = 1
    3. do the ^ within the same loop

	Time		O(N)
	Space		O(1)
	4ms beats 100%
	18apr2019
"""


class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):
            c = len(A[0])
            # get the middle value involved
            half = (c+1)/2
            for j in range(half):
                # flip horizontally
                if j == c-j-1:
                    # ^ the number in the middle
                    A[i][j] = A[i][j] ^ 1
                else:
                    # ^ as well
                    A[i][j], A[i][c-j-1] = A[i][c-j-1] ^ 1, A[i][j] ^ 1

        return A


a = [[1, 1, 0], [1, 0, 1], [0, 0, 0]]
print(Solution().flipAndInvertImage(a))
