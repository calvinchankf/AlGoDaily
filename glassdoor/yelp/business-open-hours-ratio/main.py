"""
    https://leetcode.com/discuss/interview-question/304617/Yelp-or-OA-2019-or-Business-Open-Hours-Ratio

    Businesses on Yelp list the hours that they open each day. We want to be able to calculate what percentage of a given time frame a business opens.

    Inputs:
    A time range to query for (as a TimeRange object)
    A business's open hours (as a List of TimeRanges)

    Output:
    The fraction OF THE QUERY TIME RANGE that the business is open.
    (In other words, the percentage of the query time range in which the business is open.)
    Return this number as a float. This function should NOT do any rounding.

    Examples of time ranges:
        (0, 24)        the whole day
        (9, 17)        9 AM to 5 PM
        (18, 23.75)    6 PM to 11:45 PM

    Examples of open hours:
        []                       closed the entire day
        [(0, 24)]                open the entire day
        [(9.5, 17)]              open from 9:30 AM to 5 PM
        [(11, 14), (18, 22)]     open from 11 AM to 2 PM, and from 6 PM to 10 PM

    Assume that the open hours time ranges are in order and non-overlapping.

    Furthermore, all time ranges (start, end) have the property 0 <= start < end <= 24.

    Examples:
    Query Time Range    Open Hours            Answer
    (4, 10)             [(0, 24)]             1.0
    (7, 11)             [(9, 17)]             0.5
    (0, 24)             [(0, 2), (20, 24)]    0.25
    (5, 22)             []                    0.0
"""


def f(query, hours):
    start = query[0]
    end = query[1]
    total = 0
    for s, e in hours:
        a = max(start, s)
        b = min(end, e)
        if a < b:
            total += b - a
    return total / (end - start)


a = [4, 10]
b = [(0, 24)]
print(f(a, b))

a = [7, 11]
b = [(9, 17)]
print(f(a, b))

a = [0, 24]
b = [(0, 2), (20, 24)]
print(f(a, b))

a = [5, 22]
b = []
print(f(a, b))

a = [16, 18]
b = [[11, 14]]
print(f(a, b))
