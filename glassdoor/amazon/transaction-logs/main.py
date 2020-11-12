from collections import *

"""
    https://leetcode.com/discuss/interview-question/862600/
    https://aonecode.com/amazon-online-assessment-transaction-logs

    Amazon parses logs of user transactions/activity to flag fraudulent activity. The log file is represented as an Array of arrays. The arrays consist of the following data:

    '<userid1>, <userid2> <# of transactions>'

    For example:

    '345366 89921 45'
    Note the data is space delimited

    So, the log data would look like:

    [
    '345366 89921 45',
    '029323 38239 23'
    ...
    ]
    Write a function to parse the log data to find distinct users that meet or cross a certain threshold. The function will take in 2 inputs:

    Input 1: Log data in form an array of arrays
    Input 2: threshold as an integer

    Output should be an array of userids that are sorted. <--- see if it is to sort ascendingly/descendingly !!!

    If same userid appears in the transaction as userid1 and userid2, it should count as one occurence, not two.

    Example:
    Input 1:

    [
    '345366 89921 45',
    '029323 38239 23',
    '38239 345366 15',
    '029323 38239 77',
    '345366 38239 23',
    '029323 345366 13',
    '38239 38239 23'
    ]
    Input 2: 3

    Ouput: [345366 , 38239, 029323]

    Explanation:
    Given the following counts of userids, there are only 3 userids that meet or exceed the threshold of 3.
    345366:4 , 38239:5, 029323:3, 89921:1
"""


def f(logs, threshold):
    ht = Counter()
    for log in logs:
        u1, u2, t = log.split(' ')
        if u1 == u2:
            ht[u1] += 1
        else:
            ht[u1] += 1
            ht[u2] += 1
    res = []
    for u in ht:
        if ht[u] >= threshold:
            res.append(u)
    return sorted(res, key=lambda x: int(x), reverse=True)


a = [
    "345366 89921 45]",
    "029323 38239 23",
    "38239 345366 15",
    "029323 38239 77",
    "345366 38239 23",
    "029323 345366 13",
    "38239 38239 23"
]
b = 3
print(f(a, b))

a = [
    "88 99 200",
    "88 99 300",
    "99 32 100",
    "12 12 15"
]
b = 2
print(f(a, b))
