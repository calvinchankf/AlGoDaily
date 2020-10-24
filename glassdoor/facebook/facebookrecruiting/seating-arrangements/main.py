"""
    https://leetcode.com/discuss/interview-question/709517/Facebook-or-Recruiting-Portal-or-Seating-Arrangements

    Seating Arrangements

    There are n guests attending a dinner party, numbered from 1 to n. The ith guest has a height of arr[i] inches.
    The guests will sit down at a circular table which has n seats, numbered from 1 to n in clockwise order around the table.
    As the host, you will choose how to arrange the guests, one per seat. Note that there are n! possible permutations of seat assignments.
    Once the guests have sat down, the awkwardness between a pair of guests sitting in adjacent seats is defined as the
    absolute difference between their two heights. Note that, because the table is circular, seats 1 and n are considered
    to be adjacent to one another, and that there are therefore n pairs of adjacent guests.
    The overall awkwardness of the seating arrangement is then defined as the maximum awkwardness of any pair of adjacent
    guests. Determine the minimum possible overall awkwardness of any seating arrangement.

    Signature
    int minOverallAwkwardness(int[] arr)
    Input
    n is in the range [3, 1000].
    Each height arr[i] is in the range [1, 1000].
    Output
    Return the minimum achievable overall awkwardness of any seating arrangement.

    Example
    n = 4
    arr = [5, 10, 6, 8]
    output = 4
    If the guests sit down in the permutation [3, 1, 4, 2] in clockwise order around the table
    (having heights [6, 5, 8, 10], in that order), then the four awkwardnesses between pairs of adjacent
    guests will be |6-5| = 1, |5-8| = 3, |8-10| = 2, and |10-6| = 4, yielding an overall awkwardness of 4.
    It's impossible to achieve a smaller overall awkwardness.
"""

"""
    greedy

    idea:
    e.g. [5, 10, 6, 8, 11, 12]

                       0  1  2   3   4   5
    sort them to have [5, 6, 8, 10, 11, 12]
    then the optimal result looks like this on our round table 

        5
    6       8
    10      11
        12
    
    look at the numbers in the clockwise order:
    [5, 8, 11, 12, 10, 6]
    which the indices are
     0  2  4 | 5   3   1
    which is the sortedNums[::2] + reverse of sortedNums[1::2]

    Time    O(NlogN)
    Space   O(N)
"""
def minOverallAwkwardness(arr):
    arr.sort()
    numsAtEvenIdx = arr[::2]
    numsAtOddIdx = arr[1::2]
    arr = numsAtEvenIdx + numsAtOddIdx[::-1]
    res = abs(arr[-1] - arr[0])
    for i in range(1, len(arr)):
        res = max(res, abs(arr[i] - arr[i-1]))
    return res

a = [5, 10, 6, 8]
print(minOverallAwkwardness(a))

a = [5, 10, 6, 8, 11]
print(minOverallAwkwardness(a))