"""
    Shortest substring of A containing B

    Input:
    bigString: "abcd$ef$axb$c$"
    smallString: "$$abf"

    Output:
    "f$axb$"
"""


def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    smallHt = constructHt(smallString)

    res = bigString
    curHt = {}
    cur = ''
    j = 0
    for i in range(len(bigString)):
        c = bigString[i]
        cur += c

        if c in curHt:
            curHt[c] += 1
        else:
            curHt[c] = 1

        while ifAContainB(curHt, smallHt):

            if len(cur) < len(res):
                res = cur

            last = bigString[j]
            j += 1

            cur = cur[1:]
            curHt[last] -= 1
            if curHt[last] == 0:
                del curHt[last]

    if ifAContainB(constructHt(res), smallHt):
        return res
    return ""


def constructHt(s):
    ht = {}
    for c in s:
        if c in ht:
            ht[c] += 1
        else:
            ht[c] = 1
    return ht


def ifAContainB(a, b):
    for key in b:
        if key not in a:
            return False
        if a[key] < b[key]:
            return False
    return True
