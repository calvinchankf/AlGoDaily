from collections import *

"""
    https://leetcode.com/discuss/interview-question/373625/Yelp-or-OA-2019-or-Active-Business

    Given a list of user interaction events on Yelp, return a list of active business ids.

    A business is considered active if in at least 2 event types which has occurrences >= averge for that event across all businesses.

    The average for a given event type is found by averaging any occurencees of the event type across all businesses,
    excluding the businesses where data is not provided.

    e.g.
    Input:
    [
        Event('ads', 7, 3),
        Event('ads', 8, 2),
        Event('ads', 5, 1),
        Event('page_views', 11, 2),
        Event('page_views', 12, 3),
        Event('photo_views', 10, 3),
        Event('reviews', 7, 2),
    ]
    Output:
    [2,3]

    Explanation:

    business    ads     page_views      photo_views     reviews
    1           7       12              10
    2           8       11                              7
    3           5

    For bizId=1, its ads, page_views, photo_views are >= average, count = 3 which is >= 2, so it should be in the result
    For bizId=2, its ads, reviews are >= average, count = 2 which is >= 2, so it should be in the result
    For bizId=3, all of its event_type < averge, bye
"""


class Event:
    def __init__(self, event_type, occurrences, bizId):
        self.event_type = event_type
        self.occurrences = occurrences
        self.bizId = bizId


def f(events):
    eventsTotal = Counter()
    eventsCount = Counter()
    for e in events:
        t = e.event_type
        o = e.occurrences
        eventsTotal[t] += o
        eventsCount[t] += 1

    bizMoreThanAverge = Counter()  # key: val <= businees: count of eventtype >= averge
    for e in events:
        t = e.event_type
        o = e.occurrences
        b = e.bizId
        if o >= eventsTotal[t] / eventsCount[t]:
            bizMoreThanAverge[b] += 1

    res = []
    for b in bizMoreThanAverge:
        if bizMoreThanAverge[b] >= 2:
            res.append(b)
    return res


A = [
    Event('ads', 7, 3),
    Event('ads', 8, 2),
    Event('ads', 5, 1),
    Event('page_views', 11, 2),
    Event('page_views', 12, 3),
    Event('photo_views', 10, 3),
    Event('reviews', 7, 2),
]
print(f(A))
