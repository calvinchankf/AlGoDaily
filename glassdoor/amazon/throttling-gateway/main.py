from collections import OrderedDict

"""
    On Amazon Prime Day, non-critical requests for a transaction system are routed through a throttling gateway 
    to ensure that the network is not choked by non-essential requests.

    The gateway has the following limits:
    - The number of transactions in any given second cannot exceed 3. 
    - The number of transactions in any given 10 second period cannot exceed 20. 
    - A ten-second period includes all requests arriving from any time max(1, T-9) to T (inclusive of both) for any valid time T. 
    - The number of transactions in any given minute cannot exceed 60. Similar to above, 1 minute is from max(1, T-59) to T.
    - Any request that exceeds any of the above limits will be dropped by the gateway. 
    - Given the times at which different requests arrive sorted ascending, write an algorithm to find how many requests will be dropped.

    Input:
    num: an integer representing the number of requests;
    requestTime: a list of integers representing the times of various requests.


    Output:
    Return an integer representing the total number of dropped requests.


    Note:
    Even if a request is dropped it is still considered for future calculations. 
    Although, if a request is to be dropped due to multiple violations, it is still counted only once.

    Constraints:
    1 <= num <= 10^6
    1 <= requestTime[i] <= 10^9
    0 <= i < num

    Example
    Input:
    num = 27
    requestTime = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7,7,7,7, 11, 11, 11, 11]

    Output:
    7

    Explanation:

     0  1  2  3  4  5  6  7  8  9  0  1  2  3  4  5  6  7  8  9  0  1  2   3   4   5   6
    [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
              ^                                                  ^  ^  ^       ^  ^   ^
              1                                                  2  3  4       5  6   7

    reasons:
    1. At most 3 requests are allowed in one second. Then No request will be dropped till 6 as all comes at an allowed rate of 3 requests per second and the 10-second clause is also not violated.
    2. At most 20 requests are allowed in ten seconds.
    3. At most 20 requests are allowed in ten seconds.
    4. At most 20 requests are allowed in ten seconds.
    5. Dropped. At most 20 requests are allowed in ten seconds.
    6. Dropped. At most 20 requests are allowed in ten seconds.
    7. Dropped. At most 20 requests are allowed in ten seconds.
"""


def f(n, requestTime):
    dropped = 0
    for i in range(3, len(requestTime)):
        if requestTime[i] == requestTime[i-3]:
            dropped += 1
            continue
        if i > 19 and requestTime[i] - requestTime[i-20] < 10:
            dropped += 1
            continue
        if i > 59 and requestTime[i] - requestTime[i-60] < 60:
            dropped += 1
            continue
    return dropped


a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5,
     5, 5, 6, 6, 6, 7, 7, 7, 7, 11, 11, 11, 11]
print(f(0, a))
