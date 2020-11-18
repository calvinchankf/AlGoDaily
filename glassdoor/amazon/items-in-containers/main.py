"""
    https://leetcode.com/discuss/interview-question/861453/
    https://leetcode.com/discuss/interview-question/865660/

    Items in Containers

    Amazon would like to know how much inventory exists in their closed inventory compartments. Given a string s
    consisting of items as "*" and closed compartments as an open and close "|", an array of starting indices
    startIndices, and an array of ending indices endIndices, determine the number of items in closed compartments
    within the substring between the two indices, inclusive.

    An item is represented as an asterisk ('*' = ascii decimal 42)
    A compartment is represented as a pair of pipes that may or may not have items between them ('|' = ascii decimal 124).

    Example

    s = '|**|*|*'

    startIndices = [1, 1]

    endIndices = [5, 6]

    The string has a total of 2 closed compartments, one with 2 items and one with 1 item. For the first pair of
    indices, (1, 5), the substring is '|**|*'. There are 2 items in a compartment.

    For the second pair of indices, (1, 6), the substring is '|**|*|' and there are 2 + 1 = 3 items in compartments.

    Both of the answers are returned in an array, [2, 3].

    Function Description.

    Complete the numberOfItems function in the editor below. The function must return an integer array that contains
    the results for each of the startIndices[i] and endIndices[i] pairs.

    numberOfItems has three parameters:

    s: A string to evaluate

    startIndices: An integer array, the starting indices.

    endIndices: An integer array, the ending indices.

    Constraints

    1 <= m, n <= 105
    1 <= startIndices[i] <= endIndices[i] <= n
    Each character of s is either '*' or '|'

    Input Format For Custom Testing

    The first line contains a string, S.
    The next line contains an integer, n, the number of elements in startIndices.
    Each line i of the n subsequent lines (where 1 <= i <= n) contains an integer, startIndices[i].
    The next line repeats the integer, n, the number of elements in endIndices.
    Each line i of the n subsequent lines (where 1 <= i <= n) contains an integer, endIndices[i].

    Sample Case 0
    Sample Input For Custom Testing

    STDIN Function

    *|*| -> s = "*|*|"

    1 -> startIndices[] size n = 1
    1 -> startIndices = 1
    1 -> endIndices[] size n = 1
    3 -> endIndices = 3

    ** Sample Output**
    0

    Explanation
    s = *|*|

    n = 1
    startIndices = [1]
    n = 1
    startIndices = [3]

    The substring from index = 1 to index = 3 is '|'. There is no compartments in this string.

    Sample Case 1
    Sample Input For Custom Testing

    STDIN Function

    *|*|*| -> s = "*|*|*|"
    1 -> startIndices[] size n = 1
    1 -> startIndices = 1
    1 -> endIndices[] size n = 1
    6 -> endIndices = 6

    Sample Output
    2

    Explanation
    s = '*|*|*|'
    n = 1
    startIndices = [1]
    n = 1
    startIndices = [1]

    The substring from index = 1 to index = 6 is '||*|'. There are two compartments in this string at (index = 2,
    index = 4) and (index = 4, index = 6). There are 2 items between these compartments.

    Time    O(S + min(S, E))
    Space   O(3S)
"""


"""
    approach:
    - similar to prefix sum, i accumulate the number of * during iteration
    - cache the position of the nearest left compartment at every index
    - cache the position of the nearest right compartment at every index

            0 1 2 3 4 5 6 7 8 9
            * * | * * * | * * *
    left   -1-1 2 2 2 2 6 6 6 6
    right   2 2 2 6 6 6 6-1-1-1
    pfs     1 2 2 3 4 5 5 6 7 8

    - then when we do query, we can find the compartment in the middle, and calculate the * inside using pfs[right] - pfs[left]
    query(0, 7) = pfs[left[7]] - pfs[right[0]] = pfs[6] - pfs[2] = 5 - 2 = 3
    query(1, 3) = pfs[left[3]] - pfs[right[1]] = pfs[2] - pfs[2] = 2 - 2 = 0
"""


def f(S, starts, ends):
    if not S or len(S) == 0 \
            or not starts or not ends \
            or len(starts) != len(ends):
        return 0

    n = len(S)

    cache = {}
    count = 0
    for i in range(n):
        c = S[i]
        if c == '*':
            count += 1
        cache[i] = count

    leftCompartments = n * [-1]
    rightCompartments = n * [-1]
    left = -1
    for i in range(n):
        if S[i] == '|':
            left = i
        leftCompartments[i] = left
    right = -1
    for i in range(n-1, -1, -1):
        if S[i] == '|':
            right = i
        rightCompartments[i] = right

    # print(leftCompartments)
    # print(rightCompartments)

    res = []
    for i in range(len(starts)):

        s = rightCompartments[starts[i] - 1]
        e = leftCompartments[ends[i] - 1]

        if s == -1 or e == -1 or s > e:
            res.append(0)
        else:
            res.append(cache[e] - cache[s])
    return res


# 2, 3
a = '|**|*|*'
b = [1, 1]
c = [5, 6]
print(f(a, b, c))

# 0, 1
a = '*|*|'
b = [1, 1]
c = [3, 4]
print(f(a, b, c))

# 0
a = '*|*|*|'
b = [1]
c = [1]
print(f(a, b, c))

# 0
a = '*|*|*|'
b = [2]
c = [1]
print(f(a, b, c))

# 3, 3, 3, 3, 2
a = '**|**|*|***'
b = [1, 1, 2, 3, 3]
c = [11, 10, 9, 8, 7]
print(f(a, b, c))

# 1, 0
a = '*||*|'
b = [1, 1]
c = [5, 4]
print(f(a, b, c))

# 3
a = '**|***|**'
b = [1]
c = [9]
print(f(a, b, c))

# 0
a = '*********'
b = [1]
c = [9]
print(f(a, b, c))

# 0
a = '|||||||||'
b = [1]
c = [9]
print(f(a, b, c))
