from collections import defaultdict

"""
    https://leetcode.com/discuss/interview-question/871750/Yelp-OA

    If someone leaves a positive Yelp review of a business, it's a good indicator that they enjoyed the experience and might be interested in similar spots.
    If many of the same users left positive reviews for the same 2 businesses, we can say that those 2 businesses are similar

    One way we can define how similar 2 businesses  are to each other is the percentage of the number of unique users who reviewed both businesses out of the number of unique users who reviewed either one of them.
    In other words, (A && B) / (A || B).

    Given a list of positive reviews and business of interest, find and return the business id from the list of reviews that is the most similar to the business of interest.

    Notes:
    - there is always a result
    - there wont be any ties

    Input:
    target: 10
    reviews: [(1,10),(2,10),(1,11),(2,11),(1,12),(2,12),(3,12)]

    Ouput: 11

    Explanation
    shop10: [1, 2]
    shop11: [1, 2]      <- this is the most similar
    shop12: [1, 2, 3]
"""


def f(target, reviews):
    shopsSet = set()
    graph = defaultdict(set)
    for uId, bId in reviews:
        shopsSet.add(bId)
        graph[bId].add(uId)

    targetBuyers = graph[target]

    resRatio = 0
    res = None
    for shop in shopsSet:
        if shop == target:
            continue
        curBuyers = graph[shop]

        # A and B
        usersInCommon = set()
        for u in targetBuyers:
            if u in curBuyers:
                usersInCommon.add(u)

        # A or B
        usersInEither = set()
        usersInEither |= targetBuyers
        usersInEither |= curBuyers

        ratio = len(usersInCommon) / len(usersInEither)
        if ratio > resRatio:
            resRatio = ratio
            res = shop
    return res


a = 10
b = [(1, 10), (2, 10), (1, 11), (2, 11), (1, 12), (2, 12), (3, 12)]
print(f(a, b))
