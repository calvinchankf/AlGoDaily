"""
    We have N different apps with different user growth rates. 
    At a given time t, measured in days, the number of users using an app is g^t (for simplicity we'll allow fractional users), 
    where g is the growth rate for that app. 
    
    These apps will all be launched at the same time and no user ever uses more than one of the apps. 
    We want to know how many total users there are when you add together the number of users from each app.
    
    After how many full days will we have 1 billion total users across the N apps?

    Example 1
    growthRates = [1.5]
    output = 52 because 1.5^52 = 1,434,648,375
    
    Example 2
    growthRates = [1.1, 1.2, 1.3]
    output = 79 because 1.1^79 + 1.2^79 + 1.3^79 = 1,005,319,279
    
    Example 3
    growthRates = [1.01, 1.02]
    output = 1047 because 1.01^1047 + 1.02^1047 = 1,010,169,422
"""


def getBillionUsersDay(growthRates):
    left = 1
    right = 2**11  # cannot be larger due to number overflow
    while left < right:
        t = (left + right) // 2
        total = 0
        for g in growthRates:
            total += g**t
        if 10**9 <= total:
            right = t
        else:
            left = t + 1
    return left


# 52
a = [1.5]
print(getBillionUsersDay(a))

# 79
a = [1.1, 1.2, 1.3]
print(getBillionUsersDay(a))

# 1047
a = [1.01, 1.02]
print(getBillionUsersDay(a))
